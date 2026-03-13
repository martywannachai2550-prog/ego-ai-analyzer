def generate_plan(type_name):

    if type_name == "Instinct Striker":

        strategy = "Project based learning"

        schedule = [
            "Watch tutorial",
            "Build mini project",
            "Solve challenge problem",
            "Improve your project",
            "Publish your work"
        ]

    elif type_name == "Calculated Egoist":

        strategy = "Structured training"

        schedule = [
            "Study theory",
            "Take notes",
            "Practice exercises",
            "Solve advanced problems",
            "Take a mini test"
        ]

    elif type_name == "Creative Playmaker":

        strategy = "Exploratory learning"

        schedule = [
            "Explore new concept",
            "Connect ideas",
            "Create something original",
            "Experiment with variation",
            "Share your idea"
        ]

    else:

        strategy = "Deep analytical learning"

        schedule = [
            "Deep theory study",
            "Analyze system",
            "Read case studies",
            "Apply to project",
            "Evaluate results"
        ]

    return strategy, schedule