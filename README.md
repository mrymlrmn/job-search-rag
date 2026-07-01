# Job Search RAG Chatbot

A simple chatbot that searches job listings from a SQLite database and answers questions using the Groq API.

## How it works

1. Job data is stored in a SQLite database
2. User asks a question in the search box
3. The app searches the database for matching jobs
4. Results are sent to an AI model to generate a natural answer

## Tech Stack

- Python
- SQLite
- Groq API (llama-3.1-8b-instant)
- Streamlit

## Project Structure

```
├── src/
│   ├── database.py
│   ├── query.py
│   └── genrator.py
├── app.py
├── .env
└── requirements.txt
```

## Setup

1. Clone the repo
2. Install dependencies: `pip install -r requirements.txt`
3. Create a `.env` file and add your Groq API key:
```
Groq_Api_Key=your_key_here
```
4. Run the app: `streamlit run app.py`