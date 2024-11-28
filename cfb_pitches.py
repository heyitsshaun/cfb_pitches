import streamlit as st

# Define motivations and pitches
motivations = [
    "Academic Prestige",
    "Athletic Facilities",
    "Brand Exposure",
    "Campus Lifestyle",
    "Championship Contender",
    "Coach Stability",
    "Coach Prestige",
    "Conference Prestige",
    "Playing Time",
    "Pro Potential",
    "Playing Style",
    "Proximity to Home",
    "Program Tradition",
    "Stadium Atmosphere",
]

pitches = {
    "College Experience (1-1)": ["Academic Prestige", "Campus Lifestyle", "Stadium Atmosphere"],
    "Team Player (1-2)": ["Athletic Facilities", "Coach Stability", "Proximity to Home"],
    "Campus Personality (1-3)": ["Academic Prestige", "Campus Lifestyle", "Proximity to Home"],
    "It's Game Time (1-4)": ["Conference Prestige", "Playing Style", "Proximity to Home"],
    "Prestigious (1-5)": ["Coach Prestige", "Conference Prestige", "Proximity to Home"],
    "Student of the Game (2-1)": ["Academic Prestige", "Coach Prestige", "Proximity to Home"],
    "Hometown Hero (2-2)": ["Campus Lifestyle", "Proximity to Home", "Program Tradition"],
    "Prove Yourself (2-3)": ["Athletic Facilities", "Coach Prestige", "Conference Prestige"],
    "The Clutch (2-4)": ["Pro Potential", "Playing Style", "Proximity to Home"],
    "TV Time (2-5)": ["Brand Exposure", "Championship Contender", "Playing Time"],
    "Coach's Favorite (3-1)": ["Athletic Facilities", "Coach Prestige", "Proximity to Home"],
    "Aspirational (3-2)": ["Athletic Facilities", "Championship Contender", "Proximity to Home"],
    "To The House (3-3)": ["Brand Exposure", "Championship Contender", "Coach Prestige"],
    "Football Influencer (3-4)": ["Championship Contender", "Pro Potential", "Program Tradition"],
    "Time To Get To Work (3-5)": ["Playing Time", "Playing Style", "Proximity to Home"],
    "Starter (4-1)": ["Brand Exposure", "Playing Time", "Pro Potential"],
    "Grassroots (4-2)": ["Pro Potential", "Proximity to Home", "Program Tradition"],
    "Conference Spotlight (4-3)": ["Championship Contender", "Conference Prestige", "Proximity to Home"],
    "Sunday Bound (4-4)": ["Championship Contender", "Conference Prestige", "Pro Potential"],
    "Work Horse (4-5)": ["Athletic Facilities", "Brand Exposure", "Pro Potential"],
}

# Streamlit Web App
st.title("Motivation and Pitch Finder")

st.header("Set Motivation Status")
motivation_status = {}

# Create toggles for each motivation
for motivation in motivations:
    col1, col2 = st.columns([3, 1])
    with col1:
        st.write(motivation)
    with col2:
        status = st.radio(
            label="",
            options=["❌", "❔", "✔️"],
            index=1,
            key=motivation,
            horizontal=True,
        )
        if status == "❔":
            motivation_status[motivation] = 0
        elif status == "✔️":
            motivation_status[motivation] = 1
        else:
            motivation_status[motivation] = -1

# Function to find applicable pitches
def find_applicable_pitches(motivation_status):
    applicable_pitches = []

    for pitch, pitch_motivations in pitches.items():
        match = True
        for motivation in pitch_motivations:
            if motivation_status[motivation] == -1:  # Not a motivation
                match = False
                break
        if match:
            applicable_pitches.append(pitch)

    return applicable_pitches

# Submit button to display applicable pitches
if st.button("Submit"):
    applicable_pitches = find_applicable_pitches(motivation_status)
    
    st.header("Applicable Pitches")
    if applicable_pitches:
        for pitch in applicable_pitches:
            st.write(f"- {pitch}")
    else:
        st.write("No applicable pitches based on the current motivation statuses.")
