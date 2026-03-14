def analyze_ego(scores):

    individualistic_score = scores["individualistic"]
    wholistic_score = scores["wholistic"]
    freedom_score = scores["freedom"]
    restrictive_score = scores["restrictive"]

    if individualistic_score > wholistic_score:
        orientation = "Individualistic"
    else:
        orientation = "Wholistic"

    if freedom_score > restrictive_score:
        control = "Freedom"
    else:
        control = "Restrictive"

    ego_type = orientation + " " + control

    if ego_type == "Individualistic Freedom":
        type_name = "Instinct Striker"

    elif ego_type == "Individualistic Restrictive":
        type_name = "Calculated Egoist"

    elif ego_type == "Wholistic Freedom":
        type_name = "Creative Playmaker"

    else:
        type_name = "Strategic Architect"

    return orientation, control, type_name