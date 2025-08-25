# Medical Chatbot

A complete end-to-end Medical Chatbot powered by LLMs, LangChain, and Pinecone, with FastAPI backend, ReactJS frontend, and Docker for seamless deployment.

[![Python Version](https://img.shields.io/badge/python-3.13%2B-blue.svg)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115.6-009688.svg)](https://fastapi.tiangolo.com)
[![React](https://img.shields.io/badge/React-NodeJS-61DAFB.svg)](https://reactjs.org)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED.svg)](https://docker.com)
[![RAG](https://img.shields.io/badge/RAG-Enabled-7B61FF.svg)](https://www.pinecone.io/learn/retrieval-augmented-generation/)
[![LangChain](https://img.shields.io/badge/LangChain-0.3.26-AA61FF.svg)](https://python.langchain.com/docs/introduction/)
[![Embeddings](https://img.shields.io/badge/Embeddings-Sentence--BERT(HF)-FFB000.svg)](https://huggingface.co/blog/getting-started-with-embeddings)
[![Vector%20Store](https://img.shields.io/badge/Vector%20Store-Pinecone-00A78E.svg)](https://www.pinecone.io/)
[![LLM](https://img.shields.io/badge/LLM-Gemini-4285F4.svg)](https://aistudio.google.com/prompts/new_chat)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

https://github.com/user-attachments/assets/bd44cf7a-1adb-4f7e-ad0c-dc1081465d49

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Tech Stack](#tech-stack)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Docker Deployment](#docker-deployment)
- [License](#license)

## Overview

The Medical Chatbot is an intelligent conversational AI system designed to provide medical information and answer health-related queries. Built using state-of-the-art technologies including Large Language Models (LLMs), vector databases, and modern web frameworks, it offers accurate, contextual responses based on medical literature and documents.

### Key Capabilities
- **Intelligent Document Search**: Uses RAG (Retrieval-Augmented Generation) to find relevant medical information
- **Natural Conversations**: Powered by Google's Gemini LLM for human-like interactions
- **Real-time Responses**: Fast, efficient processing with modern async architecture
- **Professional UI**: Clean, responsive interface optimized for healthcare use cases

## Features
- **RAG-based Question Answering**: Retrieves relevant context from medical documents before generating responses
- **PDF Document Processing**: Automatically processes and indexes medical literature and documents
- **Vector Similarity Search**: Uses embeddings to find semantically similar content
- **Real-time Chat Interface**: Interactive, responsive chat UI with typing indicators
- **Error Handling**: Comprehensive error management with user-friendly messages


## Architecture
``` text
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│ React Frontend  │────│ FastAPI Backend │────│   Pinecone DB   │
│                 │    │                 │    │                 │
│  • Chat UI      │    │  • LangChain    │    │  • Vector Store │
│  • Responsive   │    │  • API Endpoints│    │  • Embeddings   │
│                 │    │  • RequestHandle│    │  • Similarity   │
│                 │    │  • Error Handle │    │  • FastRetrieval│
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         │                       ▼                       │
         │            ┌─────────────────┐                │
         │            │Document Process │                │
         │            │                 │                │
         │            │  • PDF Loader   │                │
         │            │  • Extract      │                │
         │            │  • Text Splitter│                │
         │            │  • Chunk Process│                │
         │            └─────────────────┘                │
         │                       │                       │
         │                       ▼                       │
         │            ┌─────────────────┐                │
         │            │ HuggingFace     │────────────────┘
         │            │ Embeddings      │
         │            │                 │
         │            │  • Text-to-Vec  │
         │            │  • Pre-trained  │
         │            │  • Transformer  │
         │            │  • 384 Dim Vec  │
         │            └─────────────────┘
         │                       │
         │                       ▼
         └────────────┌─────────────────┐
                      │ Google Gemini   │
                      │ LLM Provider    │
                      │                 │
                      │  • Generation   │
                      │  • Context Aware│
                      │  • Multi-modal  │
                      │  • RAG Support  │
                      └─────────────────┘
┌─────────────────────────────────────────────────────────────┐
│                     Data Flow Process                       │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. User Query ──→ React Frontend ──→ FastAPI Backend       │
│                                                             │
│  2. Query Processing ──→ LangChain ──→ Retriever            │
│                                                             │
│  3. Vector Search ──→ Pinecone DB ──→ Relevant Chunks       │
│                                                             │
│  4. Context + Query ──→ Google Gemini ──→ Generated Response│
│                                                             │
│  5. Response ──→ FastAPI ──→ React ──→ User Interface       │
│                                                             │
└─────────────────────────────────────────────────────────────┘
┌─────────────────────────────────────────────────────────────┐
│                   Document Ingestion Flow                   │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  PDF Documents ──→ Document Loader ──→ Text Splitter        │
│                                                             │
│  Text Chunks ──→ HuggingFace Embeddings ──→ Vector DB       │
│                                                             │
│  Indexed Vectors ──→ Pinecone Storage ──→ Ready for Query   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```
## Tech Stack

### Backend
- **FastAPI**: Modern, fast web framework for building APIs
- **LangChain**: Framework for developing LLM applications
- **Pinecone**: Vector database for similarity search
- **HuggingFace Transformers**: Pre-trained models for embeddings
- **Google Gemini**: Large language model for response generation
- **PyPDF**: PDF document processing
- **Python**: Core programming language

### Frontend
- **React+vite**: Modern JavaScript library for building user interfaces
- **Tailwind CSS**: Utility-first CSS framework
- **Lucide React**: Beautiful icon set
- **Fetch API**: HTTP client for API communication

### DevOps & Deployment
- **Docker**: Containerization platform
- **Docker Compose**: Multi-container deployment
- **Uvicorn**: ASGI server for FastAPI
- **Environment Variables**: Secure configuration management

## Prerequisites

Before setting up the project, ensure you have:

- **Python 3.13+** installed
- **Node.js 22.12+** and **npm/yarn** for frontend development
- **Docker** and **Docker Compose** (for containerized deployment)
- **API Keys** for the following services:
  - [Pinecone](https://www.pinecone.io/) - Vector database
  - [Google AI Studio](https://makersuite.google.com/app/apikey) - Gemini API access

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Saif-000001/medical_chatbot.git
cd medical_chatbot
```

### 2. Backend Setup

```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Frontend Setup

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install
# or
yarn install
```
### Project Structure

```
medical_chatbot/
├── backend/
│   ├── app/
│   │   ├── api/            # API routes
│   │   │   ├── __init__.py
│   │   │   └── routes.py
│   │   ├── core/           # Configurations & settings
│   │   │   ├── __init__.py
│   │   │   └── config.py
│   │   ├── models/         # Database / data models
│   │   │   ├── __init__.py
│   │   │   └── chat.py
│   │   ├── services/       # Business logic & chatbot service
│   │   │   ├── __init__.py
│   │   │   └── chatbot.py
│   │   ├── utils/          # Helper functions
│   │   │   ├── __init__.py
│   │   │   └── documents.py
│   │   ├── __init__.py
│   │   └── main.py         # FastAPI entrypoint
│   ├── data/               # Storage / datasets
│   ├── .env                # Environment variables
│   ├── requirements.txt    # Python dependencies
│   ├── Dockerfile          # Docker build file
│   ├── .dockerignore
│   ├── .venv
│   └── setup.py
├── frontend/
│   ├── src/
│   │   ├── assets/                 # Images, logos, etc.
│   │   ├── components/             # Reusable UI components
│   │   │   ├── ChatMessage.jsx     # Single chat message bubble
│   │   │   ├── EmojiPicker.jsx     # emoji picker
│   │   │   ├── MessageInput.jsx    # Input field + send button
│   │   │   └── Header.jsx          # App header (branding, title)
│   │   ├── config/                 
│   │   │   ├── config.js           # API base URL & frontend configs
│   │   ├── hooks/                  # 🔹 Custom React hooks
│   │   │   ├── useChat.js          # Manages chatbot state & API calls
│   │   │   ├── useEmoji.js         # Manages chatbot state & API calls
│   │   │   ├── useScroll.js        # Auto-scrolls chat window to bottom
│   │   │   └── useFormatTime.js    # Formats timestamps for messages
│   │   ├── pages/
│   │   │   └── MedicalChatbot.jsx  # Main chatbot page (UI + logic)
│   │   ├── main.jsx                # ReactDOM entry point
│   │   └── index.css               # include tawilwind library 
│   ├── .env                        # Environment variables (API URL, etc.)
│   ├── index.html                  # HTML entry point
│   ├── package.json                # Project dependencies & scripts
│   ├── tailwind.config.js          # tailwind configuration
│   └── vite.config.js              # Vite configuration 
├── docker-compose.yml              # Docker Compose configuration
├── .gitignore                      # Git ignore rules
├── README.md                       # Project documentation
└── LICENSE                         # MIT License
```
## Configuration

### Environment Variables backend

Create a `.env` file in the project root:

```env
# Pinecone Configuration
PINECONE_API_KEY=your_pinecone_api_key_here

# Google AI Configuration
GOOGLE_API_KEY=your_google_ai_api_key_here

```
### API Keys Setup

1. **Pinecone API Key**:
   - Sign up at [Pinecone](https://www.pinecone.io/)
   - Create a new project
   - Copy the API key from your dashboard

2. **Google AI API Key**:
   - Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Create a new API key
   - Copy the generated key
### Environment Variables frontend

Create a `.env` file in the project root:

```env
# backend localhost
VITE_API_BASE_URL="http://localhost:8000"

```

### Document Preparation

1. Create a `data/` directory in the project root
2. Add your documents to this directory
3. The system will automatically process these documents during initialization

## Usage

### Development Mode

#### Start Backend Server

```bash
# From project root
cd backend
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

#### Start Frontend Development Server

```bash
# From frontend directory
cd frontend
npm start
# or
yarn start
```
##### Live UI: https://medicalchatbotapp.netlify.app/

#### Initialize Vector Database

```bash
# Make a POST request to initialize documents
curl -X POST http://localhost:8000/initialize
```

## API Documentation

### Endpoints

#### `GET /` - Root Endpoint
```json
{
  "message": "Medical Chatbot API is running"
}
```

#### `POST /chat` - Chat with Bot

**Request Body:**
```json
{
  "message": "What are the symptoms of diabetes?"
}
```

**Response:**
```json
{
  "answer": "Common symptoms of diabetes include increased thirst, frequent urination, and unexplained weight loss. However, you should consult a healthcare professional for proper diagnosis.",
}
```

#### `POST /initialize` - Initialize Vector Store

Processes PDF documents and creates vector embeddings.

**Response:**
```json
{
  "message": "Vector store initialized successfully"
}
```

### Interactive API Documentation

Once the server is running, visit:
- **Swagger UI**: `http://localhost:8000/docs`

## Docker Deployment

### Using Docker Compose (Recommended)

```bash
# build backend image
cd backend
docker build -t backend .
#build frontend image
cd frontend
docker build -t frontend .

# Run in background
docker compose up --build

# Stop services
docker compose down
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
