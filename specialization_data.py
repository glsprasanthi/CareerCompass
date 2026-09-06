"""Questions and names used by the specialization assessment."""

DOMAIN_NAMES = {
    "web": "Web & Application Development",
    "ai": "Data & Artificial Intelligence",
    "systems": "Systems & Infrastructure",
    "security": "Quality & Security"
}

SPECIALIZATION_NAMES = {
    "frontend": "Front-End Development",
    "backend": "Back-End Development",
    "fullstack": "Full-Stack Development",
    "data_science": "Data Science",
    "machine_learning": "Machine Learning",
    "data_engineering": "Data Engineering",
    "cloud": "Cloud Engineering",
    "devops": "DevOps Engineering",
    "embedded": "Embedded Systems",
    "qa": "QA Testing",
    "cybersecurity": "Cybersecurity"
}

SPECIALIZATION_DOMAINS = {
    "frontend": "web",
    "backend": "web",
    "fullstack": "web",
    "data_science": "ai",
    "machine_learning": "ai",
    "data_engineering": "ai",
    "cloud": "systems",
    "devops": "systems",
    "embedded": "systems",
    "qa": "security",
    "cybersecurity": "security"
}

SPECIALIZATION_QUESTIONS = {
    "web": [
        {
            "question": "Which part of a website interests you the most?",
            "options": [
                ("The visual design and user experience", "frontend"),
                ("The server, database and application logic", "backend"),
                ("How the complete website works together", "fullstack")
            ]
        },
        {
            "question": "Which task would you enjoy doing?",
            "options": [
                ("Creating responsive web pages", "frontend"),
                ("Building secure APIs", "backend"),
                ("Building a complete web application", "fullstack")
            ]
        },
        {
            "question": "What would you most like to learn?",
            "options": [
                ("HTML, CSS and JavaScript", "frontend"),
                ("Python, Flask and MySQL", "backend"),
                ("Both user interfaces and server code", "fullstack")
            ]
        },
        {
            "question": "How do you prefer to work on a project?",
            "options": [
                ("Focus closely on what users see", "frontend"),
                ("Focus closely on data and performance", "backend"),
                ("Work on different parts of the application", "fullstack")
            ]
        }
    ],
    "ai": [
        {
            "question": "Which activity sounds most interesting?",
            "options": [("Finding meaning in data", "data_science"), ("Teaching computers to make predictions", "machine_learning"), ("Organizing large amounts of data", "data_engineering")]
        },
        {
            "question": "Which result would make you proud?",
            "options": [("A useful report with insights", "data_science"), ("An accurate prediction model", "machine_learning"), ("A reliable data pipeline", "data_engineering")]
        },
        {
            "question": "Which subject would you prefer?",
            "options": [("Statistics and visualization", "data_science"), ("Algorithms and model training", "machine_learning"), ("Databases and cloud storage", "data_engineering")]
        },
        {
            "question": "What kind of problem do you enjoy?",
            "options": [("Explaining why something happened", "data_science"), ("Predicting what may happen next", "machine_learning"), ("Making data available and reliable", "data_engineering")]
        }
    ],
    "systems": [
        {
            "question": "Which system would you like to work with?",
            "options": [("Online cloud platforms", "cloud"), ("Automated software delivery", "devops"), ("Smart devices and hardware", "embedded")]
        },
        {
            "question": "Which task sounds most interesting?",
            "options": [("Designing scalable infrastructure", "cloud"), ("Automating testing and deployment", "devops"), ("Programming a small electronic device", "embedded")]
        },
        {
            "question": "What would you prefer to learn?",
            "options": [("Cloud services and networking", "cloud"), ("Linux, Git and CI/CD", "devops"), ("C programming and microcontrollers", "embedded")]
        },
        {
            "question": "Which goal matters most to you?",
            "options": [("Keeping services available at scale", "cloud"), ("Releasing software quickly and safely", "devops"), ("Making hardware perform a useful task", "embedded")]
        }
    ],
    "security": [
        {
            "question": "Which task would you rather perform?",
            "options": [("Test whether software works correctly", "qa"), ("Find and prevent security threats", "cybersecurity")]
        },
        {
            "question": "What catches your attention first?",
            "options": [("A feature that does not behave as expected", "qa"), ("A weakness that an attacker could use", "cybersecurity")]
        },
        {
            "question": "Which topic would you prefer to learn?",
            "options": [("Test cases and automation testing", "qa"), ("Networks, encryption and ethical hacking", "cybersecurity")]
        },
        {
            "question": "Which outcome feels more rewarding?",
            "options": [("Releasing a reliable, bug-free product", "qa"), ("Protecting important systems and information", "cybersecurity")]
        }
    ]
}
