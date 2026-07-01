import streamlit as st
from config import APP_TITLE

def main():
    st.set_page_config(
        page_title=APP_TITLE,
        page_icon="🎓",
        layout="centered"
    )
    st.title(APP_TITLE)
    st.write(
        "Generate a personalized learning plan with the help of Artificial Intelligence."
    )
    st.divider()
    topic = st.text_input(
        "Enter a topic",
        placeholder="For example: Machine Learning"
    )
    generate_button = st.button("Generate study plan")






if __name__ == "__main__":
    main()