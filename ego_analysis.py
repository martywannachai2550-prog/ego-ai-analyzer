def analyze_ego(scores, language="EN"):
    individual = scores["individualistic"]
    wholistic = scores["wholistic"]
    freedom = scores["freedom"]
    restrictive = scores["restrictive"]

    # -------------------------
    # 1. Orientation
    # -------------------------
    if individual > wholistic:
        orientation = "Individualistic"
        orientation_score = individual - wholistic
    else:
        orientation = "Wholistic"
        orientation_score = wholistic - individual

    # -------------------------
    # 2. Control Style
    # -------------------------
    if freedom > restrictive:
        control = "Freedom"
        control_score = freedom - restrictive
    else:
        control = "Restrictive"
        control_score = restrictive - freedom

    # -------------------------
    # 3. Combine Type
    # -------------------------
    if orientation == "Individualistic" and control == "Freedom":
        type_name = "Independent Explorer"

    elif orientation == "Individualistic" and control == "Restrictive":
        type_name = "Focused Achiever"

    elif orientation == "Wholistic" and control == "Freedom":
        type_name = "Adaptive Collaborator"

    else:
        type_name = "Structured Collaborator"

    # -------------------------
    # 4. Translation
    # -------------------------
    if language == "TH":
        orientation_text = {
            "Individualistic": "ปัจเจก",
            "Wholistic": "องค์รวม"
        }

        control_text = {
            "Freedom": "อิสระ",
            "Restrictive": "มีกรอบชัดเจน"
        }

        explanation = []

        if orientation == "Individualistic":
            explanation.append(
                f"คุณพึ่งพาความสามารถของตัวเอง ({individual}) "
                f"มากกว่าปัจจัยจากภายนอก ({wholistic})"
            )
        else:
            explanation.append(
                f"คุณใช้สภาพแวดล้อมและคนรอบตัว ({wholistic}) "
                f"มากกว่าการมุ่งเน้นที่ตัวเองเพียงอย่างเดียว ({individual})"
            )

        if control == "Freedom":
            explanation.append(
                f"คุณทำได้ดีเมื่อมีความยืดหยุ่น ({freedom}) "
                f"มากกว่าการอยู่ภายใต้โครงสร้างที่เข้มงวด ({restrictive})"
            )
        else:
            explanation.append(
                f"คุณทำได้ดีเมื่อมีโครงสร้างที่ชัดเจน ({restrictive}) "
                f"มากกว่าความยืดหยุ่น ({freedom})"
            )

        return (
            orientation_text[orientation],
            control_text[control],
            type_name,
            explanation
        )

    # -------------------------
    # English
    # -------------------------
    explanation = []

    if orientation == "Individualistic":
        explanation.append(
            f"You rely more on your own ability ({individual}) "
            f"than external input ({wholistic})."
        )
    else:
        explanation.append(
            f"You use your environment and others ({wholistic}) "
            f"more than focusing only on yourself ({individual})."
        )

    if control == "Freedom":
        explanation.append(
            f"You perform better with flexibility ({freedom}) "
            f"rather than strict structure ({restrictive})."
        )
    else:
        explanation.append(
            f"You perform better with clear structure ({restrictive}) "
            f"rather than flexibility ({freedom})."
        )

    return orientation, control, type_name, explanation