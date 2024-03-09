from enum import Enum

from data.apikey import API_KEY
from langchain.chains import LLMChain, SimpleSequentialChain
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate


with open('prompts/medium_article_title_generator_prompt.txt', 'r', encoding='utf-8') as file:
    TITLE_GENERATOR_TEMPLATE = file.read()

with open('prompts/medium_article_generator_prompt.txt', 'r', encoding='utf-8') as file:
    ARTICLE_GENERATOR_TEMPLATE = file.read()

GPT4 = 'gpt-4'
GPT3 = "gpt-3.5-turbo-instruct"


def get_llm(llm_name: str = GPT3):
    return OpenAI(model_name=llm_name, temperature=0.8, openai_api_key=API_KEY)


def get_title_output_chain(llm: str):
    title_template = PromptTemplate(
        input_variables=['topic'],
        template=TITLE_GENERATOR_TEMPLATE
    )
    return LLMChain(llm=get_llm(llm), prompt=title_template, verbose=True)


def get_article_output_chain(llm: str):
    article_template = PromptTemplate(
        input_variables=['title'],
        template=ARTICLE_GENERATOR_TEMPLATE
    )
    return LLMChain(llm=get_llm(llm), prompt=article_template, verbose=True)


# clunky non-langchain approach
def get_title(topic: str, llm: str = GPT3) -> str:
    title_chain = get_title_output_chain(llm)
    return title_chain.run(topic)


def get_article(title: str, llm: str = GPT3) -> str:
    article_chain = get_article_output_chain(llm)
    return article_chain.run(title)


# beautiful langchain approach
def get_complete_output(value: str, llm: str = GPT3) -> str:
    overall_chain = SimpleSequentialChain(
        chains=[
            get_title_output_chain(llm),
            get_article_output_chain(llm)
    ])
    return overall_chain.run(value)
