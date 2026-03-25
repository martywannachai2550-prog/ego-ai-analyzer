import streamlit as st
import json
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from ego_analysis import analyze_ego
from learning_plan import generate_plan

individualistic = 0
wholistic = 0
freedom = 0
restrictive = 0

def plot_ego_matrix(scores):

    x = scores["individualistic"] - scores["wholistic"]
    y = scores["freedom"] - scores["restrictive"]

    fig, ax = plt.subplots()

    ax.axhline(0)
    ax.axvline(0)

    ax.scatter(x, y, color="red", s=120)
    ax.grid(True)

    ax.text(x, y, "You", fontsize=12)

    ax.set_xlabel("← Wholistic | Individualistic →")
    ax.set_ylabel("↓ Restrictive | Freedom ↑")

    ax.set_xlim(-20, 20)
    ax.set_ylim(-20, 20)

    return fig

ego_description = {
    "Independent Explorer": {
        "desc": "You learn best through self-direction and flexibility.",
        "strength": "Independent, creative, adaptable",
        "weakness": "May lack consistency and structure"
    },

    "Focused Achiever": {
        "desc": "You rely on discipline and clear goals to succeed.",
        "strength": "Focused, consistent, goal-oriented",
        "weakness": "May become rigid under pressure"
    },

    "Adaptive Collaborator": {
        "desc": "You learn effectively by interacting with others and adapting.",
        "strength": "Collaborative, flexible, aware",
        "weakness": "May lack clear personal direction"
    },

    "Structured Collaborator": {
        "desc": "You thrive in structured environments with teamwork.",
        "strength": "Organized, reliable, team-oriented",
        "weakness": "May depend too much on structure"
    }
}

st.title("AI Self Development Analyzer")

name = st.text_input("Your Name")

st.header("Personality & Character Types")
PC1 = st.radio("When working on a difficult assignment",
               ['I prefer discussing with others to understand it',
                'I prefer solving it on my own first'],
                index = None)

PC2 = st.radio("When learning something new",
               ['I rely on my own thinking and interpretation',
                'I rely on examples, teachers, or peers'],
                index = None)

PC3 = st.radio("In group work",
               ['I focus on my own part and performance',
                'I focus on how the group performs as a whole'],
                index = None)

PC4 = st.radio("When facing a problem",
               ['I adapt based on the situation and people around me',
                'I trust my own method'],
                index = None)

PC5 = st.radio("When receiving feedback",
               ['I actively adjust based on feedback',
                'I evaluate it but rely mostly on my own judgment'],
                index = None)

PC6 = st.radio("In class",
               ['I prefer working independently',
                'I learn better through interaction'],
                index = None)

if PC1 == 'I prefer solving it on my own first':
    individualistic += 2
elif PC1 == 'I prefer discussing with others to understand it':
    wholistic += 2

if PC2 == 'I rely on my own thinking and interpretation':
    individualistic += 2
elif PC2 == 'I rely on examples, teachers, or peers':
    wholistic += 2

if PC3 == 'I focus on my own part and performance':
    individualistic += 2
elif PC3 == 'I focus on how the group performs as a whole':
    wholistic += 2

if PC4 == 'I trust my own method':
    individualistic += 2
elif PC4 == 'I adapt based on the situation and people around me':
    wholistic += 2

if PC5 == 'I evaluate it but rely mostly on my own judgment':
    individualistic += 2
elif PC5 == 'I actively adjust based on feedback':
    wholistic += 2

if PC6 == 'I prefer working independently':
    individualistic += 2
elif PC6 == 'I learn better through interaction':
    wholistic += 2

st.header("Mindset Types")
M1 = st.radio("I perform best when",
              ['I can choose my own way to complete tasks',
               'I have clear instructions to follow'],
               index = None)

M2 = st.radio("When doing assignments",
              ['I prefer structured tasks with clear steps',
               'I prefer open-ended tasks'],index = None)

