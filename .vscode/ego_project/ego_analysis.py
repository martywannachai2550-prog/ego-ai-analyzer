def analyze_ego(scores):

    self_score = scores["self"]
    wholistic_score = scores["wholistic"]
    freedom_score = scores["freedom"]
    restrictive_score = scores["restrictive"]

    if self_score > wholistic_score:
        orientation = "Self"
    else:
        orientation = "Wholistic"

    if freedom_score > restrictive_score:
        control = "Freedom"
    else:
        control = "Restrictive"

    ego_type = orientation + " " + control

    if ego_type == "Self Freedom":
        type_name = "Instinct Striker"

    elif ego_type == "Self Restrictive":
        type_name = "Calculated Egoist"

    elif ego_type == "Wholistic Freedom":
        type_name = "Creative Playmaker"

    else:
        type_name = "Strategic Architect"

    return orientation, control, type_name