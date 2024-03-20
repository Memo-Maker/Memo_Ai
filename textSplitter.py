from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema.document import Document

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=50,
    length_function=len,
)

docs = [Document(page_content=x) for x in text_splitter.split_text(result["text"])]

split_docs = text_splitter.split_documents(docs)

len(split_docs)