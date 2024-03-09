from enum import Enum

from data.apikey import API_KEY
from langchain.chains import LLMChain
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate

TITLE_GENERATOR_TEMPLATE = "Article Title: A succinct yet powerful title encapsulating the essence of the article " \
                           "on {topic}. output should be only in {output_language}. if it cannot be produced in that " \
                           "language, produce output stating why output could not be produced. Try hard to produce" \
                           "output in the {output_language}. The title should be a balanced fusion of creativity " \
                           "and clarity, making use of the provided inputs to directly address the interests and" \
                           " needs of the target audience. Do not provide translation."


def get_llm():
    return OpenAI(temperature=0.8, openai_api_key=API_KEY)


def get_title_output_chain():
    title_template = PromptTemplate(
        input_variables=['topic', 'output_language'],
        template=TITLE_GENERATOR_TEMPLATE
    )
    return LLMChain(llm=get_llm(), prompt=title_template, verbose=True)


def get_title(values: dict[str, str]) -> str:
    title_chain = get_title_output_chain()
    return title_chain.run(values)
