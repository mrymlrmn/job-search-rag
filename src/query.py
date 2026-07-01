import sqlite3

def ask_user(question):
    with sqlite3.connect("job.db")as conn:
        cursor =conn.cursor()
        cursor.execute('''SELECT job_id, title, company, skills, salary 
                            FROM jobs WHERE title LIKE ? OR company LIKE ? OR skills LIKE ?''',
                            (f"%{question}%", f"%{question}%", f"%{question}%"))
        results = cursor.fetchall()
        return results      