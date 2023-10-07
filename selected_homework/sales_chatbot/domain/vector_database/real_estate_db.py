import os
from domain.vector_database.vector_database import VectorDataBase
from langchain.text_splitter import CharacterTextSplitter


class RealEstateDB(VectorDataBase):
    def __init__(self):
        data_txt_path = os.path.abspath(os.path.join(os.path.split(__file__)[0], "../../infrastructure/data/real_estate_sales_data.txt"))
        super().__init__(data_txt_path)

    def _split_data_txt(self):
        text_splitter = CharacterTextSplitter(
            separator=r'\d+\.',
            chunk_size=100,
            chunk_overlap=0,
            length_function=len,
            is_separator_regex=True,
        )
        return text_splitter.create_documents([self.data_content])

    def get_relevant_answers(self, query, score_threshold=0.8):
        retriever = self.get_retriever(score_threshold)
        docs = retriever.get_relevant_documents(query)
        answers = [doc.page_content.split("[销售回答] ")[-1] for doc in docs]
        return answers

if __name__ == "__main__":
    vector_database = RealEstateDB()
    query = "小区距离医院远吗？"
    print(vector_database.get_relevant_answers(query))