# Import libraries to store data in database
import sqlite3
import random

# Connect to SQLite DB
conn = sqlite3.connect('profiles.db')
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS personsdata (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        bio TEXT,
        vibe TEXT
    )
''')

# List of possible names for generating random profiles
names = [
    "Raj", "Ayesha", "Liam", "Emma", "Sophia", "John", "Mia", "David", "Isabella", "Ethan",
    "Olivia", "Liam", "Charlotte", "William", "James", "Benjamin", "Amelia", "Lucas", "Zoe",
    "Henry", "Lily", "Sebastian", "Ella", "Alexander", "Grace", "Jackson", "Scarlett", "Jackson",
    "Harper", "Matthew", "Chloe", "Isaac", "Victoria", "Oliver", "Elijah", "Aiden", "Ava", "Mason",
    "Nora", "Evelyn", "Jack", "Sophie", "Samuel", "Michael", "Abigail", "Nathan", "Leah", "Matthew",
    "Daniel", "Emily", "Landon", "Daisy", "Max", "Zoey", "Ryan", "Megan", "Leo", "Charlotte",
    "Benjamin", "Lucas", "Dylan", "Grace", "Gabriel", "Amos", "Chloe", "Jayden", "Sienna",
    "Cooper", "Zoe", "Liam", "Evan", "Sophie", "Lola", "Harper", "Eleanor", "Mila", "Hunter"
]

# List of possible bios for above names
bios = [
    "Startup enthusiast into biohacking, fitness, and EDM", "Poet and wildlife photographer", "Crypto trader + hardcore minimalist",
    "Developer with a passion for gaming and tech innovation", "Digital artist and AI researcher", "Machine learning enthusiast",
    "Social media manager and content creator", "Mental health advocate and yoga practitioner", "Business strategist",
    "Music producer and vinyl collector", "UX/UI designer with a focus on inclusivity", "Travel blogger and adventure seeker",
    "Food critic and amateur chef", "Yoga instructor and mindfulness coach", "Environmental activist", "Scientist and public speaker",
    "Tech entrepreneur and startup founder", "Psychologist and well-being expert", "Data scientist with a passion for AI", "Blockchain developer",
    "Web designer and passionate about art", "Content strategist and writer", "Freelance writer and environmentalist", "Digital marketer",
    "Full-stack developer and open-source enthusiast", "Sales leader with a deep passion for leadership", "VR game developer",
    "Digital nomad with a love for exploration", "AI evangelist with a focus on responsible tech", "Hiker and outdoor enthusiast", 
    "Fashion influencer and lifestyle coach", "Personal trainer with a focus on holistic health", "Astrophysicist and space exploration advocate"
]

# List of possible vibes for data retrieval
vibes = [
    "High energy, intense, curious", "Chill, thoughtful, emotionally deep", "Efficient, cold-blooded, kind of funny", "Creative, spontaneous, positive",
    "Calm, introspective, empathetic", "Optimistic, energetic, visionary", "Disciplined, logical, strategic", "Laid-back, humorous, approachable",
    "Passionate, ambitious, innovative", "Adventurous, free-spirited, fearless", "Eccentric, imaginative, quirky", "Professional, organized, focused",
    "Playful, spontaneous, social", "Analytical, precise, detail-oriented", "Gentle, considerate, caring", "Charismatic, confident, bold", 
    "Serene, balanced, peaceful", "Friendly, outgoing, welcoming", "Pragmatic, grounded, realistic", "Dynamic, ambitious, driven", "Quiet, reserved, intellectual",
    "Sophisticated, elegant, polished", "Authentic, down-to-earth, natural", "Bold, independent, confident", "Artistic, expressive, passionate"
]

# Generate and insert profiles into the database
profile_data = []

# Using for loop to generate 100 profiles
for i in range(100):
    name = random.choice(names)
    bio = random.choice(bios)
    vibe = random.choice(vibes)
    profile_data.append((name, bio, vibe))

cursor.executemany("INSERT INTO personsdata (name, bio, vibe) VALUES (?, ?, ?)", profile_data)
conn.commit()
conn.close()

print("Database and table created with 100 sample profiles.")