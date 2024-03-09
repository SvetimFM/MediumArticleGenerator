import streamlit as st
from MediumArticleGenerator import get_llm, get_title

llm = get_llm()

APPLET_TITLE = 'Medium Article Generator'
TOPIC_BOX_TEXT = 'Enter the topic of the article'
OUTPUT_LANGUAGE = 'Enter the output language'

def user_form():
    st.title(APPLET_TITLE)
    topic = st.text_input(TOPIC_BOX_TEXT)
    output_language = st.text_input(OUTPUT_LANGUAGE, 'English')

    if topic:
        response = get_title({'topic': topic,
                              'output_language': output_language
                              })
        st.write(response)


def main():
    user_form()


if __name__ == '__main__':
    main()
