import os

from langchain import LLMChain
from langchain.chat_models import ChatOpenAI
from domain.translator.prompt import Prompt
from langchain.prompts.chat import SystemMessagePromptTemplate, HumanMessagePromptTemplate, ChatPromptTemplate

from infrastructure.logger.logger import logger


class TranslationChain(object):
    def __init__(self, model_name="gpt-3.5-turbo", verbose=False):
        os.environ["OPENAI_API_KEY"] = ""
        self.chain = self._format_chain(model_name, verbose)

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

    def run(self, text, style_template, source_language, target_language):
        result = ""
        try:
            result = self.chain.run({
                "text": text,
                "style_template":style_template,
                "source_language": source_language,
                "target_language": target_language,
            })
        except Exception as e:
            logger.error(f"An error occurred during translation: {e}")
            return result, False
        return result, True


