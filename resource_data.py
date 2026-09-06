"""Curated learning resources for Career Compass Resource Hub.

Resources are grouped by the four Career Compass domains:
1. Web & Application Development
2. Data & Artificial Intelligence
3. Systems & Infrastructure
4. Quality & Security

The collection intentionally mixes official documentation, structured courses,
beginner-friendly YouTube learning, practice platforms, and project ideas.
"""

WEB_RESOURCE_HUB = {
    "name": "Web & Application Development",
    "youtube_channels": [
        {"name": "SuperSimpleDev", "url": "https://www.youtube.com/@SuperSimpleDev", "description": "Beginner-friendly HTML, CSS, JavaScript, React and full-stack tutorials."},
        {"name": "Bro Code", "url": "https://www.youtube.com/@BroCodez", "description": "Project-based web development walkthroughs for beginners."},
        {"name": "freeCodeCamp.org", "url": "https://www.youtube.com/@freecodecamp", "description": "Full-length beginner courses on web development and programming."},
        {"name": "Traversy Media", "url": "https://www.youtube.com/@TraversyMedia", "description": "Clear real-world web development projects and tutorials."},
        {"name": "Kevin Powell", "url": "https://www.youtube.com/@KevinPowell", "description": "Practical CSS and frontend fundamentals for new developers."},
    ],
    "documentation": [
        {"name": "MDN Learn Web Development", "url": "https://developer.mozilla.org/en-US/docs/Learn_web_development", "description": "Mozilla’s beginner-friendly web development curriculum."},
        {"name": "MDN JavaScript Guide", "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide", "description": "Official JavaScript language reference and tutorials."},
        {"name": "Flask Tutorial", "url": "https://flask.palletsprojects.com/en/stable/tutorial/", "description": "Official Flask walkthrough for Python web applications."},
        {"name": "Python Tutorial", "url": "https://docs.python.org/3/tutorial/", "description": "Python basics for backend development and scripting."},
        {"name": "MySQL Tutorial", "url": "https://dev.mysql.com/doc/refman/8.4/en/tutorial.html", "description": "Official SQL and database tutorial for beginners."},
    ],
    "free_courses": [
        {"name": "freeCodeCamp Responsive Web Design", "url": "https://www.freecodecamp.org/learn/2022/responsive-web-design/", "description": "Free beginner-friendly HTML and CSS curriculum with projects."},
        {"name": "The Odin Project Foundations", "url": "https://www.theodinproject.com/paths/foundations/courses/foundations", "description": "Free project-based web development path that covers HTML, CSS, JavaScript and Git."},
        {"name": "Meta Front-End Developer Professional Certificate", "url": "https://www.coursera.org/professional-certificates/meta-front-end-developer/", "description": "Beginner-focused front-end specialization; audit available free."},
        {"name": "IBM Full Stack Software Developer Professional Certificate", "url": "https://www.coursera.org/professional-certificates/ibm-full-stack-cloud-developer/", "description": "Full-stack web developer path with Python, Flask, databases and deployment; audit available free."},
    ],
    "video_courses": [
        {"name": "HTML & CSS Full Course - SuperSimpleDev", "url": "https://youtu.be/G3e-cpL7ofc", "description": "Beginner HTML/CSS course with live coding exercises."},
        {"name": "JavaScript Tutorial - SuperSimpleDev", "url": "https://youtu.be/SBmSRK3feww", "description": "Beginner-focused JavaScript course with practical examples."},
    ],
    "materials": [
        {"name": "MDN Getting Started Modules", "url": "https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started", "description": "Beginner web tool setup and first-website guidance."},
        {"name": "Web Accessibility Guidelines - MDN", "url": "https://developer.mozilla.org/en-US/docs/Web/Accessibility", "description": "Accessible design best practices for web applications."},
        {"name": "GitHub Skills", "url": "https://skills.github.com/", "description": "Interactive Git and GitHub tutorials for beginners."},
    ],
    "practice": [
        {"name": "Frontend Mentor", "url": "https://www.frontendmentor.io/challenges", "description": "Real UI design challenges to build portfolio projects."},
        {"name": "freeCodeCamp", "url": "https://www.freecodecamp.org/learn/", "description": "Hands-on web development practice and certification projects."},
        {"name": "Exercism JavaScript", "url": "https://exercism.org/tracks/javascript", "description": "Structured JavaScript practice with mentor feedback."},
        {"name": "HackerRank JavaScript", "url": "https://www.hackerrank.com/domains/tutorials/10-days-of-javascript", "description": "Beginner-focused JavaScript challenges with automatic feedback."},
    ],
    "project_ideas": [
        "Responsive student portfolio",
        "College event management website",
        "JavaScript expense tracker",
        "Student record system using Flask and MySQL",
        "Full-stack placement preparation portal",
    ],
    "communities": [
        {"name": "freeCodeCamp Forum", "url": "https://forum.freecodecamp.org/", "description": "Open beginner community for web development questions."},
        {"name": "The Odin Project Community", "url": "https://www.theodinproject.com/community", "description": "Peer support for project-based web development learners."},
        {"name": "GitHub Community", "url": "https://github.com/orgs/community/discussions", "description": "Developer discussions and open-source collaboration."},
    ],
    "tools": [
        {"name": "Visual Studio Code", "url": "https://code.visualstudio.com/", "description": "Popular editor with strong web development support."},
        {"name": "Git", "url": "https://git-scm.com/", "description": "Version control for tracking code changes and collaboration."},
        {"name": "Postman", "url": "https://www.postman.com/downloads/", "description": "API testing tool for backend and full-stack projects."},
        {"name": "W3C Validator", "url": "https://validator.w3.org/", "description": "Checks HTML markup and accessibility issues."},
    ],
}

