import os
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from infrastructure.utils.get_config import get_openai_key

class VectorDataBase(object):
    def __init__(self, data_txt_path):
        os.environ["OPENAI_API_KEY"] = get_openai_key()
        self.db_name = self._format_db_name(data_txt_path)
        self.data_content = self._load_data_txt(data_txt_path)
        self.db = self._format_db()

    def _format_db_name(self, data_txt_path):
        data_txt_name = os.path.basename(data_txt_path)
        return os.path.splitext(data_txt_name)[0]

    def _load_data_txt(self, data_txt_path):
        with open(data_txt_path, 'r',  encoding='utf-8') as f:
            data_txt = f.read()
        return data_txt

    def _split_data_txt(self):
        raise NotImplementedError("子类实现具体的分割方法")


    def storage_db(self, docs, local_db_path):
        db = FAISS.from_documents(docs, OpenAIEmbeddings())
        db.save_local(local_db_path)
        return db

    def _format_db(self):
        local_db_path = os.path.abspath(os.path.join(os.path.split(__file__)[0], f"local/{self.db_name}"))
        if os.path.exists(local_db_path):
            return FAISS.load_local(local_db_path, OpenAIEmbeddings())
        else:
            docs = self._split_data_txt()
            return self.storage_db(docs, local_db_path)

    def get_retriever(self, score_threshold=0.8):
        return self.db.as_retriever(search_type="similarity_score_threshold", search_kwargs={"score_threshold": score_threshold})


