# Text-to-SQL with Gemini

An AI-powered Text-to-SQL application that converts natural language questions into SQL queries using Google Gemini and retrieves results from a SQLite database through an interactive Streamlit interface.

## Features

* Convert natural language questions into SQL queries
* Generate SQLite-compatible SQL using Google Gemini
* Execute generated queries against a SQLite database
* Display generated SQL and query results
* Simple Streamlit-based user interface
* Environment-variable based API key configuration

## Tech Stack

* **Python**
* **Streamlit**
* **Google Gemini API**
* **SQLite**
* **python-dotenv**

## How It Works

```text
Natural Language Question
          ↓
      Streamlit UI
          ↓
     Google Gemini
          ↓
     SQL Query
          ↓
    SQLite Database
          ↓
      Query Result
```

## Project Structure

```text
TextToSQL-Gemini/
│
├── app.py
├── create_db.py
├── sql.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/TextToSQL-Gemini.git
cd TextToSQL-Gemini
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv .venv
```

Activate it:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the Gemini API key

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_google_api_key_here
```

Do not commit the `.env` file to GitHub.

### 5. Create the database

```bash
python create_db.py
```

### 6. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

## Example Queries

You can ask questions such as:

```text
How many students are there?

Show all students.

Show students from the DS class.

Who scored more than 80?

What is the average marks?

Show the student with the highest marks.
```

## Security

The Gemini API key is loaded from an environment variable and should never be stored directly in the source code or committed to GitHub.

## Future Improvements

* SQL query validation
* Read-only query restrictions
* Better database schema handling
* Improved error handling for invalid SQL
* Support for multiple database tables
* Query history
* Data visualization for query results

## License

This project is intended for educational and portfolio purposes.
