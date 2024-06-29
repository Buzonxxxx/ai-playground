from dotenv import load_dotenv
from llama_index.core import VectorStoreIndex
from llama_index.core import SimpleDirectoryReader
from llama_index.core import StorageContext
from llama_index.core import load_index_from_storage
from llama_index.core.tools import QueryEngineTool
from llama_index.core.tools import ToolMetadata
from llama_index.llms.openai import OpenAI
from llama_index.core.agent import ReActAgent

load_dotenv()

A_docs = SimpleDirectoryReader(input_files=["電商A-Third Quarter 2023 Results.pdf"]).load_data()
B_docs = SimpleDirectoryReader(input_files=["電商B-Third Quarter 2023 Results.pdf"]).load_data()

A_index = VectorStoreIndex.from_documents(A_docs)
B_index = VectorStoreIndex.from_documents(B_docs)

# Save index
A_index.storage_context.persist(persist_dir="./storage/A")
B_index.storage_context.persist(persist_dir="./storage/B")

# Load index
try:
    storage_context = StorageContext.from_defaults(persist_dir="./storage/A")
    A_index = load_index_from_storage(storage_context)

    storage_context = StorageContext.from_defaults(persist_dir="./storage/B")
    B_index = load_index_from_storage(storage_context)

    index_loaded = True
except:
    index_loaded = False

A_engine = A_index.as_query_engine(similarity_top_k=3)
B_engine = B_index.as_query_engine(similarity_top_k=3)

query_engine_tools = [
    QueryEngineTool(
        query_engine=A_engine,
        metadata=ToolMetadata(
            name="A_Finance",
            description=("用來提供A公司的財務資訊"),
        ),
    ),
    QueryEngineTool(
        query_engine=B_engine,
        metadata=ToolMetadata(
            name="B_Finance",
            description=("用來提供B公司的財務資訊"),
        ),
    ),
]

llm = OpenAI(model="gpt-4o")

agent = ReActAgent.from_tools(query_engine_tools, llm=llm, verbose=True)
agent.chat("請比較一下兩間公司的revenue")