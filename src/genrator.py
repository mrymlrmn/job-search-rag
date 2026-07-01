import sqlite3
import os
from dotenv import load_dotenv
from groq import Groq

class Generate:
    def __init__(self,model_name="llama-3.1-8b-instant"):
        self.model_name =model_name
        load_dotenv()
        groq_api_key = os.getenv("Groq_Api_Key")
        self.client =Groq(api_key=groq_api_key)

    def build_prompt(self, question, result):
        jobs_text = ""
        for job in result:
            jobs_text += f"title: {job[1]}, company: {job[2]}, skills: {job[3]}, salary: {job[4]}\n"
        
        prompt = f"""Use the following text to answer the question.if the answer is not
        in the text,say"I do not have enough information.You have the following job data:
    {jobs_text}
    Answer the user question based on this data.
    Question: {question}
    Answer:"""
        return prompt
      
    def generator(self,user_question,result):
        prompt = self.build_prompt(user_question, result)
        chat_completion = self.client.chat.completions.create(
            messages=[{
                "role": "user",
                "content":prompt
            }],
            model= self.model_name,
            temperature=0.2
        )
        return chat_completion.choices[0].message.content

        


