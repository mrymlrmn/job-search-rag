import streamlit as st
from src.query import ask_user
from src.genrator import Generate
import pandas as pd

st.title("Sql_RAG Chatbot")
gen = Generate()
question = st.text_input("Ask tour question.")
if st.button("Send"):
    if question:
        results = ask_user(question)

        if not results:
            st.write("not found")
        else:
            df = pd.DataFrame(results, columns=["id", "title", "company", "skills", "salary"])
            answer = gen.generator(question, results)
            st.write(answer)
            st.dataframe(df)