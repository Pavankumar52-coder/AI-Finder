# Import necessary libraries for backend
from fastapi import FastAPI
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import sqlite3
import os
import pickle
import asyncio
import aiohttp
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY") # Initializing api key

# API Set up, embedding model and faiss vector
app = FastAPI()
model = SentenceTransformer('all-MiniLM-L6-v2')
index = faiss.read_index("personsdata.index")

# Load ID map to get profile id
with open("id_map.pkl", "rb") as f:
    id_list = pickle.load(f)

# Load profile data from profile database
conn = sqlite3.connect("profiles.db")
c = conn.cursor()
c.execute("SELECT id, name, bio, vibe FROM personsdata")
data = c.fetchall()
conn.close()

# Map profile_id to get person data from profile database
id_map = {row[0]: {"name": row[1], "bio": row[2], "vibe": row[3]} for row in data}

# Input model
class Query(BaseModel):
    query: str

# Async version of Gemini API call for llm explanation(optimized version)
async def generate_match_explanation(session, query, profile):
    prompt = (
        f"User is looking for: {query}\n"
        f"Candidate profile:\n"
        f"Name: {profile['name']}\nBio: {profile['bio']}\nVibe: {profile['vibe']}\n\n"
        f"In one short sentence, explain why this person is a good match:"
    )

    url = "https://generativelanguage.googleapis.com/v1/models/gemini-2.0-flash:generateContent" # Gemini-2.0-fash model for fast data retrieval
    headers = {"Content-Type": "application/json"}
    params = {"key": GEMINI_API_KEY}
    data = {
        "contents": [{"parts": [{"text": prompt}]}]
    }

    try:
        async with session.post(url, json=data, headers=headers, params=params) as response:
            response.raise_for_status()
            result = await response.json()
            return result["candidates"][0]["content"]["parts"][0]["text"].strip()
    except Exception as e:
        print("[Gemini ERROR]:", e)
        return "Explanation not available."

# Search api endpoint to search for a person based on vibes, interests...
@app.post("/search")
async def search_people(q: Query):
    query_embedding = model.encode([q.query])
    D, I = index.search(np.array(query_embedding), k=5)

    results = []
    profiles_to_explain = []

    for idx in I[0]:
        profile_id = id_list[idx]
        person_info = id_map.get(profile_id, {})
        if person_info:
            profiles_to_explain.append(person_info)

    # Generate explanations concurrently using gemini llm
    async with aiohttp.ClientSession() as session:
        tasks = [
            generate_match_explanation(session, q.query, profile)
            for profile in profiles_to_explain
        ]
        explanations = await asyncio.gather(*tasks)
    for profile, reason in zip(profiles_to_explain, explanations):
        profile["reason"] = reason
        results.append(profile)

    return {
        "your_prompt": q.query,
        "matches": results
    }