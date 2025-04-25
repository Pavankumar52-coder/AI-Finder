# AIFindr — An AI-Powered People Discovery Application
## Thought Process:
Generally now-a-days people are struggling with different types of people who hhas different ypes of vibes or goals or interests. SO, i came up with AIFindr application where the user can able to find their vibe, goal and interest matching persons and can interact with them. It feels like human. AIFindr is a semantic search application that helps users discover people based on interests, goals, and personality "vibes". It will based on using natural language input which will be given by the user. It leverages vector search using FAISS and sentence transformer model(MiniLM),and Google Gemini LLM for explanation why this is a match.

---

## Features:
- **Natural-language matching** — just describe your ideal person's vibes or interests or goals
- **Vector search** using FAISS + SentenceTransformers for fast data retrieval
- **Personality-aware results** based on bio + vibe + goals
- **LLM-powered explanations** via Gemini 2.0 Flash which is a fast model
- **Minimal Streamlit frontend ui** for real-time exploration and interaction with application using ui

---

## Tech Stack:
1. Python - code
2. streamlit ui - frontend
3. backend - FastAPI
4. Embeddings - sentence transformer model(MiniLM)
5. vector DB - FAISS
6. LLM - Gemini(gemini-2.0-flash)
7. Database - SQLite

## Setup Instructions:
1. Clone the repository
2. Use cd command to enter into the project files
3. create virtual environment
4. download necessary libraries or packages using pip command
5. first run the database file, next run the vector/embeddings file
6. Now run the backend file and frontend file
7. visit browser where the streamit ui is running and to test this application.
   
## Deployment
-> We can deploy it using different cloud platforms like Hugging Faces, Heroku, Netlify e.t.c...
-> I can deploy this application using hugging faces by creating space, uploading code files and click ok.
-> The application will run.
