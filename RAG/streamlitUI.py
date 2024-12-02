import streamlit as st 
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings 
from langchain.chat_models import ChatOpenAI

st.title("RAG Chat with Multi-LLM Support (Aarabic Ready)")

llm_option = st.sidebar.selectbox("Choose your LLM", ["OpenAI GPT-4", "Cohere", "Hugging Face models"])

uploaded_files = st.file_uploader("Upload your documents (PDF or TXT)", accept_multiple_files=True)

language = st.sidebar.selectbox("Choose language", ["English", "Arabic"])