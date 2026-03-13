import streamlit as st
import json

from ego_analysis import analyze_ego
from learning_plan import generate_plan


st.title("AI Self Development Analyzer")


name = st.text_input("Your Name")

st.header("Rate Yourself (1-10)")

logic = st.slider("Logical Thinking",1,10)
creativity = st.slider("Creativity",1,10)
competition = st.slider("Competitiveness",1,10)
system_thinking = st.slider("System Thinking",1,10)

st.header("Open Questions")

goal = st.text_input("What skill do you want to master?")
learning_style = st.text_area("How do you usually learn?")
strength = st.text_area("Your biggest strength")

if st.button("Analyze"):

    scores = {
        "self": logic + competition,
        "wholistic": system_thinking,
        "freedom": creativity,
        "restrictive": logic
    }

    orientation, control, type_name = analyze_ego(scores)

    strategy, schedule = generate_plan(type_name)

    st.header("Result")

    st.write("Ego Orientation:", orientation)
    st.write("Control Style:", control)
    st.write("Ego Type:", type_name)

    st.subheader("Learning Strategy")

    st.write(strategy)

    st.subheader("Suggested Study Plan")

    for i, s in enumerate(schedule):
        st.write(f"Day {i+1} - {s}")

    data = {
        "name": name,
        "goal": goal,
        "strength": strength,
        "ego_type": type_name
    }

    with open("data/users.json","r") as f:
        users = json.load(f)

    users.append(data)

    with open("data/users.json","w") as f:
        json.dump(users,f,indent=4)

    st.success("User data saved")