# Import necessary libraries for frontend ui
import streamlit as st
import requests

# Function to fetch profiles from backend API
def fetch_profiles_from_backendapi(query=""):
    try:
        response = requests.post("http://localhost:8000/search", json={"query": query})
        response.raise_for_status()
        return response.json().get('matches', [])
    except requests.exceptions.RequestException as e:
        st.error(f"Error connecting to backend: {e}")
        return []

# Streamlit ui page setup for interaction
st.set_page_config(page_title="AIFindr Application", layout="centered")

# UI title
st.title("AIFindr - AI Powered Profile Match Application")
st.markdown("You can give the query to match the person with your vibes, interests and goals")

# Input query
query = st.text_input("### Describe your match preferences:", placeholder="e.g. hardcore minimalists building in crypto")
search = st.button("Search")

# Results when interact with ui
if search and query:
    st.info("Wait for results, searching for top matches.")
    profiles = fetch_profiles_from_backendapi(query)

    if profiles:
        st.success(f"Top {len(profiles)} Match{'es' if len(profiles) > 1 else ''}:")
        for person in profiles:
            name = person.get('name', "No name provided")
            bio = person.get('bio', "No bio available")
            vibe = person.get('vibe', "No vibe info")
            reason = person.get('reason', None)

            with st.container():
                st.subheader(name)
                st.markdown(f"- **Bio:** {bio}")
                st.markdown(f"- **Vibe:** {vibe}")
                if reason:
                    st.markdown(f"**Why is this match good:** {reason}")
                st.markdown("---")
    else:
        st.warning("There are no profiles matched your query. Try rephrasing or changing the vibe.")
else:
    st.caption("Start typing a natural language human-like query above to discover people.")