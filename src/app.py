import streamlit as st
from MediumArticleGenerator import get_llm, get_complete_output


APPLET_TITLE = 'Medium Article Generator'
TOPIC_BOX_TEXT = 'Enter the topic of the article'
OUTPUT_LANGUAGE = 'Enter the output language'


def user_form():
    st.title(APPLET_TITLE)
    topic = st.text_input(TOPIC_BOX_TEXT)

# sequential chains are nice, but limit one to a single input/output variable.
    if topic:
        article = get_complete_output(topic)
        st.write(article)

# example of how things would have to be done without langchain
        # if topic:
        #   article = get_complete_output(topic)
        #   st.write(article)
        #
        #   article_title = get_title({
        #       'topic': topic,
        #   })
        #
        # article = get_article({
        #     'title': article_title,
        # })
        #
        # st.write(article_title)
        # st.write(article)


def main():
    user_form()


if __name__ == '__main__':
    main()