M3 = st.radio("My study style is",
              ['Flexible and adaptable',
               'Planned and consistent'],
               index = None)

M4 = st.radio("When solving problems",
              ['I follow a step-by-step method',
               'I try different approaches freely'],
               index = None)

M5 = st.radio("In deadlines",
              ['I stick strictly to a schedule',
               'I adjust my pace based on situation'],
               index = None)

M6 = st.radio("In learning environments",
              ['I feel comfortable with freedom',
               'I feel comfortable with clear rules'],
               index = None)

if M1 == 'I can choose my own way to complete tasks':
    freedom += 2
elif M1 == 'I have clear instructions to follow':
    restrictive += 2

if M2 == 'I prefer open-ended tasks':
    freedom += 2
elif M2 == 'I prefer structured tasks with clear steps':
    restrictive += 2

if M3 == 'Flexible and adaptable':
    freedom += 2
elif M3 == 'Planned and consistent':
    restrictive += 2

if M4 == 'I try different approaches freely':
    freedom += 2
elif M4 == 'I follow a step-by-step method':
    restrictive += 2

if M5 == 'I adjust my pace based on situation':
    freedom += 2
elif M5 == 'I stick strictly to a schedule':
    restrictive += 2

if M6 == 'I feel comfortable with freedom':
    freedom += 2
elif M6 == 'I feel comfortable with clear rules':
    restrictive += 2

st.header("Rate Yourself (1-5)")
logic = st.slider("Logical Thinking",1,5)
creativity = st.slider("Creativity",1,5)
competition = st.slider("Competitiveness",1,5)
system_thinking = st.slider("System Thinking",1,5)

st.header("Open Questions")

goal = st.text_input("What skill do you want to master?")
learning_style = st.text_area("How do you usually learn?")
strength = st.text_area("Your biggest strength")

if st.button("Analyze"):
    if not name:
        st.warning("Please enter your name")
    else:
        all_answers = [PC1, PC2, PC3, PC4, PC5, PC6, M1, M2, M3, M4, M5, M6]
        if None in all_answers:
            st.warning("Please answer all questions")
            st.stop()
            
        scores = {
            "individualistic": individualistic + logic + competition,
            "wholistic": wholistic + system_thinking,
            "freedom": freedom + creativity,
            "restrictive": restrictive + logic
        }

        fig = plot_ego_matrix(scores)
        st.subheader("Ego Matrix")
        st.pyplot(fig)

        orientation, control, type_name, explanation = analyze_ego(scores)

        strategy, schedule = generate_plan(type_name)

        st.header("Result")

        st.write("Ego Orientation:", orientation)
        st.write("Control Style:", control)
        st.write("Ego Type:", type_name)

        st.subheader("Why this result?")
        for e in explanation:
            st.write("- " + e)

        confidence = abs(scores["individualistic"] - scores["wholistic"]) + \
             abs(scores["freedom"] - scores["restrictive"])
        if confidence >= 15:
            level = "High"
        elif confidence >= 8:
            level = "Moderate"
        else:
            level = "Low"
        st.write(f"Confidence Level: {level} ({confidence})")

        st.subheader("Learning Strategy")

        st.write(strategy)

        st.subheader("About Your Ego")

        info = ego_description[type_name]

        st.write("Description:", info["desc"])
        st.write("Strength:", info["strength"])
        st.write("Weakness:", info["weakness"])

        st.subheader("Suggested Study Plan")

        for i, s in enumerate(schedule):
            st.write(f"Day {i+1} - {s}")

        data = {
            "name": name,
            "goal": goal,
            "strength": strength,
            "ego_type": type_name
        }
        try:
            with open("data/users.json","r") as f:
                users = json.load(f)
        except:
            users = []

        users.append(data)

        try:
            with open("data/users.json","w") as f:
                json.dump(users,f,indent=4)
        except:
            users = []

        st.caption("Privacy Notice: Your data is stored locally and will not be shared. Results are for personal use only.")