YOUTUBE_CHANNELS = WEB_RESOURCE_HUB["youtube_channels"]

RESOURCE_COLLECTION_DOMAINS = {
    "web": {
        "name": "Web & Application Development",
        "description": "Resources for frontend, backend and full-stack web development.",
        "focus_areas": ["Frontend", "Backend", "Full-Stack", "APIs", "Databases"],
    },
    "ai": {
        "name": "Data & Artificial Intelligence",
        "description": "Resources for data science, machine learning, AI and data engineering.",
        "focus_areas": ["Data Science", "Machine Learning", "AI", "Data Engineering", "Generative AI"],
    },
    "systems": {
        "name": "Systems & Infrastructure",
        "description": "Resources for cloud, DevOps, networking and embedded systems.",
        "focus_areas": ["Cloud", "DevOps", "Networking", "Linux", "Embedded Systems"],
    },
    "security": {
        "name": "Quality & Security",
        "description": "Resources for software testing, quality assurance and cybersecurity.",
        "focus_areas": ["QA Testing", "Automation Testing", "Cybersecurity", "Web Security", "Security Fundamentals"],
    },
}

AI_RESOURCE_HUB = {
    "name": "Data & Artificial Intelligence",
    "youtube_channels": [
        {"name": "freeCodeCamp.org", "url": "https://www.youtube.com/@freecodecamp", "description": "Beginner-friendly data science and ML tutorials with full project walkthroughs."},
        {"name": "StatQuest with Josh Starmer", "url": "https://www.youtube.com/@statquest", "description": "Clear explanations of statistics and machine learning concepts for beginners."},
        {"name": "Data School", "url": "https://www.youtube.com/@DataSchool", "description": "Python data analysis tutorials focusing on pandas and scikit-learn."},
        {"name": "IBM Technology", "url": "https://www.youtube.com/@IBMTechnology", "description": "Industry-focused AI and data engineering content from IBM."},
    ],
    "documentation": [
        {"name": "Google Machine Learning Crash Course", "url": "https://developers.google.com/machine-learning/crash-course", "description": "Free interactive ML curriculum with videos, exercises and TensorFlow examples."},
        {"name": "scikit-learn User Guide", "url": "https://scikit-learn.org/stable/user_guide.html", "description": "Official guide to common machine learning algorithms and workflows."},
        {"name": "Pandas Getting Started", "url": "https://pandas.pydata.org/docs/getting_started/index.html", "description": "Official intro to data analysis with pandas."},
        {"name": "NumPy User Guide", "url": "https://numpy.org/doc/stable/user/", "description": "Official numerical computing guide for Python."},
        {"name": "Python Tutorial", "url": "https://docs.python.org/3/tutorial/", "description": "Official Python programming tutorial for beginners."},
    ],
    "free_courses": [
        {"name": "Google Machine Learning Crash Course", "url": "https://developers.google.com/machine-learning/crash-course", "description": "Free beginner ML course with interactive exercises and visualizations."},
        {"name": "IBM SkillsBuild Artificial Intelligence", "url": "https://skillsbuild.org/college-students/artificial-intelligence", "description": "Free AI fundamentals and responsible AI learning path."},
        {"name": "Kaggle Learn", "url": "https://www.kaggle.com/learn", "description": "Free short practical courses in Python, pandas, data visualization and ML."},
        {"name": "Microsoft Learn AI Fundamentals", "url": "https://learn.microsoft.com/en-us/training/paths/azure-ai-fundamentals/", "description": "Free introductory AI concepts and Azure AI technology learning."},
    ],
    "video_courses": [
        {"name": "Introduction to Machine Learning - freeCodeCamp", "url": "https://youtu.be/i_LwzRVP7bg", "description": "Beginner-focused machine learning overview with examples."},
        {"name": "Python for Data Science - freeCodeCamp", "url": "https://youtu.be/LHBE6Q9XlzI", "description": "Python foundations for data science with real examples."},
    ],
    "materials": [
        {"name": "Google ML Crash Course Exercises", "url": "https://developers.google.com/machine-learning/crash-course/exercises", "description": "Practical programming exercises for ML concepts."},
        {"name": "Google ML Crash Course Prerequisites", "url": "https://developers.google.com/machine-learning/crash-course/prereqs-and-prework", "description": "Preparation material for Python, NumPy, pandas and math."},
        {"name": "IBM AI Fundamentals", "url": "https://skillsbuild.org/college-students/artificial-intelligence", "description": "Structured AI learning material and project resources."},
    ],
    "practice": [
        {"name": "Kaggle Datasets", "url": "https://www.kaggle.com/datasets", "description": "Public datasets for data analysis and machine learning practice."},
        {"name": "Kaggle Competitions", "url": "https://www.kaggle.com/competitions", "description": "Beginner-friendly ML challenges and real-data projects."},
        {"name": "Google Colab", "url": "https://colab.research.google.com/", "description": "Free Python notebooks for data and machine learning experimentation."},
    ],
    "project_ideas": [
        "Student performance analysis dashboard",
        "House-price prediction model",
        "Spam-message classifier",
        "College placement data analysis",
        "Movie recommendation prototype",
    ],
    "communities": [
        {"name": "Kaggle Community", "url": "https://www.kaggle.com/discussions", "description": "Discuss datasets, notebooks and machine learning questions."},
        {"name": "Hugging Face Community", "url": "https://huggingface.co/", "description": "Explore open-source AI models and community resources."},
    ],
    "tools": [
        {"name": "Jupyter", "url": "https://jupyter.org/", "description": "Interactive notebooks for Python data work."},
        {"name": "Google Colab", "url": "https://colab.research.google.com/", "description": "Cloud-hosted notebooks for data experiments."},
        {"name": "Kaggle", "url": "https://www.kaggle.com/", "description": "Datasets, notebooks and competitions for beginners."},
    ],
}

