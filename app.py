from dotenv import load_dotenv
load_dotenv()

import os
import sqlite3
import streamlit as st
import google.generativeai as genai


# =========================
# CONFIGURATION
# =========================

st.set_page_config(
    page_title="Text to SQL",
    page_icon="🗄️"
)

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    st.error("GOOGLE_API_KEY is not configured.")
    st.stop()

genai.configure(api_key=GOOGLE_API_KEY)

DB_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "student.db"
)


# =========================
# GEMINI FUNCTION
# =========================

def get_gemini_response(question, prompt):
    model = genai.GenerativeModel("gemini-3.6-flash")

    response = model.generate_content(
        [prompt, question]
    )

    return response.text.strip()


# =========================
# SQL FUNCTION
# =========================

def read_sql_query(sql):
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute(sql)
    rows = cursor.fetchall()

    connection.close()

    return rows


# =========================
# PROMPT
# =========================

prompt = """
You are an expert in converting English questions into SQL queries.

The SQLite database contains a table named STUDENT.

The STUDENT table has these columns:

NAME
CLASS
SECTION
MARKS

Examples:

Question:
How many student records are present?

SQL:
SELECT COUNT(*) FROM STUDENT;

Question:
Tell me all the students studying in DS class.

SQL:
SELECT * FROM STUDENT WHERE CLASS = 'DS';

Rules:
1. Return ONLY the SQL query.
2. Do not use markdown code blocks.
3. Do not include ```sql.
4. Do not include explanations.
5. Use SQLite-compatible SQL.
"""


# =========================
# STREAMLIT UI
# =========================

st.title("🗄️ Text to SQL")
st.write("Ask a question about the student database in plain English.")

question = st.text_input(
    "Enter your question:",
    placeholder="Example: Show students who scored more than 80"
)

if st.button("Ask"):

    if not question.strip():
        st.warning("Please enter a question.")
        st.stop()

    try:
        sql_query = get_gemini_response(
            question,
            prompt
        )

        st.subheader("Generated SQL")
        st.code(sql_query, language="sql")

        data = read_sql_query(sql_query)

        st.subheader("Result")

        if data:
            for row in data:
                st.write(row)
        else:
            st.info("No records found.")

    except Exception as e:
        st.error(f"Error: {e}")