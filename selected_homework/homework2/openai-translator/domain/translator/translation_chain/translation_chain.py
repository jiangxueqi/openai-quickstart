from infrastructure.logger.logger import logger


class TranslationChain(object):
    def __init__(self, model_name, verbose=False):
        self.chain = self.format_chain(model_name, verbose)

    def format_chain(self, model_name, verbose):
        raise NotImplementedError

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