SYSTEMS_RESOURCE_HUB = {
    "name": "Systems & Infrastructure",
    "youtube_channels": [
        {"name": "NetworkChuck", "url": "https://www.youtube.com/@NetworkChuck", "description": "Beginner-friendly networking, Linux, cloud and DevOps videos."},
        {"name": "TechWorld with Nana", "url": "https://www.youtube.com/@TechWorldwithNana", "description": "Visual explainers for Docker, Kubernetes and CI/CD."},
        {"name": "Kunal Kushwaha", "url": "https://www.youtube.com/@KunalKushwaha", "description": "DevOps, cloud-native tools and infrastructure tutorials."},
        {"name": "AWS Training and Certification", "url": "https://www.youtube.com/@AWSTraining", "description": "Official AWS cloud and infrastructure training content."},
    ],
    "documentation": [
        {"name": "AWS Skill Builder", "url": "https://skillbuilder.aws/", "description": "Free AWS cloud training and hands-on labs."},
        {"name": "Microsoft Learn - Discover DevOps", "url": "https://learn.microsoft.com/en-us/training/modules/discover-devops/", "description": "Introductory DevOps concepts and team workflows."},
        {"name": "Microsoft Learn - Develop with DevOps", "url": "https://learn.microsoft.com/en-us/training/modules/develop-with-devops/", "description": "Practical Git, GitHub and CI/CD fundamentals."},
        {"name": "Docker Get Started", "url": "https://docs.docker.com/get-started/", "description": "Official Docker getting started guide and tutorials."},
        {"name": "Kubernetes Documentation", "url": "https://kubernetes.io/docs/home/", "description": "Authoritative Kubernetes concepts and tutorials."},
    ],
    "free_courses": [
        {"name": "AWS Skill Builder", "url": "https://skillbuilder.aws/", "description": "Free cloud foundations and labs from AWS."},
        {"name": "Microsoft Learn - Develop with DevOps", "url": "https://learn.microsoft.com/en-us/training/modules/develop-with-devops/", "description": "Free beginner module on Git, CI/CD and DevOps workflows."},
        {"name": "Microsoft Learn - Discover DevOps", "url": "https://learn.microsoft.com/en-us/training/modules/discover-devops/", "description": "Free introduction to DevOps culture and practices."},
        {"name": "Linux Journey", "url": "https://linuxjourney.com/", "description": "Free interactive Linux tutorials for command-line beginners."},
    ],
    "video_courses": [
        {"name": "AWS Training and Certification - Cloud Learning Journey", "url": "https://youtu.be/BY-1rYe85qI", "description": "Official AWS cloud learning overview video."},
        {"name": "Kunal Kushwaha DevOps Bootcamp", "url": "https://www.techwithkunal.com/courses/devops", "description": "Free curated DevOps path covering Linux, Docker and Kubernetes."},
    ],
    "materials": [
        {"name": "Docker Workshop", "url": "https://docs.docker.com/get-started/workshop/", "description": "Hands-on Docker workshop for container fundamentals."},
        {"name": "Kubernetes Basics", "url": "https://kubernetes.io/docs/tutorials/kubernetes-basics/", "description": "Interactive Kubernetes tutorial with concept walkthroughs."},
        {"name": "Microsoft Learn - Explore Azure Pipelines", "url": "https://learn.microsoft.com/en-us/training/modules/explore-azure-pipelines/", "description": "CI/CD learning material for Azure Pipelines."},
    ],
    "practice": [
        {"name": "Docker Get Started", "url": "https://docs.docker.com/get-started/", "description": "Guided Docker hands-on learning."},
        {"name": "Killercoda", "url": "https://killercoda.com/", "description": "Browser-based Linux, Docker and Kubernetes labs."},
        {"name": "Play with Docker", "url": "https://labs.play-with-docker.com/", "description": "In-browser Docker playground for practice."},
    ],
    "project_ideas": [
        "Dockerize the Career Compass Flask application",
        "Deploy a Flask website to the cloud",
        "Build a CI/CD pipeline for a GitHub project",
        "Linux server monitoring dashboard",
        "Containerized college event application",
    ],
    "communities": [
        {"name": "AWS Community", "url": "https://community.aws/", "description": "Community learning and support for AWS training."},
        {"name": "Kubernetes Community", "url": "https://www.kubernetes.dev/", "description": "Kubernetes learning resources and collaboration."},
    ],
    "tools": [
        {"name": "Docker", "url": "https://www.docker.com/", "description": "Containerization platform."},
        {"name": "GitHub Actions", "url": "https://github.com/features/actions", "description": "Automation and CI/CD workflows integrated with GitHub."},
        {"name": "Kubernetes", "url": "https://kubernetes.io/", "description": "Orchestration platform for containerized apps."},
        {"name": "AWS", "url": "https://aws.amazon.com/", "description": "Cloud platform for modern infrastructure."},
    ],
}

