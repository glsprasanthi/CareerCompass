from flask import Flask, redirect, render_template, request, url_for
from specialization_data import DOMAIN_NAMES, SPECIALIZATION_DOMAINS, SPECIALIZATION_NAMES, SPECIALIZATION_QUESTIONS
from career_data import CAREER_DETAILS
from roadmap_data import LEARNING_ROADMAPS
from resource_data import SPECIALIZATION_RESOURCES, WEB_RESOURCE_HUB, YOUTUBE_CHANNELS

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/career-discovery")
def career_discovery():
    return render_template("career_discovery.html")


@app.route("/career-explorer", methods=["GET", "POST"])
def career_explorer():
    if request.method == "GET":
        return redirect(url_for("career_discovery"))

    scores = {
        "web": 0,
        "systems": 0,
        "ai": 0,
        "security": 0
    }

    answers = [
        request.form.get("q1"),
        request.form.get("q2"),
        request.form.get("q3"),
        request.form.get("q4"),
        request.form.get("q5"),
        request.form.get("q6")
    ]

    if any(answer not in scores for answer in answers):
        return render_template(
            "career_discovery.html",
            error="Please answer all six questions before viewing your result."
        ), 400

    for answer in answers:
        if answer in scores:
            scores[answer] += 1

    total = sum(scores.values())

    percentages = {
        domain: round((score / total) * 100)
        for domain, score in scores.items()
    }

    sorted_domains = sorted(
        percentages.items(),
        key=lambda x: x[1],
        reverse=True
    )

    primary_domain = sorted_domains[0][0]
    primary_score = sorted_domains[0][1]

    secondary_domain = sorted_domains[1][0]
    secondary_score = sorted_domains[1][1]

    is_tie = primary_score == secondary_score

    domain_names = {
        "web": "Web & Application Development",
        "systems": "Systems & Infrastructure",
        "ai": "Data & Artificial Intelligence",
        "security": "Quality & Security"
    }

    return render_template(
        "career_explorer.html",
        domain=primary_domain,
        primary_score=primary_score,
        secondary_domain=secondary_domain,
        secondary_score=secondary_score,
        domain_names=domain_names,
        is_tie=is_tie
    )


@app.route("/specialization-assessment/<domain>")
def specialization_assessment(domain):
    if domain not in SPECIALIZATION_QUESTIONS:
        return redirect(url_for("career_discovery"))

    questions = SPECIALIZATION_QUESTIONS[domain]
    return render_template(
        "specialization_assessment.html",
        domain=domain,
        domain_name=DOMAIN_NAMES[domain],
        questions=questions
    )


@app.route("/specialization-result", methods=["POST"])
def specialization_result():
    domain = request.form.get("domain")

    if domain not in SPECIALIZATION_QUESTIONS:
        return redirect(url_for("career_discovery"))

    questions = SPECIALIZATION_QUESTIONS[domain]
    valid_specializations = []

    for question in questions:
        for option_text, specialization in question["options"]:
            if specialization not in valid_specializations:
                valid_specializations.append(specialization)

    specialization_scores = {}
    for specialization in valid_specializations:
        specialization_scores[specialization] = 0

    for question_number in range(1, len(questions) + 1):
        answer = request.form.get("question" + str(question_number))
        if answer not in valid_specializations:
            return render_template(
                "specialization_assessment.html",
                domain=domain,
                domain_name=DOMAIN_NAMES[domain],
                questions=questions,
                error="Please answer every question."
            ), 400
        specialization_scores[answer] += 1

    recommended_specialization = max(
        specialization_scores,
        key=specialization_scores.get
    )

    return render_template(
        "specialization_result.html",
        domain=domain,
        domain_name=DOMAIN_NAMES[domain],
        specialization=recommended_specialization,
        specialization_name=SPECIALIZATION_NAMES[recommended_specialization]
    )


@app.route("/career-details/<domain>/<specialization>")
def career_details(domain, specialization):
    if domain not in SPECIALIZATION_QUESTIONS:
        return redirect(url_for("career_discovery"))

    valid_specializations = []
    for question in SPECIALIZATION_QUESTIONS[domain]:
        for option_text, option_value in question["options"]:
            if option_value not in valid_specializations:
                valid_specializations.append(option_value)

    if specialization not in valid_specializations:
        return redirect(url_for("career_discovery"))

    return render_template(
        "career_details.html",
        domain_name=DOMAIN_NAMES[domain],
        specialization=specialization,
        career=CAREER_DETAILS[specialization]
    )


@app.route("/learning-roadmap/<specialization>")
def learning_roadmap(specialization):
    if specialization not in LEARNING_ROADMAPS:
        return redirect(url_for("career_discovery"))

    roadmap = LEARNING_ROADMAPS[specialization]
    return render_template(
        "learning_roadmap.html",
        specialization=specialization,
        roadmap=roadmap
    )


@app.route("/resource-hub/<specialization>")
def resource_hub(specialization):
    if specialization not in SPECIALIZATION_RESOURCES:
        return redirect(url_for("career_discovery"))

    resources = SPECIALIZATION_RESOURCES[specialization]
    hub_resources = resources

    if specialization in ["frontend", "backend", "fullstack"]:
        hub_resources = WEB_RESOURCE_HUB

    return render_template(
        "resource_hub.html",
        specialization=specialization,
        resources=resources,
        hub_resources=hub_resources,
        youtube_channels=YOUTUBE_CHANNELS
    )


@app.route("/dashboard/<specialization>")
def dashboard(specialization):
    if specialization not in SPECIALIZATION_DOMAINS:
        return redirect(url_for("career_discovery"))

    domain = SPECIALIZATION_DOMAINS[specialization]

    return render_template(
        "dashboard.html",
        domain=domain,
        domain_name=DOMAIN_NAMES[domain],
        specialization=specialization,
        specialization_name=SPECIALIZATION_NAMES[specialization],
        career=CAREER_DETAILS[specialization],
        roadmap=LEARNING_ROADMAPS[specialization],
        resources=SPECIALIZATION_RESOURCES[specialization],
        youtube_channels=YOUTUBE_CHANNELS
    )


@app.route("/roadmap")
def roadmap():
    return render_template("roadmap.html")


@app.route("/resources")
def resources():
    return render_template("resources.html")


if __name__ == "__main__":
    app.run(debug=True)
