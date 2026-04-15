import streamlit as st
import json
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from ego_analysis import analyze_ego
from learning_plan import generate_plan

pquestion = [
    {
        "EN": (
            "1.)When working on a difficult assignment",
            [
                "I can choose my own way to complete tasks",
                "I have clear instructions to follow"
            ]
        ),
        "TH": (
            "1.)เมื่อต้องทำงานที่มีความยากลำบาก",
            [
                "ฉันสามารถเลือกวิธีการทำงานในแบบของฉันเอง",
                "ฉันมักทำตามคำแนะนำที่มีความชัดเจน"
            ]
        ),
        "score": ["individualistic", "wholistic"]
    },

    {
        "EN": (
            "2.)When learning something new",
            [
                "I rely on my own thinking and interpretation",
                "I rely on examples, teachers, or peers"
            ]
        ),
        "TH": (
            "2.)เมื่อต้องเรียนรู้สิ่งใหม่ๆ",
            [
                "ฉันมักจะพึ่งพาความคิดและความสามารถของตัวเอง",
                "ฉันเรียนรู้ผ่านตัวอย่างที่คุณครูสอนหรือของเพื่อน"
            ]
        ),
        "score": ["individualistic", "wholistic"]
    },

    {
        "EN": (
            "3.)In group work",
            [
                "I focus on my own part and performance",
                "I focus on how the group performs as a whole"
            ]
        ),
        "TH": (
            "3.)การทำงานกลุ่ม",
            [
                "ฉันโฟกัสไปที่ส่วนของฉันและผลงานของฉันเอง",
                "ฉันให้ความสำคัญกับผลการปฎิบัติการโดยรวมของเพื่อนร่วมงานภายในกลุ่ม"
            ]
        ),
        "score": ["individualistic", "wholistic"]
    },

    {
        "EN": (
            "4.)When facing a problem",
            [
                "I adapt based on the situation and people around me",
                "I trust my own method"
            ]
        ),
        "TH": (
            "4.)เมื่อเผชิญหน้ากับปัญหา",
            [
                "ฉันจะปรับตัวไปตามสถานการณ์และผู้คนรอบๆตัว",
                "ฉันเชื่อมั่นในความสามารถของฉันเอง"
            ]
        ),
        "score": ["wholistic", "individualistic"]
    },

    {
        "EN": (
            "5.)When receiving feedback",
            [
                "I actively adjust based on feedback",
                "I evaluate it but rely mostly on my own judgment"
            ]
        ),
        "TH": (
            "5.)เมื่อได้รับคำติชม",
            [
                "ฉันเปิดรับและปรับปรุงตามคำติชมอย่างต่อเนื่อง",
                "ฉันเปิดรับคำติชมแต่ส่วนใหญ่จะอาศัยการตัดสินใจของตนเอง"
            ]
        ),
        "score": ["wholistic", "individualistic"]
    },

    {
        "EN": (
            "6.)In class",
            [
                "I prefer working independently",
                "I learn better through interaction"
            ]
        ),
        "TH": (
            "6.)ขณะอยู่ในชั้นเรียน",
            [
                "ฉันชอบการทำงานเดี่ยว",
                "ฉันเรียนรู้ได้ดีจากการมีปฏิสัมพันธ์กับเพื่อนร่วมห้อง"
            ]
        ),
        "score": ["individualistic", "wholistic"]
    }
]

text = {
    "EN": {
        "title": "AI Self Development Analyzer",
        "name": "👤 Please enter your name to begin",
        "personality": "--Personality & Character Types--",
        "mindset": "--Mindset Types--",
        "rate": "--Rate Yourself (1-5)--",
        "open": "--Open Questions--",
        "analyze": "Analyze",
        "warning_name": "Please enter your name",
        "warning_q": "Please answer all questions",
        "result": "Result",
        "ego": "Ego Orientation",
        "control": "Control Style",
        "type": "Ego Type",
        "why": "Why this result?",
        "strategy": "Learning Strategy",
        "about": "About Your Ego",
        "plan": "Suggested Study Plan"
    },

    "TH": {
        "title": "ระบบวิเคราะห์การพัฒนาตนเอง",
        "name": "👤 กรุณากรอกชื่อของคุณ",
        "personality": "--ลักษณะนิสัยและพฤติกรรม--",
        "mindset": "--รูปแบบการเรียนรู้--",
        "rate": "--ให้คะแนนตัวเอง (1-5)--",
        "open": "--คำถามเพิ่มเติม--",
        "analyze": "วิเคราะห์",
        "warning_name": "กรุณากรอกชื่อ",
        "warning_q": "กรุณาตอบคำถามให้ครบ",
        "result": "ผลลัพธ์",
        "ego": "ลักษณะการเรียนรู้",
        "control": "รูปแบบการควบคุม",
        "type": "ประเภทของคุณ",
        "why": "เหตุผลของผลลัพธ์",
        "strategy": "กลยุทธ์การเรียน",
        "about": "เกี่ยวกับตัวคุณ",
        "plan": "แผนการเรียนที่แนะนำ"
    }
}

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

col1, col2 = st.columns([6,1])

with col2:
    language = st.selectbox("",["EN", "TH"])

st.title(text[language]["title"])
name = st.text_input(text[language]["name"])

st.header(text[language]["personality"])
pc_answers = []

for i, q in enumerate(pquestion):
    question, options = q[language]

    ans = st.radio(f"{i+1}. {question}", options, index=None)

    pc_answers.append((ans, q))

for ans, q in pc_answers:
    if ans is not None:
        index = q[language][1].index(ans)

        if q["score"][index] == "individualistic":
            individualistic += 2
        else:
            wholistic += 2

st.header(text[language]["mindset"])
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

st.header(text[language]["rate"])
logic = st.slider("Logical Thinking",1,5)
creativity = st.slider("Creativity",1,5)
competition = st.slider("Competitiveness",1,5)
system_thinking = st.slider("System Thinking",1,5)

st.header(text[language]["open"])

goal = st.text_input("What skill do you want to master?")
learning_style = st.text_area("How do you usually learn?")
strength = st.text_area("Your biggest strength")

if st.button(text[language]["analyze"]):
    if not name:
        st.warning(text[language]["warning_name"])
    else:
        all_answers = [PC1, PC2, PC3, PC4, PC5, PC6, M1, M2, M3, M4, M5, M6]
        if None in all_answers:
            st.warning(text[language]["warning_q"])
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

        st.header(text[language]["result"])

        st.write(text[language]["ego"] + ":", orientation)
        st.write(text[language]["control"] + ":", control)
        st.write(text[language]["type"] + ":", type_name)

        st.subheader(text[language]["why"])
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

        st.subheader(text[language]["strategy"])

        st.write(strategy)

        st.subheader(text[language]["about"])

        info = ego_description[language][type_name]

        st.write("Description:", info["desc"])
        st.write("Strength:", info["strength"])
        st.write("Weakness:", info["weakness"])

        st.subheader(text[language]["plan"])

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
            with open("data/users.json", "w", encoding="utf-8") as f:
                json.dump(users, f, indent=4, ensure_ascii=False)
        except:
            users = []

        st.caption("Privacy Notice: Your data is stored locally and will not be shared. Results are for personal use only.")