

class Prompt(object):

    @staticmethod
    def format_single_prompt():
        prompt = """
                你是一个翻译专家，精通各种语言。
                请按照一定的翻译风格，将{source_languange}翻译为{target_language},
                翻译风格如下：{style_template},
                翻译的内容如下：{text}
                """
        return prompt

    @staticmethod
    def format_system_message_prompt():
        """
        翻译任务指令始终由 System 角色承担
        """
        prompt = """
                    你是一个翻译专家，精通各种语言。
                    请按照一定的翻译风格，将{source_languange}翻译为{target_language},
                    翻译风格如下：{style_template}
                    """
        return prompt

    @staticmethod
    def format_human_message_prompt():
        """
        待翻译文本由 Human 角色输入
        """
        prompt = """
                {text}
                """
        return prompt

    @staticmethod
    def _format_novel_style():
        prompt = """
                 要求准确传递原文的情景和语境，同时保持文学风格和人物性格的一致性，注意文学的优美性
                        """
        return prompt

    @staticmethod
    def _format_news_style():
        prompt = """
                  【新闻稿风格】准确无误地传达原文的信息，保持客观公正的立场，同时注意文化差异和词语的选择。
                            """
        return prompt

    @staticmethod
    def _format_luxun_style():
        prompt = """
                      【鲁迅风格】注意保持其独特的讽刺和批判的语言风格，同时准确传达其深刻的社会思考和人文关怀。
                                """
        return prompt
