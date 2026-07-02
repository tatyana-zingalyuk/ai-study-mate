import streamlit as st
from config import APP_TITLE
from llm import generate_response


def main():
    st.set_page_config(
        page_title=APP_TITLE,
        page_icon="🎓",
        layout="centered"
    )
    st.title(APP_TITLE)
    st.markdown(
    """
    ### Welcome! 👋

    AI Study Mate creates personalized study plans powered by Large Language Models.

    Simply choose a topic, your current level, and your learning goal to receive a structured learning roadmap.
    """
    )
    st.write(
        "Generate a personalized learning plan with the help of Artificial Intelligence."
    )
    st.divider()
    topic = st.text_input(
        "📖 Study Topic",
        placeholder="For example: Machine Learning"
    )
    level = st.radio(
        "🎯 Current Level",
        [
            "Beginner",
            "Intermediate",
            "Advanced"
        ]
    )
    goal = st.selectbox(
        "🚀 Learning Goal",
        [
        "Learn from scratch",
        "Prepare for interview",
        "Prepare for exam",
        "University course"
        ]
    )
    generate_button = st.button(
         "🚀 Generate Study Plan",
        use_container_width=True
    )

    if generate_button:

        if not topic:
            st.warning("⚠️ Please enter a study topic.")

        else:
            with st.spinner("AI is generating your study plan..."):
                answer = generate_response(
                    topic,
                    level,
                    goal
                )

            with st.container():
                st.divider()
                st.subheader("📚 Your Personalized Study Plan")
                st.markdown(answer)

    with st.sidebar:

        st.header("About")
        st.write(
            """
            AI Study Mate helps students create structured learning plans using Large Language Models.
            """
        )

        st.header("Technologies")
        st.write(
            """
            • Python 3.13

            • Streamlit
            
            • OpenRouter API
            
            • Large Language Models (LLMs)
            
            • Prompt Engineering
            """
        )

        st.divider()

        st.header("Author")

        st.write(
            """
            Developed by Tatyana Zingalyuk

            AI & Business Systems Analysis Student

            School 21
            """
        )
        









if __name__ == "__main__":
    main()