from domain.translator.translation_chain.translation_chain_chatglm2 import Translation_Chain_chatglm2
from domain.translator.translation_chain.translation_chain_gpt import Translation_Chain_GPT


class TranslationChainFactory(object):

    @staticmethod
    def create(model_name, verbose=False):
        if model_name == "gpt-3.5-turbo":
            return Translation_Chain_GPT(model_name, verbose)
        if model_name == "chatglm2-6b":
            return Translation_Chain_chatglm2(model_name, verbose)

