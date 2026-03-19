import streamlit as st
import json
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from ego_analysis import analyze_ego
from learning_plan import generate_plan

def plot_radar(logic, creativity, competition, system):

    labels = ["Logic", "Creativity", "Competition", "System"]
    values = [logic, creativity, competition, system]

    values += values[:1]  # ปิดกราฟ

    angles = np.linspace(0, 2*np.pi, len(labels), endpoint=False)
    angles = np.concatenate((angles, [angles[0]]))

    fig = plt.figure()
    ax = fig.add_subplot(111, polar=True)

    ax.plot(angles, values)
    ax.fill(angles, values, alpha=0.2)

    ax.set_thetagrids(angles[:-1] * 180/np.pi, labels)

    return fig

ego_description = {
    "Instinct Striker": {
        "desc": "You rely on instinct and freedom to grow.",
        "strength": "Fast learner, fearless, competitive",
        "weakness": "May lack structure, inconsistent"
    },

    "Calculated Egoist": {
        "desc": "You grow through discipline and structured strategy.",
        "strength": "Consistent, analytical, focused",
        "weakness": "May become rigid, slow to adapt"
    },

    "Creative Playmaker": {
        "desc": "You connect ideas and innovate.",
        "strength": "Creative, adaptive, visionary",
        "weakness": "May lack execution consistency"
    },

    "Strategic Architect": {
        "desc": "You understand systems deeply.",
        "strength": "Strategic, deep thinker",
        "weakness": "Overthinking, slow action"
    }
}

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
        "individualistic": logic + competition,
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

st.subheader("Skill Radar")

fig = plot_radar(logic, creativity, competition, system_thinking)
st.pyplot(fig)

st.subheader("About Your Ego")

info = ego_description[type_name]

st.write("Description:", info["desc"])
st.write("Strength:", info["strength"])
st.write("Weakness:", info["weakness"])

st.header("User Dashboard")

with open("data/users.json","r") as f:
    users = json.load(f)

if users:
    df = pd.DataFrame(users)

    st.subheader("All Users")
    st.dataframe(df)

    st.subheader("Ego Type Distribution")
    st.bar_chart(df["ego_type"].value_counts())
else:
    st.write("No data yet")