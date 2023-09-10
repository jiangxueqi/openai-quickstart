import sys
import os
import gradio as gr

from domain.translator.pdf_translator import PDFTranslator
from domain.translator.prompt import Prompt
from domain.translator.translation_config import TranslationConfig
from infrastructure.logger.logger import logger
from infrastructure.utils.argument_parser import ArgumentParser

sys.path.append(os.path.dirname(os.path.abspath(__file__)))



def translation(input_file, source_language, target_language, style_template):
    logger.debug(f"[翻译任务]\n源文件: {input_file.name}\n源语言: {source_language}\n目标语言: {target_language}\n翻译风格：{style_template}")
    output_file_path = Translator.translate_pdf(input_file.name, style_template, source_language=source_language, target_language=target_language)
    return output_file_path

def launch_gradio():

    iface = gr.Interface(
        fn=translation,
        title="OpenAI-Translator v2.0(PDF 电子书翻译工具)",
        inputs=[
            gr.File(label="上传PDF文件"),
            gr.Textbox(label="源语言（默认：英文）", placeholder="English", value="English"),
            gr.Textbox(label="目标语言（默认：中文）", placeholder="Chinese", value="Chinese"),
            gr.inputs.Dropdown(choices=["【小说风格】{}".format(Prompt._format_novel_style()),
                                        "【新闻稿风格】{}".format(Prompt._format_news_style()),
                                        "【鲁迅风格】{}".format(Prompt._format_luxun_style())], label="翻译风格"),
        ],
        outputs=[
            gr.File(label="下载翻译文件")
        ],
        allow_flagging="never"
    )

    iface.launch(share=True, server_name="0.0.0.0")

def initialize_translator():
    # 解析命令行
    argument_parser = ArgumentParser()
    args = argument_parser.parse_arguments()

    # 初始化配置单例
    config = TranslationConfig()
    config.initialize(args)
    # 实例化 PDFTranslator 类，并调用 translate_pdf() 方法
    global Translator
    Translator = PDFTranslator(config.model_name)


if __name__ == "__main__":
    # 初始化 translator
    initialize_translator()
    # 启动 Gradio 服务
    launch_gradio()
