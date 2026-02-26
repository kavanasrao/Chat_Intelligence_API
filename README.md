# 🚀 Chat Intelligence API

AI-powered backend service that transforms unstructured chat conversations into structured meeting summaries, action items, and analytics using FastAPI, LangGraph, and LLM-based extraction.

---

## 📌 Overview

Chat Intelligence API is a production-oriented backend system that:

- Accepts unstructured chat input
- Uses LLM-based extraction (Groq / LLaMA)
- Converts text into structured data
- Stores results in a relational database
- Provides analytics endpoints
- Includes logging, validation, and error handling

This project demonstrates backend architecture design, AI integration, and database-driven APIs.

---

## 🏗 Architecture

Client → FastAPI → LangGraph Agent → Groq LLM → Structured Output → Database → Analytics

Key Components:

- FastAPI (API layer)
- LangGraph (Agent workflow orchestration)
- Groq LLM (Information extraction)
- Pydantic (Validation layer)
- SQLAlchemy (Database ORM)
- Logging (Production-ready logging system)

---

## 🛠 Tech Stack

- Python 3.10+
- FastAPI
- LangGraph
- Groq LLM (LLaMA 3.1)
- SQLAlchemy
- SQLite (can be replaced with PostgreSQL)
- Pydantic
- Logging (RotatingFileHandler)

---

## ⚙️ Features

### ✅ Chat Analysis
- Extracts structured fields from unstructured chat
- Handles missing fields gracefully
- Validates structured output using schema models

### ✅ Database Storage
- Stores:
  - Raw chat text
  - Extracted structured data
  - Status
  - Timestamps

### ✅ Analytics Endpoint
- Total processed chats
- Successful extractions
- Failed extractions

### ✅ Production-Level Practices
- Structured logging
- Error handling with HTTP exceptions
- Environment-based configuration
- Database session management
- Clean modular architecture

---

## 📂 Project Structure
'''
        backend/
        │
        ├── agent/
        │ ├── state.py
        │ ├── logic.py
        │ └── graph.py
        │
        ├── database/
        │ ├── db.py
        │ ├── usermodel.py
        │ └── init__.py
        │
        ├── llm_model/
        │ ├── extract.py
        │ └── prompt.py
        │
        ├── core/
        │ └── config.py
        │
        └── app.py


'''
---

## 🔐 Environment Variables

1. Create a `.env` file:
pythom -m venv myenv

2. Activate:
Windows:
myenv\Scripts\activate


3. Install dependencies:
pip install -r requirements.txt


4. Run server:
uvicorn backend.main:app --reload

5. open :
   http://127.0.0.1:8000/docs


---

## 📊 API Endpoints

### POST /analyse
Analyzes chat and stores structured output.

### GET /Interaction
Returns all stored interactions.

### GET /Interaction/{id}
Returns specific interaction.

### GET /analytics
Returns summary statistics.

### GET /health
Health check endpoint.

---

## 🧠 What This Project Demonstrates

- LLM integration in production backend
- Agent-based workflow orchestration
- Structured extraction with validation
- Error handling and logging best practices
- REST API design
- Database persistence and analytics

---

## 📈 Future Improvements

- Add authentication (JWT)
- Replace SQLite with PostgreSQL
- Add Docker support
- Add request logging middleware
- Add rate limiting
- Add async DB support

---

## 👨‍💻 Author

Kavana S   
Backend Developer | AI Enthusiast


