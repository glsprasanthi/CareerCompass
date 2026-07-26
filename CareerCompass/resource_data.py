"""Categorized learning resources for the Resource Hub."""

WEB_RESOURCE_HUB = {
    "name": "Web & Application Development",
    "youtube_channels": [
        {"name": "freeCodeCamp.org", "url": "https://www.youtube.com/@freecodecamp", "description": "Complete beginner-friendly courses for front-end and back-end development."},
        {"name": "Traversy Media", "url": "https://www.youtube.com/@TraversyMedia", "description": "Clear crash courses and practical projects from Brad Traversy."},
        {"name": "The Net Ninja", "url": "https://www.youtube.com/@NetNinja", "description": "Well-organized playlists that students can follow lesson by lesson."},
        {"name": "Kevin Powell", "url": "https://www.youtube.com/@KevinPowell", "description": "Beginner-friendly explanations of CSS and responsive design."},
        {"name": "Web Dev Simplified", "url": "https://www.youtube.com/@WebDevSimplified", "description": "Focused explanations of JavaScript and web-development concepts."},
        {"name": "Fireship", "url": "https://www.youtube.com/@Fireship", "description": "Short introductions to modern tools after learning the fundamentals."},
        {"name": "CS50", "url": "https://www.youtube.com/@cs50", "description": "University-quality computer-science and web-programming lectures."}
    ],
    "documentation": [
        {"name": "MDN Learn Web Development", "url": "https://developer.mozilla.org/en-US/docs/Learn_web_development", "description": "Structured lessons for HTML, CSS, JavaScript and accessibility."},
        {"name": "MDN JavaScript Guide", "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide", "description": "A trusted reference for JavaScript fundamentals."},
        {"name": "Python Tutorial", "url": "https://docs.python.org/3/tutorial/", "description": "The official starting point for Python back-end development."},
        {"name": "Flask Tutorial", "url": "https://flask.palletsprojects.com/en/stable/tutorial/", "description": "Learn routes, templates and databases through a small application."},
        {"name": "MySQL Tutorial", "url": "https://dev.mysql.com/doc/refman/8.4/en/tutorial.html", "description": "Introduces tables, queries and common database operations."}
    ],
    "free_courses": [
        {"name": "freeCodeCamp Responsive Web Design", "url": "https://www.freecodecamp.org/learn/2022/responsive-web-design/", "description": "Learn HTML and CSS through exercises and projects."},
        {"name": "The Odin Project Foundations", "url": "https://www.theodinproject.com/paths/foundations/courses/foundations", "description": "A structured path covering HTML, CSS, JavaScript and Git."},
        {"name": "Meta Introduction to Front-End Development", "url": "https://www.coursera.org/learn/introduction-to-front-end-development/", "description": "A beginner Coursera course that can generally be audited for free."},
        {"name": "CS50 Web Programming", "url": "https://cs50.harvard.edu/web/", "description": "Free material covering Python, JavaScript, SQL and security."},
        {"name": "The Odin Project Full Stack JavaScript", "url": "https://www.theodinproject.com/paths/full-stack-javascript", "description": "A project-based route through JavaScript, React and Node.js."}
    ],
    "practice": [
        {"name": "Frontend Mentor", "url": "https://www.frontendmentor.io/challenges", "description": "Recreate realistic designs using HTML, CSS and JavaScript."},
        {"name": "freeCodeCamp", "url": "https://www.freecodecamp.org/learn/", "description": "Complete coding exercises and certification projects."},
        {"name": "Exercism JavaScript", "url": "https://exercism.org/tracks/javascript", "description": "Free exercises with automated feedback and mentoring."},
        {"name": "Codewars JavaScript", "url": "https://www.codewars.com/kata/search/javascript", "description": "Solve ranked exercises and compare community solutions."},
        {"name": "HackerRank JavaScript", "url": "https://www.hackerrank.com/domains/tutorials/10-days-of-javascript", "description": "Structured JavaScript exercises with automatic tests."}
    ],
    "project_ideas": ["Personal profile page", "Responsive landing page", "Student portfolio website", "JavaScript calculator", "To-do list with local storage", "Interactive quiz application", "Expense tracker", "Student record system using Flask and MySQL", "Community event portal", "Mini e-commerce application"],
    "communities": [
        {"name": "freeCodeCamp Forum", "url": "https://forum.freecodecamp.org/", "description": "Ask beginner questions and get help with projects."},
        {"name": "The Odin Project Community", "url": "https://www.theodinproject.com/community", "description": "Meet students following the same curriculum."},
        {"name": "DEV Community", "url": "https://dev.to/", "description": "Discuss tutorials, projects and career experiences."},
        {"name": "GitHub Community", "url": "https://github.com/orgs/community/discussions", "description": "Learn GitHub and open-source workflows."},
        {"name": "r/learnprogramming", "url": "https://www.reddit.com/r/learnprogramming/", "description": "Ask programming questions and get study advice."}
    ],
    "tools": [
        {"name": "Visual Studio Code", "description": "A free editor for web and Python code."},
        {"name": "Git and GitHub", "description": "Track changes and publish a project portfolio."},
        {"name": "Chrome or Firefox Developer Tools", "description": "Debug pages and test responsive layouts."},
        {"name": "Live Server and Prettier", "description": "Preview pages and format code inside VS Code."},
        {"name": "Python, Flask and MySQL", "description": "Back-end and database tools used by Career Compass."},
        {"name": "Postman", "description": "Test Flask routes and web APIs."},
        {"name": "W3C Validator and PageSpeed Insights", "description": "Check HTML quality, accessibility and performance."}
    ]
}