SECURITY_RESOURCE_HUB = {
    "name": "Quality & Security",
    "youtube_channels": [
        {"name": "Professor Messer", "url": "https://www.youtube.com/@professormesser", "description": "Beginner-focused cybersecurity fundamentals, networking and Security+ concepts."},
        {"name": "John Hammond", "url": "https://www.youtube.com/@_JohnHammond", "description": "Practical and ethical cybersecurity labs and threat analysis."},
        {"name": "freeCodeCamp.org", "url": "https://www.youtube.com/@freecodecamp", "description": "Long-form learning resources for QA and security-related topics."},
    ],
    "documentation": [
        {"name": "Cisco Networking Academy", "url": "https://www.netacad.com/", "description": "Official networking and cybersecurity learning paths."},
        {"name": "Fortinet Training Institute", "url": "https://training.fortinet.com/", "description": "Free security training resources and certification preparation."},
        {"name": "OWASP Web Security Testing Guide", "url": "https://owasp.org/www-project-web-security-testing-guide/", "description": "Comprehensive web application security testing guide."},
        {"name": "Selenium Documentation", "url": "https://www.selenium.dev/documentation/", "description": "Official browser automation and test automation documentation."},
        {"name": "Postman Learning Center", "url": "https://learning.postman.com/", "description": "Official API testing documentation and tutorials."},
    ],
    "free_courses": [
        {"name": "Cisco Introduction to Cybersecurity", "url": "https://www.netacad.com/courses/cybersecurity/introduction-to-cybersecurity", "description": "Free beginner cybersecurity course from Cisco Networking Academy."},
        {"name": "Fortinet Training Institute", "url": "https://training.fortinet.com/", "description": "Free security fundamentals courses and labs."},
        {"name": "Test Automation University", "url": "https://testautomationu.applitools.com/", "description": "Free courses for software testing, automation and Selenium."},
        {"name": "OWASP Web Security Testing Guide", "url": "https://owasp.org/www-project-web-security-testing-guide/", "description": "Free official web security testing learning material."},
    ],
    "video_courses": [
        {"name": "Cisco Cybersecurity Learning", "url": "https://www.youtube.com/@CiscoSecure", "description": "Cisco’s security-focused video content for learners."},
        {"name": "Professor Messer Security+ Training", "url": "https://www.youtube.com/@professormesser", "description": "Free security fundamentals videos and study guides."},
    ],
    "materials": [
        {"name": "OWASP Web Security Testing Guide", "url": "https://owasp.org/www-project-web-security-testing-guide/", "description": "Official web security testing reference material."},
        {"name": "Professor Messer Security+ Course Notes", "url": "https://www.professormesser.com/security-plus/sy0-701/sy0-701-course-notes/", "description": "Free security fundamentals study notes."},
        {"name": "Selenium Documentation", "url": "https://www.selenium.dev/documentation/", "description": "Browser automation and test automation reference."},
    ],
    "practice": [
        {"name": "TryHackMe Learning Paths", "url": "https://tryhackme.com/paths", "description": "Guided cybersecurity labs for legal hands-on practice."},
        {"name": "OWASP Juice Shop", "url": "https://owasp.org/www-project-juice-shop/", "description": "Intentionally vulnerable web app for security practice."},
        {"name": "The Internet Test Site", "url": "https://the-internet.herokuapp.com/", "description": "Sample web app for automated testing and QA practice."},
    ],
    "project_ideas": [
        "Automated login-page test suite",
        "API testing collection using Postman",
        "Security checklist for a Flask application",
        "Basic vulnerability-reporting dashboard",
        "Web application test plan",
    ],
    "communities": [
        {"name": "OWASP Community", "url": "https://owasp.org/", "description": "Community support for security awareness and training."},
        {"name": "Cisco Networking Academy", "url": "https://www.netacad.com/", "description": "Networking and cybersecurity learning community."},
        {"name": "TryHackMe Community", "url": "https://tryhackme.com/classrooms", "description": "Cybersecurity study groups and community learning resources."},
    ],
    "tools": [
        {"name": "Selenium", "url": "https://www.selenium.dev/", "description": "Browser automation and QA testing tool."},
        {"name": "Postman", "url": "https://www.postman.com/", "description": "API testing and automation tool."},
        {"name": "OWASP ZAP", "url": "https://www.zaproxy.org/", "description": "Open-source web security scanning tool."},
        {"name": "GitHub Actions", "url": "https://github.com/features/actions", "description": "CI/CD automation for testing and deployments."},
    ],
}

