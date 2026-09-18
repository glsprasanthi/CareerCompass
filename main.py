import json
from flask import Flask, redirect, render_template, request, url_for, session, flash
from specialization_data import DOMAIN_NAMES, SPECIALIZATION_DOMAINS, SPECIALIZATION_NAMES, SPECIALIZATION_QUESTIONS
from career_data import CAREER_DETAILS
from roadmap_data import LEARNING_ROADMAPS
from resource_data import (
    SPECIALIZATION_RESOURCES,
    WEB_RESOURCE_HUB,
    AI_RESOURCE_HUB,
    SYSTEMS_RESOURCE_HUB,
    SECURITY_RESOURCE_HUB,
    YOUTUBE_CHANNELS,
    RESOURCE_COLLECTION_DOMAINS
)
from db import init_db, create_user, verify_user, save_survey_result, assign_teammate, get_domain_assignments, get_survey_results
from functools import wraps

DOMAIN_RESOURCE_HUBS = {
    "web": WEB_RESOURCE_HUB,
    "ai": AI_RESOURCE_HUB,
    "systems": SYSTEMS_RESOURCE_HUB,
    "security": SECURITY_RESOURCE_HUB
}

app = Flask(__name__)
app.secret_key = "change-this-secret"


@app.context_processor
def inject_user_status():
    return {
        "logged_in": "user_id" in session,
        "user_name": session.get("user_name"),
        "user_email": session.get("user_email")
    }


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user_id" not in session:
            return redirect(url_for("login", next=request.path))
        return f(*args, **kwargs)
    return decorated_function

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

    # Save career-discovery survey result if user logged in
    user_id = session.get("user_id")
    if user_id:
        try:
            save_survey_result(user_id, "career_discovery", {
                "percentages": percentages,
                "primary": primary_domain,
                "secondary": secondary_domain
            })
        except Exception:
            pass

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

    # Save specialization assessment result if user logged in
    user_id = session.get("user_id")
    if user_id:
        try:
            save_survey_result(user_id, "specialization_assessment", {
                "domain": domain,
                "specialization": recommended_specialization,
                "scores": specialization_scores
            })
        except Exception:
            pass

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
    domain = SPECIALIZATION_DOMAINS.get(specialization)
    if not domain and specialization in DOMAIN_RESOURCE_HUBS:
        domain = specialization

    if specialization not in SPECIALIZATION_RESOURCES and domain not in DOMAIN_RESOURCE_HUBS:
        return redirect(url_for("career_discovery"))

    resources = SPECIALIZATION_RESOURCES.get(specialization, DOMAIN_RESOURCE_HUBS.get(domain))
    hub_resources = DOMAIN_RESOURCE_HUBS.get(domain, WEB_RESOURCE_HUB)
    youtube_channels = hub_resources.get("youtube_channels", YOUTUBE_CHANNELS)

    return render_template(
        "resource_hub.html",
        specialization=specialization,
        resources=resources,
        hub_resources=hub_resources,
        youtube_channels=youtube_channels
    )


@app.route("/resource-collection", methods=["GET", "POST"])
@login_required
def resource_collection():
    user_id = session.get("user_id")
    selected_domain = None
    message = None

    if request.method == "POST":
        selected_domain = request.form.get("domain")
        teammate_name = request.form.get("teammate_name")
        notes = request.form.get("notes")
        try:
            assign_teammate(user_id, selected_domain, teammate_name, notes)
            message = f"Assigned {teammate_name} to {RESOURCE_COLLECTION_DOMAINS[selected_domain]['name']}."
        except Exception as exc:
            message = str(exc)

    domain_cards = []
    for domain_key, domain_info in RESOURCE_COLLECTION_DOMAINS.items():
        domain_cards.append({
            "domain": domain_key,
            "name": domain_info["name"],
            "description": domain_info["description"],
            "focus_areas": domain_info["focus_areas"],
            "assignments": get_domain_assignments(user_id, domain_key)
        })

    return render_template(
        "resource_collection.html",
        domain_cards=domain_cards,
        message=message,
        selected_domain=selected_domain
    )


@app.route("/profile")
@login_required
def profile():
    user_id = session["user_id"]
    results = get_survey_results(user_id)

    processed_results = []
    for row in results:
        try:
            data = json.loads(row["data"])
        except Exception:
            data = row["data"]

        processed_results.append({
            "id": row["id"],
            "survey_type": row["survey_type"],
            "data": data,
            "created_at": row["created_at"]
        })

    domain_names = {
        "web": "Web & Application Development",
        "systems": "Systems & Infrastructure",
        "ai": "Data & Artificial Intelligence",
        "security": "Quality & Security"
    }

    return render_template(
        "profile.html",
        results=processed_results,
        domain_names=domain_names,
        specialization_names=SPECIALIZATION_NAMES
    )


@app.route("/dashboard/<specialization>")
def dashboard(specialization):
    if specialization not in SPECIALIZATION_DOMAINS:
        return redirect(url_for("career_discovery"))

    domain = SPECIALIZATION_DOMAINS[specialization]
    hub_resources = DOMAIN_RESOURCE_HUBS.get(domain, WEB_RESOURCE_HUB)
    youtube_channels = hub_resources.get("youtube_channels", YOUTUBE_CHANNELS)

    return render_template(
        "dashboard.html",
        domain=domain,
        domain_name=DOMAIN_NAMES[domain],
        specialization=specialization,
        specialization_name=SPECIALIZATION_NAMES[specialization],
        career=CAREER_DETAILS[specialization],
        roadmap=LEARNING_ROADMAPS[specialization],
        resources=SPECIALIZATION_RESOURCES[specialization],
        youtube_channels=youtube_channels
    )


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")

    name = request.form.get("name", "").strip()
    email = request.form.get("email") or request.form.get("username", "")
    password = request.form.get("password", "")

    if not email or not password:
        flash("Please provide an email and password.", "error")
        return render_template("register.html"), 400

    try:
        create_user(name, email, password)
    except ValueError as e:
        flash(str(e), "error")
        return render_template("register.html"), 400

    flash("Account created successfully. Please log in.", "success")
    return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    email = request.form.get("email") or request.form.get("username", "")
    password = request.form.get("password", "")

    if not email or not password:
        flash("Please enter both email and password.", "error")
        return render_template("login.html"), 400

    user = verify_user(email, password)
    if not user:
        flash("Invalid email or password.", "error")
        return render_template("login.html"), 400

    session["user_id"] = user["id"]
    session["user_name"] = user.get("name") or user.get("username")
    session["user_email"] = user.get("email") or user.get("username")
    flash(f"Welcome back, {session['user_name']}!", "success")

    next_url = request.args.get("next")
    if next_url and next_url.startswith("/") and next_url not in ["/login", "/register", "/logout"]:
        return redirect(next_url)
    return redirect(url_for("profile"))


@app.route("/logout")
def logout():
    session.clear()
    flash("Logged out successfully.", "success")
    return redirect(url_for("home"))


@app.route("/roadmap")
def roadmap():
    return render_template("roadmap.html")


@app.route("/resources")
def resources():
    return render_template("resources.html")


if __name__ == "__main__":
    app.run(debug=True)
