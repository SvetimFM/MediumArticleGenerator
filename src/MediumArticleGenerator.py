from enum import Enum

from data.apikey import API_KEY
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate


def get_llm():
    return OpenAI(temperature=0.8, openai_api_key=API_KEY)


def serve_title_template(topic: str):
    title_template = PromptTemplate(
        input_variables=['topic', 'language'],
        template="Article Title: A succinct yet powerful title that encapsulates the essence of the article on "
                 "{topic} in {language}. The title should be a balanced fusion of creativity and clarity, making use "
                 "of the provided inputs to directly address the interests and needs of the target audience."
    )
    return title_template.format(topic=topic, language="English")