# Resources for specialization pages.
SPECIALIZATION_RESOURCES = {
    "frontend": {
        "name": "Front-End Development",
        "documentation": [
            {"name": "MDN Learn Web Development", "url": "https://developer.mozilla.org/en-US/docs/Learn_web_development", "description": "HTML, CSS, JavaScript and accessibility foundations."},
        ],
        "free_courses": [
            {"name": "Meta Front-End Developer Professional Certificate", "url": "https://www.coursera.org/professional-certificates/meta-front-end-developer/", "description": "Structured front-end learning from Meta."},
        ],
        "practice": [
            {"name": "Frontend Mentor", "url": "https://www.frontendmentor.io/challenges", "description": "Build responsive interfaces from real design briefs."},
        ],
        "materials": [
            {"name": "MDN Getting Started", "url": "https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started", "description": "Beginner web-development setup and learning material."},
        ],
        "project_ideas": ["Portfolio website", "Responsive college event page", "Interactive dashboard"],
    },
    "backend": {
        "name": "Back-End Development",
        "documentation": [
            {"name": "Flask Documentation", "url": "https://flask.palletsprojects.com/en/stable/tutorial/", "description": "Official Flask tutorial."},
            {"name": "Python Documentation", "url": "https://docs.python.org/3/tutorial/", "description": "Official Python tutorial."},
        ],
        "free_courses": [
            {"name": "IBM Full Stack Software Developer Professional Certificate", "url": "https://www.coursera.org/professional-certificates/ibm-full-stack-cloud-developer", "description": "Backend, APIs, databases, containers and cloud-native development."},
        ],
        "practice": [
            {"name": "HackerRank Python", "url": "https://www.hackerrank.com/domains/python", "description": "Python programming practice."},
        ],
        "materials": [
            {"name": "MySQL Tutorial", "url": "https://dev.mysql.com/doc/refman/8.4/en/tutorial.html", "description": "Database and SQL learning material."},
        ],
        "project_ideas": ["Student record API", "Library management backend", "Notes application with authentication"],
    },
    "fullstack": {
        "name": "Full-Stack Development",
        "documentation": [
            {"name": "MDN Learn Web Development", "url": "https://developer.mozilla.org/en-US/docs/Learn_web_development", "description": "Frontend fundamentals."},
            {"name": "Flask Tutorial", "url": "https://flask.palletsprojects.com/en/stable/tutorial/", "description": "Backend application development with Flask."},
        ],
        "free_courses": [
            {"name": "IBM Full Stack Software Developer Professional Certificate", "url": "https://www.coursera.org/professional-certificates/ibm-full-stack-cloud-developer", "description": "End-to-end full-stack development and deployment."},
        ],
        "practice": [
            {"name": "GitHub Skills", "url": "https://skills.github.com/", "description": "Interactive Git and GitHub practice."},
        ],
        "materials": [
            {"name": "Postman Learning Center", "url": "https://learning.postman.com/", "description": "API development and testing material."},
        ],
        "project_ideas": ["Placement portal", "Expense tracker", "Community event management website"],
    },
    "data_science": {
        "name": "Data Science",
        "documentation": [
            {"name": "Pandas Getting Started", "url": "https://pandas.pydata.org/docs/getting_started/index.html", "description": "Official Pandas data-analysis tutorials."},
            {"name": "NumPy User Guide", "url": "https://numpy.org/doc/stable/user/", "description": "Official numerical-computing material."},
        ],
        "free_courses": [
            {"name": "Kaggle Learn", "url": "https://www.kaggle.com/learn", "description": "Short practical courses for Python, Pandas and data analysis."},
        ],
        "practice": [
            {"name": "Kaggle Datasets", "url": "https://www.kaggle.com/datasets", "description": "Real datasets for analysis projects."},
        ],
        "materials": [
            {"name": "Google ML Crash Course Exercises", "url": "https://developers.google.com/machine-learning/crash-course/exercises", "description": "Interactive data and ML exercises."},
        ],
        "project_ideas": ["Student performance analysis", "Survey analysis dashboard", "Weather-data analysis"],
    },
    "machine_learning": {
        "name": "Machine Learning",
        "documentation": [
            {"name": "Google Machine Learning Crash Course", "url": "https://developers.google.com/machine-learning/crash-course", "description": "Practical ML concepts and exercises."},
            {"name": "scikit-learn User Guide", "url": "https://scikit-learn.org/stable/user_guide.html", "description": "Official ML model and workflow reference."},
        ],
        "free_courses": [
            {"name": "Google Machine Learning Crash Course", "url": "https://developers.google.com/machine-learning/crash-course", "description": "Hands-on ML course from Google."},
        ],
        "practice": [
            {"name": "Kaggle Competitions", "url": "https://www.kaggle.com/competitions", "description": "Practical ML challenges."},
        ],
        "materials": [
            {"name": "Google ML Crash Course Exercises", "url": "https://developers.google.com/machine-learning/crash-course/exercises", "description": "Programming and interactive ML exercises."},
        ],
        "project_ideas": ["House-price prediction", "Spam classifier", "Student performance predictor"],
    },
    "data_engineering": {
        "name": "Data Engineering",
        "documentation": [
            {"name": "MySQL Tutorial", "url": "https://dev.mysql.com/doc/refman/8.4/en/tutorial.html", "description": "Database fundamentals."},
            {"name": "Apache Spark Documentation", "url": "https://spark.apache.org/docs/latest/", "description": "Reference for large-scale data processing."},
        ],
        "free_courses": [
            {"name": "Kaggle Learn", "url": "https://www.kaggle.com/learn", "description": "Practical data-cleaning and data-workflow courses."},
        ],
        "practice": [
            {"name": "SQLBolt", "url": "https://sqlbolt.com/", "description": "Interactive SQL lessons."},
        ],
        "materials": [
            {"name": "PostgreSQL Tutorial", "url": "https://www.postgresql.org/docs/current/tutorial.html", "description": "Official relational database tutorial."},
        ],
        "project_ideas": ["CSV-to-database pipeline", "Attendance data warehouse", "Daily weather-data pipeline"],
    },
    "cloud": {
        "name": "Cloud Engineering",
        "documentation": [
            {"name": "AWS Skill Builder", "url": "https://skillbuilder.aws/", "description": "Official AWS cloud learning."},
            {"name": "Microsoft Learn Azure", "url": "https://learn.microsoft.com/en-us/training/azure/", "description": "Structured Azure learning paths."},
        ],
        "free_courses": [
            {"name": "AWS Skill Builder", "url": "https://skillbuilder.aws/", "description": "Cloud fundamentals and AWS services."},
            {"name": "Microsoft Learn - Cloud", "url": "https://learn.microsoft.com/en-us/training/azure/", "description": "Free Azure cloud learning modules."},
        ],
        "practice": [
            {"name": "Docker Get Started", "url": "https://docs.docker.com/get-started/", "description": "Container practice useful for cloud deployments."},
        ],
        "materials": [
            {"name": "AWS Architecture Center", "url": "https://aws.amazon.com/architecture/", "description": "Cloud architecture reference material and patterns."},
        ],
        "project_ideas": ["Deploy a Flask app", "Cloud-hosted portfolio", "Cloud backup system"],
    },
    "devops": {
        "name": "DevOps Engineering",
        "documentation": [
            {"name": "Docker Get Started", "url": "https://docs.docker.com/get-started/", "description": "Official containerization guide."},
            {"name": "Microsoft Learn - Develop with DevOps", "url": "https://learn.microsoft.com/en-us/training/modules/develop-with-devops/", "description": "Git, GitHub, CI and shift-left DevOps practices."},
        ],
        "free_courses": [
            {"name": "Kunal Kushwaha DevOps Bootcamp", "url": "https://www.techwithkunal.com/courses/devops", "description": "Free DevOps bootcamp covering Linux, Docker, Kubernetes, CI/CD and cloud."},
            {"name": "Microsoft Learn - Discover DevOps", "url": "https://learn.microsoft.com/en-us/training/modules/discover-devops/", "description": "Beginner DevOps fundamentals."},
        ],
        "practice": [
            {"name": "Killercoda", "url": "https://killercoda.com/", "description": "Browser-based DevOps and Kubernetes practice."},
        ],
        "materials": [
            {"name": "Kubernetes Basics", "url": "https://kubernetes.io/docs/tutorials/kubernetes-basics/", "description": "Interactive Kubernetes learning material."},
        ],
        "project_ideas": ["Dockerized Flask application", "CI/CD pipeline", "Automated deployment workflow"],
    },
    "embedded": {
        "name": "Embedded Systems",
        "documentation": [
            {"name": "Arduino Learn", "url": "https://docs.arduino.cc/learn", "description": "Official Arduino hardware and programming learning material."},
            {"name": "Arduino Built-in Examples", "url": "https://docs.arduino.cc/built-in-examples/", "description": "Ready-to-study Arduino examples."},
        ],
        "free_courses": [
            {"name": "Arduino Built-in Examples", "url": "https://docs.arduino.cc/built-in-examples/", "description": "Hands-on examples for learning microcontroller programming."},
        ],
        "practice": [
            {"name": "Wokwi", "url": "https://wokwi.com/", "description": "Browser-based electronics and Arduino simulator."},
        ],
        "materials": [
            {"name": "Arduino Learn", "url": "https://docs.arduino.cc/learn", "description": "Reference material for digital pins, analog input, PWM and sketches."},
        ],
        "project_ideas": ["Automatic street light", "Temperature monitoring system", "Smart plant-watering system"],
    },
    "qa": {
        "name": "QA Testing",
        "documentation": [
            {"name": "Selenium Documentation", "url": "https://www.selenium.dev/documentation/", "description": "Official browser automation testing documentation."},
            {"name": "Postman Learning Center", "url": "https://learning.postman.com/", "description": "API testing and development material."},
        ],
        "free_courses": [
            {"name": "Test Automation University", "url": "https://testautomationu.applitools.com/", "description": "Free courses on software testing and automation."},
        ],
        "practice": [
            {"name": "The Internet Test Site", "url": "https://the-internet.herokuapp.com/", "description": "Purpose-built web pages for automation testing practice."},
        ],
        "materials": [
            {"name": "Selenium Documentation", "url": "https://www.selenium.dev/documentation/", "description": "Reference material for automated browser testing."},
        ],
        "project_ideas": ["E-commerce test plan", "Automated login tests", "API testing collection"],
    },
    "cybersecurity": {
        "name": "Cybersecurity",
        "documentation": [
            {"name": "OWASP Web Security Testing Guide", "url": "https://owasp.org/www-project-web-security-testing-guide/", "description": "Detailed guide for web application security testing."},
            {"name": "Cisco Networking Academy", "url": "https://www.netacad.com/en", "description": "Beginner cybersecurity and networking learning paths."},
            {"name": "Fortinet Training Institute", "url": "https://training.fortinet.com/", "description": "Security training and certification-oriented resources."},
        ],
        "free_courses": [
            {"name": "Cisco Introduction to Cybersecurity", "url": "https://www.netacad.com/courses/introduction-to-cybersecurity", "description": "Free beginner cybersecurity course."},
            {"name": "Fortinet Training Institute", "url": "https://training.fortinet.com/", "description": "Security fundamentals and certification-aligned training."},
        ],
        "practice": [
            {"name": "TryHackMe Learning Paths", "url": "https://tryhackme.com/paths", "description": "Guided cybersecurity labs in legal learning environments."},
            {"name": "OWASP Juice Shop", "url": "https://owasp.org/www-project-juice-shop/", "description": "Intentionally vulnerable web application for security practice."},
        ],
        "materials": [
            {"name": "OWASP WSTG PDF and Web Guide", "url": "https://owasp.org/www-project-web-security-testing-guide/", "description": "Versioned security-testing guide available online and as PDF releases."},
            {"name": "Professor Messer Security+ Course Notes", "url": "https://www.professormesser.com/security-plus/sy0-701/sy0-701-course-notes/", "description": "Free security fundamentals study notes."},
        ],
        "project_ideas": ["Flask security checklist", "Basic vulnerability report", "Password-strength checker"],
    },
}

# Backward-compatible aliases used by existing code, if any.
SPECIALIZATION_RESOURCES = {
    key: value
    for key, value in {
        **SPECIALIZATION_RESOURCES,
    }.items()
}
