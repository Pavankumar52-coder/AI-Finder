# Import necessary libraries for embedding the sentences
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import sqlite3
import pickle

# Load pre-trained model for embeddings
model = SentenceTransformer('all-MiniLM-L6-v2') # Smal but efficient model

# Connect to SQLite and retrieve profiles from profiles db
conn = sqlite3.connect("profiles.db")
c = conn.cursor()
c.execute("SELECT id, bio, vibe FROM personsdata")
data = c.fetchall()
conn.close()

# Better semantic structure for embeddings to get the accurate output
text_data = [f"Bio: {bio.lower()}. Personality traits: {vibe.lower()}." for _, bio, vibe in data]
embeddings = model.encode(text_data)

# Create FAISS index for fast retrieval
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(np.array(embeddings))

# Save FAISS index
faiss.write_index(index, "personsdata.index")

# Save ID mapping to get the profiles id
id_map = [row[0] for row in data]
with open("id_map.pkl", "wb") as f:
    pickle.dump(id_map, f)

print("Embeddings and FAISS index creation completed.")