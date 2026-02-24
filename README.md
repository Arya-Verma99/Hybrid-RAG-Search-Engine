<h1 align="center"> 🚀 Multi-Document Hybrid RAG Search Engine </h1>
<align="center" (With Real-Time Web Search Integration)>

## 📌 Overview
The Multi-Document Hybrid RAG Search Engine is an AI-powered search assistant that combines:
* Multi-document semantic search
* Real-time web search
* Retrieval-Augmented Generation (RAG)
* Interactive Streamlit chatbot UI

This system enables users to retrieve and synthesize information from internal knowledge sources (PDFs, text files, Wikipedia) along with live internet data using Tavily Search.

The project mirrors real-world enterprise AI copilots that blend private knowledge bases with dynamic web intelligence.

## 🎯 Objective
The objective of this project is to design and implement a Hybrid RAG system that:
* Builds a searchable knowledge base from multiple documents
* Uses FAISS for semantic vector search
* Integrates Tavily for real-time web search
* Dynamically routes queries (Document / Web / Hybrid)
* Generates citation-aware, grounded answers
* Provides a transparent and interactive chatbot interface

## 🏗️ Architecture Overview
#### Frontend (app.py) :
Streamlit web application that allows:
* Document upload
* Chat-based querying
* Web search toggle
* Source-aware response display

#### Document Loader : 
Loads PDFs, text files, and Wikipedia pages using LangChain loaders with metadata consistency.

#### Text Splitter : 
Splits documents into overlapping chunks for improved retrieval accuracy.

#### Embeddings Module : 
Generates vector embeddings using Sentence Transformers.

#### Vector Store (FAISS) : 
Stores embeddings locally and enables fast semantic similarity search.

#### Query Router : 
Classifies user queries into:
* Document-based
* Web-based
* Hybrid

#### Web Search Integration : 
Uses Tavily Search API to fetch real-time information including titles, snippets, and URLs.

#### RAG Chain : 
Combines retrieved context with LLM to generate grounded, citation-aware responses.

## 🧠 Core Features
* Multi-document semantic retrieval using FAISS
* Hybrid search (Documents + Real-Time Web)
* Intelligent query routing
* Citation-aware answer generation
* Clear distinction between document and web sources
* Interactive Streamlit chatbot UI
* Persistent vector indexing for performance optimization

## 🛠️ Tech Stack
* Programming Language : Python
* LLM Orchestration : LangChain
* Vector Database : FAISS
* Web Search : Tavily Search
* Frontend : Streamlit
* Embeddings : Sentence Transformers

## ⚙️ Installation & Setup
1. Clone Repository : Obtain the project source code from GitHub. 

2. Create Virtual Environment :
python -m venv venv
venv\Scripts\activate

3. Install Dependencies : pip install -r requirements.txt

4. Configure API Keys : GROQ_API_KEY=your_groq_api_key
   
TAVILY_API_KEY=your_tavily_api_key

Add .env to .gitignore

5. Run the Application : streamlit run app.py

## ☁️ Deployment (Streamlit Cloud)
* Push project to GitHub
* Go to https://share.streamlit.io
* Connect GitHub repository
* Set app.py as main file
* Add API keys in Secrets
* Click Deploy
The app will be live at : https://your-app-name.streamlit.app

## 📊 Results
* Answers questions from multiple documents simultaneously
* Combines document knowledge with real-time web data
* Provides grounded, citation-aware responses
* Distinguishes clearly between document and web sources
* Optimized retrieval using FAISS indexing
* Interactive and transparent chatbot interface

## 🔮 Future Enhancements
* Advanced LLM-based query classification
* Support for additional file formats (DOCX, CSV, DB connections)
* Role-based authentication system
* Monitoring and analytics dashboard
* Multi-Language Support

## 🎓 Key Learning Outcomes
* Multi-document RAG system design
* Hybrid retrieval architecture
* Real-time web integration
* Citation-aware answer generation
* LangChain + Streamlit application development
* Explainable AI system design

## 📌 Conclusion 
This project demonstrates how to build a production-style Hybrid RAG system that integrates private document knowledge with live web search. It showcases expertise in semantic retrieval, LLM orchestration, explainability, and full-stack AI application development.

#### 👨‍💻 Author 
Pooja Verma
AI Engineer | Data Science Enthusiast
Focused on building practical, scalable AI systems.
