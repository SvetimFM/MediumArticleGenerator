import streamlit as st
from MediumArticleGenerator import get_llm, serve_title_template

llm = get_llm()


def user_form():
    st.title('Medium Article Generator')
    topic = st.text_input('Enter the topic of the article')
    if topic:
        response = llm(serve_title_template(topic))
        st.write(response)


def main():
    user_form()


if __name__ == '__main__':
    main()