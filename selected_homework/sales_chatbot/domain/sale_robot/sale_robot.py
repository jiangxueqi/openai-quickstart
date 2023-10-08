import os
from domain.vector_database.real_estate_db import RealEstateDB
from langchain.chat_models import ChatOpenAI
from infrastructure.logger.logger import logger
from infrastructure.utils.get_config import get_openai_model, get_openai_key
from langchain.chains import RetrievalQA


class SaleRobot(object):
    def __init__(self, similarity_score_threshold=0.8, temperature=0):
        os.environ["OPENAI_API_KEY"] = get_openai_key()
        self.vector_db = RealEstateDB()
        self.llm = ChatOpenAI(model_name=get_openai_model(), temperature=temperature)
        self.qa_chain = RetrievalQA.from_chain_type(self.llm, retriever=self.vector_db.get_retriever(similarity_score_threshold))
        self.qa_chain.return_source_documents = True

    def chat(self, message, history):
        logger.info(f"[message]：{message}")
        logger.info(f"[history]：{history}")
        answer = self.qa_chain({"query": message})
        if answer.get('source_documents'):
            logger.info(f"[source_documents]：{answer.get('source_documents')}")
            return answer.get('source_documents')
        elif answer.get('result'):
            logger.info(f"[result]：{answer.get('result')}")
            return answer.get('result')
        else:
            return "很抱歉，这个问题暂时没有答案，请重新提问！"