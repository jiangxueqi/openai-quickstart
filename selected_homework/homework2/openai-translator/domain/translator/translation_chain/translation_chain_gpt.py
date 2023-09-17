import os

from langchain import LLMChain
from langchain.chat_models import ChatOpenAI
from domain.translator.prompt import Prompt
from langchain.prompts.chat import SystemMessagePromptTemplate, HumanMessagePromptTemplate, ChatPromptTemplate
from domain.translator.translation_chain.translation_chain import TranslationChain


class Translation_Chain_GPT(TranslationChain):

    def __init__(self, model_name="gpt-3.5-turbo", verbose=False):
        os.environ["OPENAI_API_KEY"] = ""
        super().__init__(model_name=model_name, verbose=verbose)

    def _format_chain(self, model_name, verbose):
        system_message_prompt = Prompt.format_system_message_prompt()
        system_message_prompt_template = SystemMessagePromptTemplate.from_template(system_message_prompt)
        human_message_prompt = Prompt.format_human_message_prompt()
        human_message_prompt_template = HumanMessagePromptTemplate.from_template(human_message_prompt)
        chat_prompt_template = ChatPromptTemplate.from_messages(
            [system_message_prompt_template, human_message_prompt_template]
        )
        chat = ChatOpenAI(model_name=model_name, temperature=0, verbose=verbose)
        return LLMChain(llm=chat, prompt=chat_prompt_template, verbose=verbose)
