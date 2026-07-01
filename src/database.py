import sqlite3
     
def creat_table():
    with sqlite3.connect("job.db")as conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS  jobs(
            job_id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            company TEXT,
            skills TEXT,
            salary INTEGER

        )''')
       
        conn.commit()
   
def add_jobs():
    sample_jobs =[
        ('data sceientist','benz','python',42000),
        ('ai engineer','telekom','sql',55000),
        ('machin learning','DHL','sklrearn',62000)
    ] 
    with sqlite3.connect("job.db") as conn:
        cursor = conn.cursor()
        cursor.executemany('''INSERT INTO jobs(
                           title, company, skills, salary) VALUES (?, ?, ?, ?)''',sample_jobs)
        
        conn.commit()
def add_one_job(title, company, skills, salary):  
    with sqlite3.connect("job.db") as conn:
        cursor = conn.cursor() 
        cursor.execute('''INSERT INTO jobs(
                           title, company, skills, salary) VALUES (?, ?, ?, ?)''', (title, company, skills, salary))
        conn.commit()

def get_all_data():
    with sqlite3.connect("job.db") as conn:
        cursor =conn.cursor()
        cursor.execute('''SELECT job_id ,title, company, skills, salary FROM jobs''')
        rows = cursor.fetchall()
        for row in rows:
            print(row)
def filter_by_title(title):   
    with sqlite3.connect("job.db") as conn:
        cursor = conn.cursor()
        cursor.execute('''SELECT job_id ,title, company, skills, salary FROM jobs WHERE
                        title =?''',(title,))
        results=cursor.fetchall() 
        for result in results:
            print(result)
def filter_by_company(company):
    with sqlite3.connect("job.db") as conn:
        cursor = conn.cursor()         
        cursor.execute('''SELECT job_id ,title, company, skills, salary FROM jobs WHERE
                        company =?''',(company,))
        results=cursor.fetchall() 
        for result in results:
            print(result)
def filter_by_skills(skills): 
    with sqlite3.connect("job.db") as conn:
        cursor = conn.cursor()            
        cursor.execute('''SELECT job_id ,title, company, skills, salary FROM jobs WHERE
                        skills =?''',(skills,))
        results=cursor.fetchall() 
        for result in results:
            print(result)      
# creat_table()
# add_jobs()
# # add_one_job('data sceientist','o2','java',82000)
# select_data()
filter_by_company("benz")
filter_by_skills('python')
filter_by_title('data sceientist')