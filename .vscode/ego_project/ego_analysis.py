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
        type_name = "Independent Learner"

    elif ego_type == "Individualistic Restrictive":
        type_name = "Structured Individual"

    elif ego_type == "Wholistic Freedom":
        type_name = "Collaborative Explorer"

    else:
        type_name = "Systematic Collaborator"

    return orientation, control, type_name

