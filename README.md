# AI Agent with Retrieval-Augmented Generation (RAG) on Azure

This project implements an AI Agent capable of answering user queries either directly or by retrieving relevant information from internal documents using a Retrieval-Augmented Generation (RAG) approach.  
The application is built using FastAPI and deployed on Azure App Service with a public endpoint.

---

## 1. Architecture Overview

**High-level flow:**

User → FastAPI (`/ask`) → AI Agent (Decision Logic)  
→ (Optional) Document Retrieval → Response + Sources

**Components:**
- **AI Agent**: Decides whether a query requires document retrieval or can be answered directly.
- **RAG Module**: Retrieves relevant document content when required.
- **Session Memory**: Maintains session-level conversation history.
- **FastAPI Backend**: Exposes REST API endpoints.
- **Azure App Service**: Hosts the application.

---

## 2. Tech Stack

- **Language**: Python 3.10  
- **Backend Framework**: FastAPI  
- **AI / LLM Integration**: OpenAI-compatible interface (Azure-ready)  
- **Retrieval Logic**: Lightweight in-memory retrieval (FAISS removed for deployment stability)  
- **Deployment**: Azure App Service (Linux, Free Tier F1)  
- **Server**: Gunicorn  

---

## 3. API Specification

### Endpoint


POST

### Request Body
```json
{
  "query": "string",
  "session_id": "optional"
}

Response
{
  "answer": "string",
  "source": ["doc1.txt", "doc2.txt"]
}


Local Setup

git clone https://github.com/nextrack17/ai-agent-rag.git
cd ai-agent-rag
python -m venv venv
venv\Scripts\activate   # Windows
pip install -r requirements.txt
uvicorn app.main:app --reload


Open:

    http://127.0.0.1:8000/docs


Azure Deployment

- Create Azure App Service (Linux, Python 3.10)
- Connect GitHub repository via Deployment Center
- Set Startup Command:
   gunicorn app.main:app -k uvicorn.workers.UvicornWorker --workers 1 --timeout 120

Restart the app
Access live API via:

    https://ai-agent-rag-nextrack-h7fyfpfzajf7bgad.southindia-01.azurewebsites.net/



Design Decisions

Agent Routing

- Implemented lightweight, deterministic routing logic to decide whether document retrieval is required.
- Keeps behavior transparent and easy to evaluate.

Retrieval Strategy (Important Note)

- FAISS was used during local development for vector-based retrieval.
- During Azure deployment (Free F1 tier), FAISS caused native dependency/runtime issues.
- To ensure deployment stability and reliability, FAISS was replaced with a lightweight in-memory retrieval mechanism for    the deployed version.


Session Memory

- Implemented simple in-memory session tracking using session_id.
- Demonstrates agent memory without external stateful services.



Limitations:

- No authentication or authorization.
- In-memory document retrieval (not optimized for large-scale datasets).
- Session memory resets on app restart.
- LLM-based reasoning can be extended further.



Future Improvements

- Re-enable FAISS or Azure AI Search on paid Azure plans.
- Integrate Azure OpenAI embeddings and chat completions.
- Add persistent memory (Redis / Cosmos DB).
- Add user authentication.
- Improve agent decision-making using LLM-based tool selection.


Live Deployment
- Base URL:
   https://ai-agent-rag-nextrack-h7fyfpfzajf7bgad.southindia-01.azurewebsites.net/

- Swagger UI:
   https://ai-agent-rag-nextrack-h7fyfpfzajf7bgad.southindia-01.azurewebsites.net/docs



Author
  -Divyanshu Pandey



