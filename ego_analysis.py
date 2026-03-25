def analyze_ego(scores):
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
    # 4. Explanation
    # -------------------------
    explanation = []

    if orientation == "Individualistic":
        explanation.append(f"You rely more on your own ability ({individual}) than external input ({wholistic}).")
    else:
        explanation.append(f"You use your environment and others ({wholistic}) more than focusing only on yourself ({individual}).")

    if control == "Freedom":
        explanation.append(f"You perform better with flexibility ({freedom}) rather than strict structure ({restrictive}).")
    else:
        explanation.append(f"You perform better with clear structure ({restrictive}) rather than flexibility ({freedom}).")

    return orientation, control, type_name, explanation