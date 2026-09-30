import json


def analyze_open_questions(goal, learning_style, strength):

    prompt = f"""
You are an AI learning behavior analyzer.

Analyze the student's answers below.

Learning Goal:
{goal}

Learning Style:
{learning_style}

Strength:
{strength}

Evaluate the student's learning behavior across four dimensions:

1. Individualistic
How strongly the student relies on their own abilities,
self-direction, and personal judgment.

2. Wholistic
How strongly the student benefits from people, feedback,
collaboration, and the surrounding environment.

3. Freedom
How strongly the student prefers flexibility,
experimentation, and choosing their own approach.

4. Restrictive
How strongly the student benefits from structure,
rules, clear instructions, and defined goals.

Give each dimension a score from 0 to 4.

Return JSON only in this format:

{{
    "individualistic": 0,
    "wholistic": 0,
    "freedom": 0,
    "restrictive": 0,
    "reason": "short explanation"
}}
"""

    # Temporary Mock AI
    # This will later be replaced with a real AI model.

    text = f"{goal} {learning_style} {strength}".lower()

    scores = {
        "individualistic": 0,
        "wholistic": 0,
        "freedom": 0,
        "restrictive": 0
    }

    if any(word in text for word in [
        "ตัวเอง", "ด้วยตัวเอง", "self", "independent"
    ]):
        scores["individualistic"] += 3

    if any(word in text for word in [
        "เพื่อน", "ครู", "คนอื่น", "teacher", "friends"
    ]):
        scores["wholistic"] += 3

    if any(word in text for word in [
        "ยืดหยุ่น", "ลอง", "ทดลอง", "flexible", "experiment"
    ]):
        scores["freedom"] += 3

    if any(word in text for word in [
        "ตามขั้นตอน", "ตาราง", "แผน", "step", "schedule", "plan"
    ]):
        scores["restrictive"] += 3

    return {
        "scores": scores,
        "prompt": prompt
    }