YOUTUBE_CHANNELS = [
    {"name": "freeCodeCamp.org", "url": "https://www.youtube.com/@freecodecamp", "description": "Long, beginner-friendly programming courses."},
    {"name": "CS50", "url": "https://www.youtube.com/@cs50", "description": "Computer-science lectures and programming lessons."}
]

SPECIALIZATION_RESOURCES = {
    "frontend": {
        "name": "Front-End Development",
        "documentation": [{"name": "MDN Learn Web Development", "url": "https://developer.mozilla.org/en-US/docs/Learn_web_development", "description": "HTML, CSS and JavaScript lessons from MDN."}],
        "free_courses": [{"name": "freeCodeCamp Responsive Web Design", "url": "https://www.freecodecamp.org/learn/2022/responsive-web-design/", "description": "Learn by building responsive web pages."}],
        "practice": [{"name": "Frontend Mentor", "url": "https://www.frontendmentor.io/challenges", "description": "Practise building designs with HTML, CSS and JavaScript."}],
        "project_ideas": ["Personal portfolio website", "Responsive college event page", "To-do list with JavaScript"]
    },
    "backend": {
        "name": "Back-End Development",
        "documentation": [{"name": "Flask Documentation", "url": "https://flask.palletsprojects.com/en/stable/tutorial/", "description": "The official beginner Flask tutorial."}],
        "free_courses": [{"name": "Python Tutorial", "url": "https://docs.python.org/3/tutorial/", "description": "Learn Python using the official tutorial."}],
        "practice": [{"name": "HackerRank Python", "url": "https://www.hackerrank.com/domains/python", "description": "Solve Python programming exercises."}],
        "project_ideas": ["Student record system", "Library management application", "Simple notes application with login"]
    },
    "fullstack": {
        "name": "Full-Stack Development",
        "documentation": [{"name": "MDN Learn Web Development", "url": "https://developer.mozilla.org/en-US/docs/Learn_web_development", "description": "Learn the main technologies used by websites."}, {"name": "Flask Tutorial", "url": "https://flask.palletsprojects.com/en/stable/tutorial/", "description": "Build a server-side application with Flask."}],
        "free_courses": [{"name": "freeCodeCamp Curriculum", "url": "https://www.freecodecamp.org/learn/", "description": "Free lessons covering web-development skills."}],
        "practice": [{"name": "GitHub Skills", "url": "https://skills.github.com/", "description": "Interactive lessons for Git and GitHub."}],
        "project_ideas": ["College placement portal", "Expense tracker", "Community event management website"]
    },
    "data_science": {
        "name": "Data Science",
        "documentation": [{"name": "Pandas Getting Started", "url": "https://pandas.pydata.org/docs/getting_started/index.html", "description": "Official tutorials for analysing data with Pandas."}],
        "free_courses": [{"name": "Kaggle Learn", "url": "https://www.kaggle.com/learn", "description": "Short courses covering Python, Pandas and visualization."}],
        "practice": [{"name": "Kaggle Datasets", "url": "https://www.kaggle.com/datasets", "description": "Public datasets for analysis practice."}],
        "project_ideas": ["Student performance analysis", "Local weather-data dashboard", "Community survey analysis"]
    },
    "machine_learning": {
        "name": "Machine Learning",
        "documentation": [{"name": "Scikit-learn User Guide", "url": "https://scikit-learn.org/stable/user_guide.html", "description": "Official guidance for machine-learning models."}],
        "free_courses": [{"name": "Google Machine Learning Crash Course", "url": "https://developers.google.com/machine-learning/crash-course", "description": "A practical introduction to machine-learning concepts."}],
        "practice": [{"name": "Kaggle Competitions", "url": "https://www.kaggle.com/competitions", "description": "Apply machine learning to practical datasets."}],
        "project_ideas": ["House-price prediction", "Spam-message classifier", "Plant-species classifier"]
    },
    "data_engineering": {
        "name": "Data Engineering",
        "documentation": [{"name": "MySQL Tutorial", "url": "https://dev.mysql.com/doc/refman/8.4/en/tutorial.html", "description": "Official introduction to MySQL databases."}],
        "free_courses": [{"name": "Kaggle Data Cleaning", "url": "https://www.kaggle.com/learn/data-cleaning", "description": "Practise preparing data for further use."}],
        "practice": [{"name": "SQLBolt", "url": "https://sqlbolt.com/", "description": "Interactive SQL lessons and exercises."}],
        "project_ideas": ["CSV-to-MySQL data loader", "Daily weather-data pipeline", "College attendance data warehouse"]
    },
    "cloud": {
        "name": "Cloud Engineering",
        "documentation": [{"name": "AWS Getting Started", "url": "https://aws.amazon.com/getting-started/", "description": "Beginner guides for core cloud services."}],
        "free_courses": [{"name": "Microsoft Learn: Azure Fundamentals", "url": "https://learn.microsoft.com/en-us/training/paths/describe-cloud-concepts/", "description": "Free modules explaining cloud concepts."}],
        "practice": [{"name": "Docker Get Started", "url": "https://docs.docker.com/get-started/", "description": "Guided practice with containers."}],
        "project_ideas": ["Host a static portfolio in the cloud", "Deploy a Flask application", "Create a cloud backup system"]
    },
    "devops": {
        "name": "DevOps Engineering",
        "documentation": [{"name": "Docker Get Started", "url": "https://docs.docker.com/get-started/", "description": "Official introduction to Docker containers."}],
        "free_courses": [{"name": "GitHub Skills", "url": "https://skills.github.com/", "description": "Free interactive GitHub and automation lessons."}],
        "practice": [{"name": "Killercoda", "url": "https://killercoda.com/", "description": "Browser-based Linux, Docker and Kubernetes labs."}],
        "project_ideas": ["Automated Flask deployment", "Dockerized college project", "CI/CD pipeline with automated tests"]
    },
    "embedded": {
        "name": "Embedded Systems",
        "documentation": [{"name": "Arduino Documentation", "url": "https://docs.arduino.cc/learn/", "description": "Official Arduino electronics and programming lessons."}],
        "free_courses": [{"name": "Arduino Built-in Examples", "url": "https://docs.arduino.cc/built-in-examples/", "description": "Small programs for learning hardware control."}],
        "practice": [{"name": "Wokwi Simulator", "url": "https://wokwi.com/projects/new/arduino-uno", "description": "Practise Arduino projects in a browser simulator."}],
        "project_ideas": ["Automatic street light", "Temperature monitoring system", "Smart plant-watering system"]
    },
    "qa": {
        "name": "QA Testing",
        "documentation": [{"name": "Selenium Documentation", "url": "https://www.selenium.dev/documentation/", "description": "Official guide to browser automation testing."}],
        "free_courses": [{"name": "Test Automation University", "url": "https://testautomationu.applitools.com/", "description": "Free courses on software testing tools."}],
        "practice": [{"name": "The Internet Test Site", "url": "https://the-internet.herokuapp.com/", "description": "Sample web pages designed for testing practice."}],
        "project_ideas": ["Test plan for an e-commerce website", "Automated login-page tests", "API testing collection in Postman"]
    },
    "cybersecurity": {
        "name": "Cybersecurity",
        "documentation": [{"name": "OWASP Web Security Testing Guide", "url": "https://owasp.org/www-project-web-security-testing-guide/", "description": "A structured guide to web-security testing."}],
        "free_courses": [{"name": "Cisco Introduction to Cybersecurity", "url": "https://www.netacad.com/courses/introduction-to-cybersecurity", "description": "A beginner course covering security concepts."}],
        "practice": [{"name": "TryHackMe Learning Paths", "url": "https://tryhackme.com/paths", "description": "Guided cybersecurity labs in a legal environment."}],
        "project_ideas": ["Password-strength checker", "Basic network traffic report", "Security checklist for a Flask website"]
    }
}
