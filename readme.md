# Enterprise IT Support Agentic RAG Copilot

An intelligent enterprise IT support assistant powered by **Agentic RAG, LangGraph, LangChain, Groq, Pinecone, Tavily, and FastAPI**. It retrieves relevant internal knowledge, evaluates evidence, makes intelligent retrieval decisions, and generates context-aware responses to employee IT support queries.

## Overview

Enterprise IT teams handle repetitive support requests related to VPN connectivity, password resets, MFA configuration, software installation, network troubleshooting, and hardware issues.

Traditional keyword-based search often struggles to identify relevant documentation, while generic AI chatbots can generate inaccurate or unsupported answers.

**Enterprise IT Support Agentic RAG Copilot** combines Retrieval-Augmented Generation (RAG) with agent-based decision-making to provide reliable, knowledge-grounded IT support.

The system prioritizes internal company documentation, evaluates retrieved evidence, and uses external web search when internal information is insufficient.

## Key Features

- **Intelligent Query Routing:** Classifies user queries and determines the appropriate response path.
- **Agentic RAG Workflow:** Uses LangGraph to manage retrieval, evaluation, and conditional routing.
- **Private Knowledge Retrieval:** Retrieves relevant information from enterprise documents using Pinecone.
- **Evidence Grading:** Evaluates retrieved context before generating answers.
- **Query Rewriting:** Improves search queries when retrieved evidence is insufficient.
- **Web Search Fallback:** Uses Tavily to retrieve external information when required.
- **Grounded Responses:** Generates answers based on retrieved supporting evidence.
- **Document Ingestion:** Supports uploading and processing enterprise knowledge documents.
- **Execution Tracing:** Provides visibility into agent decisions and retrieval workflows.

## System Architecture

```text
              Employee / User
                     |
                     v
              FastAPI Backend
                     |
                     v
               LangGraph Agent
                     |
                     v
              Query Classification
                     |
           +---------+---------+
           |                   |
           v                   v
      Private KB           Direct Answer
      Retrieval
           |
           v
      Evidence Grading
           |
      +----+----+
      |         |
     Good      Weak
      |         |
      v         v
   Generate   Tavily Search
   Answer         |
                  v
            Web Evidence Grading
                  |
            +-----+-----+
            |           |
           Good        Weak
            |           |
            v           v
        Generate    Query Rewrite
        Answer          |
                        v
                   Retry Retrieval
```

## Agentic RAG Workflow

The system follows a decision-driven workflow:

1. **Query Classification:** Identifies whether the query requires a direct response or IT knowledge retrieval.
2. **Private KB Retrieval:** Searches the enterprise knowledge base using Pinecone.
3. **Evidence Evaluation:** Grades retrieved documents for relevance and usefulness.
4. **External Search:** Uses Tavily when internal knowledge is insufficient.
5. **Query Rewriting:** Improves weak queries and retries retrieval.
6. **Response Generation:** Produces context-aware answers grounded in retrieved evidence.
7. **Execution Trace:** Tracks routing decisions and retrieval operations.

## Technology Stack

| Component | Technology | Purpose |
|---|---|---|
| Programming Language | Python | Core development |
| Agent Orchestration | LangGraph | Stateful agent workflows |
| LLM Framework | LangChain | LLM integration |
| LLM Provider | Groq | LLM inference |
| Vector Database | Pinecone | Semantic knowledge retrieval |
| Embeddings | HuggingFace | Text embeddings |
| Web Search | Tavily | External information retrieval |
| Backend | FastAPI | REST API development |
| Frontend | HTML, CSS, JavaScript | User interface |
| Templates | Jinja2 | Dynamic HTML rendering |
| Document Processing | PyPDF, python-docx | Document extraction |
| Database | SQLite | Audit logging |
| Deployment | Docker | Containerization |

## Example Use Cases

### 1. VPN Troubleshooting

**User Query:**

How do I connect to the company VPN from home?

**Workflow:**

```text
Query
  → Private KB Retrieval
  → Evidence Grading
  → Grounded Response
```

### 2. Password and MFA Policy

**User Query:**

Can IT support ask me to share my MFA code?

**Workflow:**

```text
Query
  → Internal Policy Retrieval
  → Evidence Evaluation
  → Policy-Based Response
```

### 3. External Information Retrieval

**User Query:**

What is the latest Microsoft Teams outage guidance?

**Workflow:**

```text
Query
  → Private KB Retrieval
  → Weak Evidence
  → Tavily Web Search
  → Web Evidence Grading
  → Response with External Sources
```

### 4. Query Rewriting

**User Query:**

My work communication application is not working properly after an update.

**Workflow:**

```text
Query
  → Private KB Retrieval
  → Evidence Evaluation
  → Query Rewriting
  → Retry Retrieval
  → Response Generation
```

## Project Structure

```text
enterprise-it-support-copilot/
│
├── backend/
│   └── app/
│       ├── api/
│       │   └── routes/
│       ├── agents/
│       ├── graph/
│       ├── rag/
│       ├── tools/
│       ├── database/
│       ├── core/
│       └── main.py
│
├── frontend/
│   └── streamlit_app.py
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── evaluation/
│
├── tests/
├── scripts/
├── notebooks/
│
├── .env.example
├── .gitignore
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/enterprise-it-support-copilot.git

cd enterprise-it-support-copilot
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate on Windows:

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root.

```env
GROQ_API_KEY=your_groq_api_key
GROQ_MODEL=your_groq_model_id

TAVILY_API_KEY=your_tavily_api_key

PINECONE_API_KEY=your_pinecone_api_key
PINECONE_INDEX_NAME=enterprise-it-support
PINECONE_NAMESPACE=company-it-kb
```

### 5. Run the Application

Start the FastAPI application:

```bash
python -m uvicorn backend.app.main:app --reload
```

Access the application:

- Backend: `http://127.0.0.1:8000`
- API Documentation: `http://127.0.0.1:8000/docs`

## License

This project is developed for educational and portfolio purposes.

---

**Enterprise IT Support Agentic RAG Copilot**  
*Building intelligent IT support systems with Agentic AI and Retrieval-Augmented Generation.*

## 👨‍💻 Author

**Shivam Singh**

 AI Engineer 

- GitHub: [@shivamsingh-itds](https://github.com/shivamsingh-itds)
- LinkedIn: [Shivam Singh](https://www.linkedin.com/in/shivamsingh-itds/)

---

⭐ If you find this project interesting, consider giving it a star!
