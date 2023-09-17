from langchain import LLMChain, PromptTemplate
from domain.translator.prompt import Prompt
from transformers import AutoModel


from domain.translator.translation_chain.translation_chain import TranslationChain


class Translation_Chain_chatglm2(TranslationChain):

    def __init__(self, model_name="THUDM/chatglm2-6b", verbose=False):
        super().__init__(model_name=model_name, verbose=verbose)

    def _format_chain(self, model_name, verbose):
        single_prompt = Prompt.format_single_prompt()
        prompt_template = PromptTemplate.from_template(single_prompt)
        model = AutoModel.from_pretrained(model_name)
        return LLMChain(llm=model, prompt=prompt_template, verbose=verbose)