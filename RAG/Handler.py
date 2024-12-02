from PyPDF2 import PdfReader 
from langchain.text_splitter import RecursiveCharacterTextSplitter
from streamlitUI import uploaded_files , st, FAISS, OpenAIEmbeddings, ChatOpenAI, llm_option

if uploaded_files:
    texts = []
    for file in uploaded_files: 
        reader = PdfReader(file)
        text = "".join([page.extract_text() for page in reader.pages])
        texts.append(text)

    # Split and process text for embeddings 
    text_splitter = RecursiveCharacterTextSplitter(chink_size=500, chunk_ovelap=50)    
    documents = text_splitter.create_documents(texts)

    # Create embeddings 
    embeddings = OpenAIEmbeddings()
    vector_db = FAISS.from_documents(documents, embeddings)
    st.succes("Documents uploaded and processed successfuly! ")


# Chat interference 

if st.button("Start Chat"):
    user_input = st.text_input("Your question:")
    if user_input: 
        retriever = vector_db.as_retriever(search_type="similarity", search_kwargs={"k":5})
        related_docs = retriever.get_relevant_documents(user_input)

        context = "\n".join([doc.page_content for doc in related_docs])

        if llm_option == "OpenAI GPT-4":
            llm = ChatOpenAI(model_name="gpt-4")
        elif llm_option == "Cohere":
            from cohere import Client
            client = Client("api_key")
            llm = lambda text: client.generate(prompt=text).text
        else:
            from transformers import pipeline 
            llm = pipeline("text-generation", model="gpt2")    

        response = llm.generate(context + "\n\n" + user_input)            
        st.write(response)
