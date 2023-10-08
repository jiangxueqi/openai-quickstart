import os
import gradio as gr
from domain.factory.robot_factory import SaleRobotFactory


def sale_chat(message, history):
    sale_robot = SaleRobotFactory.create()
    return sale_robot.chat(message, history)

def launch_gradio():
    demo = gr.ChatInterface(
        fn=sale_chat,
        title="房产销售",
        # retry_btn=None,
        # undo_btn=None,
        chatbot=gr.Chatbot(height=600),
    )
    demo.launch(share=True, server_name="0.0.0.0", server_port=8000)

if __name__ == "__main__":
    launch_gradio()