"""Specialization-specific learning resources for Career Compass Resource Hub.

Provides rich, tailored resource collections for all 11 career specializations:
1. Frontend Development (frontend)
2. Backend Development (backend)
3. Full-Stack Development (fullstack)
4. Data Science (data_science)
5. Machine Learning (machine_learning)
6. Data Engineering (data_engineering)
7. Cloud Engineering (cloud)
8. DevOps Engineering (devops)
9. Embedded Systems (embedded)
10. QA Testing (qa)
11. Cybersecurity (cybersecurity)

Each specialization includes curated:
- Documentation
- YouTube Channels
- Free Courses
- Study Materials
- Practice Platforms
- Project Ideas
- Communities
- Tools
"""

FRONTEND_RESOURCES = {
    "name": "Front-End Development",
    "domain": "web",
    "domain_name": "Web & Application Development",
    "youtube_channels": [
        {"name": "Kevin Powell", "url": "https://www.youtube.com/@KevinPowell", "description": "Practical CSS, flexbox, grid, and modern responsive UI design tutorials."},
        {"name": "SuperSimpleDev", "url": "https://www.youtube.com/@SuperSimpleDev", "description": "Beginner-friendly HTML, CSS, JavaScript, and React project walkthroughs."},
        {"name": "Web Dev Simplified", "url": "https://www.youtube.com/@WebDevSimplified", "description": "Clean, concise explanations of frontend web development and DOM concepts."},
        {"name": "Traversy Media", "url": "https://www.youtube.com/@TraversyMedia", "description": "Hands-on web UI crash courses and practical interface projects."},
    ],
    "documentation": [
        {"name": "MDN Learn Web Development", "url": "https://developer.mozilla.org/en-US/docs/Learn_web_development", "description": "Mozilla's authoritative curriculum for HTML, CSS, and JavaScript."},
        {"name": "MDN JavaScript Guide", "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide", "description": "Official JavaScript language reference, syntax, and DOM manipulation."},
        {"name": "CSS-Tricks Flexbox & Grid Guides", "url": "https://css-tricks.com/snippets/css/a-guide-to-flexbox/", "description": "Visual reference guides for modern CSS layout models."},
    ],
    "free_courses": [
        {"name": "freeCodeCamp Responsive Web Design", "url": "https://www.freecodecamp.org/learn/2022/responsive-web-design/", "description": "Interactive HTML5 and CSS3 curriculum with 5 certification projects."},
        {"name": "The Odin Project - Foundations", "url": "https://www.theodinproject.com/paths/foundations/courses/foundations", "description": "Free, open-source project-based curriculum covering frontend basics and Git."},
        {"name": "Meta Front-End Developer Professional Certificate", "url": "https://www.coursera.org/professional-certificates/meta-front-end-developer", "description": "Structured frontend career curriculum from Meta (free audit available)."},
    ],
    "materials": [
        {"name": "MDN Getting Started Guide", "url": "https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started", "description": "Essential web development setup, tooling, and first-site walkthroughs."},
        {"name": "Web Accessibility Guidelines (W3C WAI)", "url": "https://www.w3.org/WAI/fundamentals/accessibility-intro/", "description": "Foundational accessibility principles for accessible user interfaces."},
    ],
    "practice": [
        {"name": "Frontend Mentor", "url": "https://www.frontendmentor.io/challenges", "description": "Real-world HTML/CSS/JS design briefs to build portfolio-ready web interfaces."},
        {"name": "Exercism JavaScript Track", "url": "https://exercism.org/tracks/javascript", "description": "Hands-on JavaScript coding exercises with automated and mentor feedback."},
        {"name": "CSSBattle", "url": "https://cssbattle.dev/", "description": "Gamified CSS target replication challenges to master visual styling."},
    ],
    "project_ideas": [
        "Responsive personal portfolio website with dark mode toggle",
        "Interactive recipe and meal finder using a public REST API",
        "College event schedule and registration landing page",
        "Kanban task board application with drag-and-drop support",
    ],
    "communities": [
        {"name": "Frontend Mentor Community", "url": "https://www.frontendmentor.io/community", "description": "Active community for UI code reviews and feedback."},
        {"name": "freeCodeCamp Forum", "url": "https://forum.freecodecamp.org/", "description": "Helpful peer forum for frontend programming questions."},
    ],
    "tools": [
        {"name": "Visual Studio Code", "url": "https://code.visualstudio.com/", "description": "Popular code editor with rich web extensions."},
        {"name": "Figma", "url": "https://www.figma.com/", "description": "Industry-standard UI/UX design and prototyping tool."},
        {"name": "Chrome DevTools", "url": "https://developer.chrome.com/docs/devtools/", "description": "In-browser inspection and responsive debugging tools."},
    ],
}

BACKEND_RESOURCES = {
    "name": "Back-End Development",
    "domain": "web",
    "domain_name": "Web & Application Development",
    "youtube_channels": [
        {"name": "Corey Schafer", "url": "https://www.youtube.com/@coreyms", "description": "Authoritative Python, Flask, Django, SQL, and backend architecture tutorials."},
        {"name": "Hussein Nasser", "url": "https://www.youtube.com/@hnasr", "description": "Deep dives into backend engineering, databases, HTTP protocols, and system design."},
        {"name": "ArjanCodes", "url": "https://www.youtube.com/@ArjanCodes", "description": "Clean code architecture, OOP patterns, and Python backend best practices."},
        {"name": "freeCodeCamp.org", "url": "https://www.youtube.com/@freecodecamp", "description": "Full-length backend bootcamps covering Python, APIs, and databases."},
    ],
    "documentation": [
        {"name": "Flask Official Tutorial", "url": "https://flask.palletsprojects.com/en/stable/tutorial/", "description": "Official walkthrough for building database-driven Python backend apps."},
        {"name": "Python Official Tutorial", "url": "https://docs.python.org/3/tutorial/", "description": "Core Python programming concepts, data structures, and standard libraries."},
        {"name": "PostgreSQL Documentation", "url": "https://www.postgresql.org/docs/current/tutorial.html", "description": "Authoritative guide to relational databases, SQL queries, and indexing."},
        {"name": "MySQL Tutorial", "url": "https://dev.mysql.com/doc/refman/8.4/en/tutorial.html", "description": "SQL syntax, relational tables, and database operations for beginners."},
    ],
    "free_courses": [
        {"name": "CS50's Web Programming with Python and JavaScript", "url": "https://cs50.harvard.edu/web/", "description": "Harvard's acclaimed course on backend design, APIs, databases, and scalability."},
        {"name": "freeCodeCamp Relational Databases", "url": "https://www.freecodecamp.org/learn/relational-database/", "description": "Interactive Linux terminal and PostgreSQL course building real databases."},
        {"name": "IBM Full Stack Software Developer Certificate", "url": "https://www.coursera.org/professional-certificates/ibm-full-stack-cloud-developer", "description": "Covers Python backend, databases, APIs, and cloud microservices (free audit)."},
    ],
    "materials": [
        {"name": "Postman Learning Center", "url": "https://learning.postman.com/", "description": "Official guides for testing RESTful endpoints and API requests."},
        {"name": "SQLZoo Interactive Tutorials", "url": "https://sqlzoo.net/", "description": "Step-by-step SQL query exercises and database fundamentals."},
    ],
    "practice": [
        {"name": "SQLBolt", "url": "https://sqlbolt.com/", "description": "Interactive in-browser lessons for mastering SQL syntax and joins."},
        {"name": "HackerRank Python", "url": "https://www.hackerrank.com/domains/python", "description": "Algorithm and backend problem-solving challenges in Python."},
        {"name": "LeetCode Database", "url": "https://leetcode.com/problemset/database/", "description": "Real-world database querying problems."},
    ],
    "project_ideas": [
        "Student record & grade management REST API with JWT authentication",
        "Library book reservation backend with SQL relationships",
        "Secure notes application with password hashing and role-based access",
        "E-commerce product catalog and order processing API",
    ],
    "communities": [
        {"name": "Python Discord", "url": "https://pythondiscord.com/", "description": "Large community for backend and Python discussions."},
        {"name": "Reddit r/backend", "url": "https://www.reddit.com/r/backend/", "description": "Developer discussions on server architecture and APIs."},
    ],
    "tools": [
        {"name": "Postman", "url": "https://www.postman.com/", "description": "Essential tool for building and testing backend APIs."},
        {"name": "DBeaver", "url": "https://dbeaver.io/", "description": "Universal database client for managing SQLite, MySQL, and PostgreSQL."},
        {"name": "Visual Studio Code", "url": "https://code.visualstudio.com/", "description": "Code editor with rich Python and database extensions."},
    ],
}

FULLSTACK_RESOURCES = {
    "name": "Full-Stack Development",
    "domain": "web",
    "domain_name": "Web & Application Development",
    "youtube_channels": [
        {"name": "Traversy Media", "url": "https://www.youtube.com/@TraversyMedia", "description": "Full-stack project tutorials connecting frontend interfaces with backend databases."},
        {"name": "Dave Gray", "url": "https://www.youtube.com/@DaveGrayTeachesCode", "description": "Comprehensive full-stack web courses covering React, Node, Python, and APIs."},
        {"name": "PedroTech", "url": "https://www.youtube.com/@PedroTechnologies", "description": "Full-stack web application development walkthroughs and project builds."},
        {"name": "freeCodeCamp.org", "url": "https://www.youtube.com/@freecodecamp", "description": "End-to-end full-stack development courses and certification tracks."},
    ],
    "documentation": [
        {"name": "Full Stack Open", "url": "https://fullstackopen.com/en/", "description": "University of Helsinki's acclaimed curriculum for modern full-stack web apps."},
        {"name": "MDN Web Development", "url": "https://developer.mozilla.org/en-US/docs/Learn_web_development", "description": "Complete reference for web standards, client-side code, and servers."},
        {"name": "Flask Tutorial", "url": "https://flask.palletsprojects.com/en/stable/tutorial/", "description": "Official guide for connecting HTML templates to Python backend logic."},
    ],
    "free_courses": [
        {"name": "Full Stack Open", "url": "https://fullstackopen.com/en/", "description": "Free world-class curriculum covering frontend, backend, databases, and CI/CD."},
        {"name": "The Odin Project - Full Stack Ruby / JavaScript", "url": "https://www.theodinproject.com/", "description": "Project-based full-stack developer path from zero to full deployment."},
        {"name": "IBM Full Stack Software Developer Certificate", "url": "https://www.coursera.org/professional-certificates/ibm-full-stack-cloud-developer", "description": "End-to-end web developer path with Python, Flask, databases, and deployment."},
    ],
    "materials": [
        {"name": "GitHub Skills", "url": "https://skills.github.com/", "description": "Interactive tutorials for Git branching, pull requests, and collaboration."},
        {"name": "Postman Learning Center", "url": "https://learning.postman.com/", "description": "API design, debugging, and full-stack integration documentation."},
    ],
    "practice": [
        {"name": "Frontend Mentor Challenges", "url": "https://www.frontendmentor.io/challenges", "description": "Practice building multi-page web applications from design briefs."},
        {"name": "freeCodeCamp Full Stack Curriculum", "url": "https://www.freecodecamp.org/learn/", "description": "Interactive coding challenges with instant validation."},
        {"name": "GitHub Skills", "url": "https://skills.github.com/", "description": "Hands-on version control practice directly on GitHub."},
    ],
    "project_ideas": [
        "College placement portal connecting students with recruiters",
        "Student budget and expense tracking application with visual charts",
        "Campus club event management and ticketing platform",
        "Full-stack discussion forum with user authentication and voting",
    ],
    "communities": [
        {"name": "The Odin Project Community", "url": "https://www.theodinproject.com/community", "description": "Active peer community for full-stack learners."},
        {"name": "freeCodeCamp Forum", "url": "https://forum.freecodecamp.org/", "description": "Open global community for web development questions."},
    ],
    "tools": [
        {"name": "Visual Studio Code", "url": "https://code.visualstudio.com/", "description": "Industry-standard editor for full-stack coding."},
        {"name": "Git & GitHub", "url": "https://github.com/", "description": "Essential version control and code hosting platform."},
        {"name": "Postman", "url": "https://www.postman.com/", "description": "API testing and development workbench."},
    ],
}

DATA_SCIENCE_RESOURCES = {
    "name": "Data Science",
    "domain": "ai",
    "domain_name": "Data & Artificial Intelligence",
    "youtube_channels": [
        {"name": "StatQuest with Josh Starmer", "url": "https://www.youtube.com/@statquest", "description": "Visual, intuitive explanations of statistics, probability, and data science concepts."},
        {"name": "Data School", "url": "https://www.youtube.com/@DataSchool", "description": "Clear Python data analysis tutorials focusing on Pandas and exploratory analysis."},
        {"name": "Keith Galli", "url": "https://www.youtube.com/@KeithGalli", "description": "Hands-on real-world data analysis walkthroughs with Pandas and Matplotlib."},
        {"name": "Ken Jee", "url": "https://www.youtube.com/@KenJee_ds", "description": "Practical data science project portfolios and career advice for students."},
    ],
    "documentation": [
        {"name": "Pandas Getting Started", "url": "https://pandas.pydata.org/docs/getting_started/index.html", "description": "Official guide for data manipulation, filtering, and aggregation in Python."},
        {"name": "NumPy User Guide", "url": "https://numpy.org/doc/stable/user/", "description": "Official numerical computing documentation for array operations."},
        {"name": "Seaborn Documentation", "url": "https://seaborn.pydata.org/tutorial.html", "description": "Statistical data visualization library built on top of Matplotlib."},
        {"name": "Python for Data Analysis (Free Online Book)", "url": "https://wesmckinney.com/book/", "description": "Comprehensive reference written by the creator of Pandas."},
    ],
    "free_courses": [
        {"name": "Kaggle Learn - Pandas & Python", "url": "https://www.kaggle.com/learn/pandas", "description": "Free, hands-on micro-courses covering essential data manipulation."},
        {"name": "IBM SkillsBuild Data Science", "url": "https://skillsbuild.org/college-students/data-science", "description": "Foundational data science, visualization, and methodology course for students."},
        {"name": "freeCodeCamp Data Analysis with Python", "url": "https://www.freecodecamp.org/learn/data-analysis-with-python/", "description": "Interactive data analysis curriculum with certification projects."},
    ],
    "materials": [
        {"name": "Kaggle Data Visualization Course", "url": "https://www.kaggle.com/learn/data-visualization", "description": "Hands-on guides to creating effective statistical charts with Seaborn."},
        {"name": "Python Data Science Handbook", "url": "https://jakevdp.github.io/PythonDataScienceHandbook/", "description": "Free digital book covering NumPy, Pandas, Matplotlib, and Scikit-Learn."},
    ],
    "practice": [
        {"name": "Kaggle Datasets", "url": "https://www.kaggle.com/datasets", "description": "Thousands of real-world datasets for exploratory data analysis projects."},
        {"name": "Google Colab", "url": "https://colab.research.google.com/", "description": "Free cloud Jupyter notebooks with zero local configuration required."},
        {"name": "SQLBolt", "url": "https://sqlbolt.com/", "description": "Interactive SQL practice essential for data science querying."},
    ],
    "project_ideas": [
        "Student academic performance & attendance analytics dashboard",
        "E-commerce customer buying trends & churn exploratory data analysis",
        "IPL / Sports match statistics and player performance insight report",
        "Global weather & climate patterns visualization dashboard",
    ],
    "communities": [
        {"name": "Kaggle Discussions", "url": "https://www.kaggle.com/discussions", "description": "Global hub for sharing data notebooks and seeking analysis advice."},
        {"name": "Reddit r/datascience", "url": "https://www.reddit.com/r/datascience/", "description": "Community of practicing data scientists and learners."},
    ],
    "tools": [
        {"name": "Jupyter Notebook", "url": "https://jupyter.org/", "description": "Interactive computing environment for Python data analysis."},
        {"name": "Google Colab", "url": "https://colab.research.google.com/", "description": "Cloud-hosted Jupyter notebook service with free hardware acceleration."},
        {"name": "Pandas & Matplotlib", "url": "https://pandas.pydata.org/", "description": "Core Python libraries for tabular data processing and plotting."},
    ],
}

ML_RESOURCES = {
    "name": "Machine Learning",
    "domain": "ai",
    "domain_name": "Data & Artificial Intelligence",
    "youtube_channels": [
        {"name": "StatQuest with Josh Starmer", "url": "https://www.youtube.com/@statquest", "description": "Crystal-clear visual walkthroughs of ML algorithms, trees, and neural networks."},
        {"name": "3Blue1Brown", "url": "https://www.youtube.com/@3blue1brown", "description": "Intuitive visual animations explaining linear algebra, calculus, and deep learning."},
        {"name": "Sentdex", "url": "https://www.youtube.com/@sentdex", "description": "Practical Python machine learning and neural network implementations from scratch."},
        {"name": "Krish Naik", "url": "https://www.youtube.com/@krishnaik06", "description": "End-to-end machine learning project tutorials and industry workflows."},
    ],
    "documentation": [
        {"name": "Google Machine Learning Crash Course", "url": "https://developers.google.com/machine-learning/crash-course", "description": "Interactive curriculum with short videos, real-world case studies, and TensorFlow exercises."},
        {"name": "scikit-learn Official User Guide", "url": "https://scikit-learn.org/stable/user_guide.html", "description": "Authoritative guide to classification, regression, clustering, and model validation."},
        {"name": "PyTorch Getting Started Tutorials", "url": "https://pytorch.org/tutorials/", "description": "Official guides for deep learning, tensors, and neural network training."},
    ],
    "free_courses": [
        {"name": "Google Machine Learning Crash Course", "url": "https://developers.google.com/machine-learning/crash-course", "description": "Free beginner ML course with interactive exercises and visualizations."},
        {"name": "Kaggle Intro to Machine Learning", "url": "https://www.kaggle.com/learn/intro-to-machine-learning", "description": "Build your first ML models using Scikit-Learn in just a few hours."},
        {"name": "fast.ai Practical Deep Learning for Coders", "url": "https://course.fast.ai/", "description": "Top-down, practical deep learning course designed for coders."},
    ],
    "materials": [
        {"name": "Google ML Crash Course Exercises", "url": "https://developers.google.com/machine-learning/crash-course/exercises", "description": "Hands-on coding exercises reinforcing model training and loss evaluation."},
        {"name": "Kaggle Intermediate Machine Learning", "url": "https://www.kaggle.com/learn/intermediate-machine-learning", "description": "Handling missing values, categorical variables, and XGBoost."},
    ],
    "practice": [
        {"name": "Kaggle Titanic Machine Learning Competition", "url": "https://www.kaggle.com/c/titanic", "description": "The quintessential first machine learning competition for beginners."},
        {"name": "Kaggle Housing Prices Prediction", "url": "https://www.kaggle.com/c/house-prices-advanced-regression-techniques", "description": "Practice feature engineering and regression techniques."},
        {"name": "Google Colab", "url": "https://colab.research.google.com/", "description": "Free GPU-enabled notebooks for training machine learning models."},
    ],
    "project_ideas": [
        "Real estate house price prediction model using regression",
        "SMS spam and email phishing classifier using NLP text processing",
        "Cardiovascular disease risk predictor based on patient health metrics",
        "Handwritten digit classification using convolutional neural networks",
    ],
    "communities": [
        {"name": "Kaggle Discussions", "url": "https://www.kaggle.com/discussions", "description": "Share model architectures and learn from competition grandmasters."},
        {"name": "Hugging Face Community", "url": "https://huggingface.co/", "description": "Hub for exploring, sharing, and deploying state-of-the-art ML models."},
    ],
    "tools": [
        {"name": "scikit-learn", "url": "https://scikit-learn.org/", "description": "Premier Python library for classical machine learning algorithms."},
        {"name": "Google Colab", "url": "https://colab.research.google.com/", "description": "Cloud development environment with free GPU access."},
        {"name": "Jupyter", "url": "https://jupyter.org/", "description": "Interactive notebook environment for training and experimenting."},
    ],
}

DATA_ENGINEERING_RESOURCES = {
    "name": "Data Engineering",
    "domain": "ai",
    "domain_name": "Data & Artificial Intelligence",
    "youtube_channels": [
        {"name": "Seattle Data Guy", "url": "https://www.youtube.com/@SeattleDataGuy", "description": "Data engineering roadmaps, architectures, ETL pipelines, and SQL best practices."},
        {"name": "Andreas Kretz", "url": "https://www.youtube.com/@AndreasKretz", "description": "Hands-on data engineering tutorials covering Spark, Kafka, and big data architecture."},
        {"name": "Darshil Parmar", "url": "https://www.youtube.com/@DarshilParmar", "description": "End-to-end cloud data engineering projects with real-time data ingestion."},
        {"name": "freeCodeCamp.org", "url": "https://www.youtube.com/@freecodecamp", "description": "Comprehensive full courses on database design and data pipelines."},
    ],
    "documentation": [
        {"name": "PostgreSQL Documentation", "url": "https://www.postgresql.org/docs/current/tutorial.html", "description": "Official relational database tutorial and schema design reference."},
        {"name": "Apache Airflow Documentation", "url": "https://airflow.apache.org/docs/", "description": "Official guide for orchestrating complex data workflows and DAGs."},
        {"name": "Apache Spark Documentation", "url": "https://spark.apache.org/docs/latest/", "description": "Authoritative documentation for large-scale distributed data processing."},
        {"name": "dbt (Data Build Tool) Documentation", "url": "https://docs.getdbt.com/", "description": "Modern data transformation and modeling in cloud data warehouses."},
    ],
    "free_courses": [
        {"name": "Data Engineering Zoomcamp", "url": "https://github.com/DataTalksClub/data-engineering-zoomcamp", "description": "Free, comprehensive cohort-based course covering Docker, SQL, Airflow, Spark, and dbt."},
        {"name": "Kaggle Learn - Data Cleaning", "url": "https://www.kaggle.com/learn/data-cleaning", "description": "Practical workflows for handling missing values and inconsistent data."},
        {"name": "IBM SkillsBuild Data Engineering", "url": "https://skillsbuild.org/college-students", "description": "Free enterprise-aligned data pipeline and database fundamentals."},
    ],
    "materials": [
        {"name": "Docker Get Started Guide", "url": "https://docs.docker.com/get-started/", "description": "Essential container fundamentals for standing up databases and ETL services."},
        {"name": "SQLBolt Interactive Lessons", "url": "https://sqlbolt.com/", "description": "Practical exercises on queries, aggregate functions, and table constraints."},
    ],
    "practice": [
        {"name": "SQLBolt", "url": "https://sqlbolt.com/", "description": "Interactive SQL query lessons with real-time feedback."},
        {"name": "LeetCode Database Problem Set", "url": "https://leetcode.com/problemset/database/", "description": "Challenging SQL schema and join problems."},
        {"name": "Killercoda Linux & Docker Labs", "url": "https://killercoda.com/", "description": "Browser-based environments for deploying databases and pipelines."},
    ],
    "project_ideas": [
        "Automated weather API data extraction, transformation, and PostgreSQL loading pipeline",
        "Batch CSV/JSON ingestion pipeline with automated data validation and error logging",
        "Airflow DAG scheduled to fetch and store daily financial market data",
        "Spotify / YouTube API data pipeline loading analytics into a warehouse",
    ],
    "communities": [
        {"name": "DataTalks.Club", "url": "https://datatalks.club/", "description": "Vibrant global community of data engineers and learners."},
        {"name": "Reddit r/dataengineering", "url": "https://www.reddit.com/r/dataengineering/", "description": "Active community discussing pipelines, tooling, and best practices."},
    ],
    "tools": [
        {"name": "PostgreSQL", "url": "https://www.postgresql.org/", "description": "Powerful open-source object-relational database system."},
        {"name": "Apache Airflow", "url": "https://airflow.apache.org/", "description": "Industry-standard platform to programmatically author and schedule workflows."},
        {"name": "Docker", "url": "https://www.docker.com/", "description": "Essential tool for containerizing databases and data pipelines."},
    ],
}

CLOUD_RESOURCES = {
    "name": "Cloud Engineering",
    "domain": "systems",
    "domain_name": "Systems & Infrastructure",
    "youtube_channels": [
        {"name": "AWS Training and Certification", "url": "https://www.youtube.com/@AWSTraining", "description": "Official AWS cloud training, architecture walkthroughs, and certifications."},
        {"name": "TechWorld with Nana", "url": "https://www.youtube.com/@TechWorldwithNana", "description": "Visual, intuitive explainers for cloud computing, containers, and infrastructure."},
        {"name": "Digital Cloud Training", "url": "https://www.youtube.com/@DigitalCloudTraining", "description": "Practical cloud architecture walkthroughs and exam preparation."},
        {"name": "freeCodeCamp.org", "url": "https://www.youtube.com/@freecodecamp", "description": "Full-length AWS and Azure cloud certification training videos."},
    ],
    "documentation": [
        {"name": "AWS Skill Builder", "url": "https://skillbuilder.aws/", "description": "Free official learning center from AWS with self-paced digital courses."},
        {"name": "Microsoft Learn Azure", "url": "https://learn.microsoft.com/en-us/training/azure/", "description": "Structured, free interactive learning paths for Microsoft Azure cloud."},
        {"name": "AWS Architecture Center", "url": "https://aws.amazon.com/architecture/", "description": "Reference architectures and cloud best practices for scalable systems."},
    ],
    "free_courses": [
        {"name": "AWS Cloud Practitioner Essentials", "url": "https://explore.skillbuilder.aws/learn/course/external/view/elearning/134/aws-cloud-practitioner-essentials", "description": "Free official introductory course covering fundamental AWS cloud concepts."},
        {"name": "Microsoft Learn Azure Fundamentals (AZ-900)", "url": "https://learn.microsoft.com/en-us/training/paths/microsoft-azure-fundamentals-describe-cloud-concepts/", "description": "Free beginner Azure curriculum covering compute, networking, and storage."},
        {"name": "Linux Journey", "url": "https://linuxjourney.com/", "description": "Free interactive Linux command-line tutorial essential for cloud servers."},
    ],
    "materials": [
        {"name": "Google Cloud Architecture Framework", "url": "https://cloud.google.com/architecture/framework", "description": "Best practices for building reliable and cost-effective cloud workloads."},
        {"name": "Docker Get Started Guide", "url": "https://docs.docker.com/get-started/", "description": "Foundational container guide essential for cloud microservices."},
    ],
    "practice": [
        {"name": "AWS Free Tier", "url": "https://aws.amazon.com/free/", "description": "Free cloud tier providing 12 months of hands-on practice with EC2, S3, and Lambda."},
        {"name": "Killercoda Linux & Cloud Labs", "url": "https://killercoda.com/", "description": "Free browser-based sandbox environments for cloud practice."},
        {"name": "Play with Docker", "url": "https://labs.play-with-docker.com/", "description": "Interactive in-browser container playground."},
    ],
    "project_ideas": [
        "Host and deploy a secure static website on Amazon S3 with CloudFront CDN",
        "Deploy a containerized Flask application on AWS EC2 or App Runner",
        "Build a serverless image processing pipeline using AWS Lambda and S3 triggers",
        "Automated cloud backup and storage lifecycle management script",
    ],
    "communities": [
        {"name": "AWS Community", "url": "https://community.aws/", "description": "Global hub for sharing AWS architectures and connecting with peers."},
        {"name": "Reddit r/cloudcomputing", "url": "https://www.reddit.com/r/cloudcomputing/", "description": "Discussions on cloud platforms, infrastructure, and careers."},
    ],
    "tools": [
        {"name": "AWS Console & CLI", "url": "https://aws.amazon.com/cli/", "description": "Command-line interface for managing cloud services."},
        {"name": "Terraform", "url": "https://www.terraform.io/", "description": "Leading Infrastructure as Code tool for automating cloud deployments."},
        {"name": "Docker", "url": "https://www.docker.com/", "description": "Platform for building and packaging cloud-native containers."},
    ],
}

DEVOPS_RESOURCES = {
    "name": "DevOps Engineering",
    "domain": "systems",
    "domain_name": "Systems & Infrastructure",
    "youtube_channels": [
        {"name": "TechWorld with Nana", "url": "https://www.youtube.com/@TechWorldwithNana", "description": "The premier channel for Docker, Kubernetes, CI/CD, Terraform, and DevOps culture."},
        {"name": "NetworkChuck", "url": "https://www.youtube.com/@NetworkChuck", "description": "Engaging, beginner-friendly tutorials on Linux, networking, Docker, and Git."},
        {"name": "Kunal Kushwaha", "url": "https://www.youtube.com/@KunalKushwaha", "description": "Free comprehensive DevOps bootcamp covering Linux, Git, Docker, and CI/CD."},
        {"name": "Christian Lempa", "url": "https://www.youtube.com/@ChristianLempa", "description": "Practical guides on home servers, Linux, automation, and infrastructure."},
    ],
    "documentation": [
        {"name": "Docker Documentation", "url": "https://docs.docker.com/get-started/", "description": "Official containerization reference and step-by-step guides."},
        {"name": "Kubernetes Documentation", "url": "https://kubernetes.io/docs/home/", "description": "Official tutorials for container orchestration, pods, and deployments."},
        {"name": "GitHub Actions Documentation", "url": "https://docs.github.com/en/actions", "description": "Authoritative guide to building automated CI/CD pipelines."},
        {"name": "Linux Documentation Project", "url": "https://tldp.org/", "description": "Guides and references for the Linux operating system and shell scripting."},
    ],
    "free_courses": [
        {"name": "Kunal Kushwaha DevOps Bootcamp", "url": "https://www.techwithkunal.com/courses/devops", "description": "Free, open-source DevOps bootcamp from zero to production deployments."},
        {"name": "Microsoft Learn - Develop with DevOps", "url": "https://learn.microsoft.com/en-us/training/modules/develop-with-devops/", "description": "Free beginner module on Git, CI/CD, and automated workflows."},
        {"name": "Linux Journey", "url": "https://linuxjourney.com/", "description": "Interactive Linux command-line tutorial from basics to networking."},
    ],
    "materials": [
        {"name": "Kubernetes Basics Interactive Tutorial", "url": "https://kubernetes.io/docs/tutorials/kubernetes-basics/", "description": "Official interactive walkthrough of cluster deployment and service routing."},
        {"name": "Docker Workshop", "url": "https://docs.docker.com/get-started/workshop/", "description": "Hands-on multi-container application workshop."},
    ],
    "practice": [
        {"name": "Killercoda", "url": "https://killercoda.com/", "description": "Free interactive Linux, Docker, and Kubernetes labs right in your browser."},
        {"name": "Play with Docker", "url": "https://labs.play-with-docker.com/", "description": "In-browser terminal for building and testing Docker containers."},
        {"name": "Play with Kubernetes", "url": "https://labs.play-with-k8s.com/", "description": "In-browser multi-node Kubernetes cluster playground."},
    ],
    "project_ideas": [
        "Dockerize a full-stack web application (Flask + MySQL + Nginx)",
        "Build a GitHub Actions CI/CD pipeline that runs automated tests and pushes Docker images",
        "Deploy a containerized application to Kubernetes with rolling updates and auto-healing",
        "Linux server health & uptime monitoring script with automated Discord/Slack alerts",
    ],
    "communities": [
        {"name": "Kubernetes Community", "url": "https://www.kubernetes.dev/", "description": "Global open-source community around cloud-native infrastructure."},
        {"name": "DevOps Directive Community", "url": "https://devopsdirective.com/", "description": "Practical discussions on DevOps tools, career paths, and automation."},
    ],
    "tools": [
        {"name": "Docker", "url": "https://www.docker.com/", "description": "Essential platform for packaging and shipping applications in containers."},
        {"name": "GitHub Actions", "url": "https://github.com/features/actions", "description": "Built-in CI/CD automation workflow engine in GitHub."},
        {"name": "Kubernetes", "url": "https://kubernetes.io/", "description": "Industry-standard container orchestration platform."},
    ],
}

EMBEDDED_RESOURCES = {
    "name": "Embedded Systems",
    "domain": "systems",
    "domain_name": "Systems & Infrastructure",
    "youtube_channels": [
        {"name": "Ben Eater", "url": "https://www.youtube.com/@BenEater", "description": "Masterclasses on computer architecture, 8-bit computers on breadboards, and digital logic."},
        {"name": "DroneBot Workshop", "url": "https://www.youtube.com/@Dronebotworkshop", "description": "Practical tutorials on Arduino, ESP32, sensors, motors, and robotics."},
        {"name": "Phil's Lab", "url": "https://www.youtube.com/@PhilsLab", "description": "PCB design, STM32 microcontroller firmware, and embedded C programming."},
        {"name": "GreatScott!", "url": "https://www.youtube.com/@greatscottlab", "description": "Engaging electronics projects, circuit testing, and microcontroller hardware."},
    ],
    "documentation": [
        {"name": "Arduino Documentation & Learn", "url": "https://docs.arduino.cc/learn", "description": "Official guides for microcontroller hardware, pinouts, and C++ sketch development."},
        {"name": "Raspberry Pi Documentation", "url": "https://www.raspberrypi.com/documentation/", "description": "Official guides for single-board computers, Linux OS, and GPIO control."},
        {"name": "ESP32 Technical Documentation", "url": "https://docs.espressif.com/projects/esp-idf/en/latest/esp32/", "description": "Official documentation for ESP32 Wi-Fi & Bluetooth microcontrollers."},
        {"name": "C Programming Language Reference", "url": "https://en.cppreference.com/w/c", "description": "Standard C language reference essential for firmware development."},
    ],
    "free_courses": [
        {"name": "Arduino Official Built-in Examples", "url": "https://docs.arduino.cc/built-in-examples/", "description": "Hands-on interactive examples for learning digital I/O, analog read, and PWM."},
        {"name": "All About Circuits - Embedded Systems", "url": "https://www.allaboutcircuits.com/", "description": "Comprehensive free educational textbook on circuits, microcontrollers, and logic."},
        {"name": "edX Microcontroller Foundations", "url": "https://www.edx.org/", "description": "Academic introductory curriculum for embedded systems and computer architecture."},
    ],
    "materials": [
        {"name": "Arduino Language Reference", "url": "https://docs.arduino.cc/language-reference/", "description": "Syntax and function reference for Arduino C++ programming."},
        {"name": "Digital Logic & Circuit Basics", "url": "https://www.allaboutcircuits.com/textbook/digital/", "description": "Free textbook covering binary, logic gates, and microcontroller internals."},
    ],
    "practice": [
        {"name": "Wokwi Online Simulator", "url": "https://wokwi.com/", "description": "Browser-based Arduino, ESP32, and Raspberry Pi Pico electronics simulator."},
        {"name": "Tinkercad Circuits", "url": "https://www.tinkercad.com/circuits", "description": "Interactive visual breadboard simulation for beginners to test code safely."},
        {"name": "Exercism C Track", "url": "https://exercism.org/tracks/c", "description": "Structured C programming exercises to build solid low-level coding skills."},
    ],
    "project_ideas": [
        "Temperature & humidity monitoring alert system with an LCD display and buzzer",
        "Smart automated plant watering system using soil moisture sensors",
        "Ultrasonic distance sensor obstacle-avoiding mini robot",
        "Home automation smart light controller using ESP32 and Wi-Fi",
    ],
    "communities": [
        {"name": "Arduino Forum", "url": "https://forum.arduino.cc/", "description": "Large community for microcontroller hardware and code troubleshooting."},
        {"name": "Reddit r/embedded", "url": "https://www.reddit.com/r/embedded/", "description": "Discussions with practicing firmware engineers and embedded developers."},
    ],
    "tools": [
        {"name": "Arduino IDE", "url": "https://www.arduino.cc/en/software", "description": "Beginner-friendly environment for writing and flashing microcontroller code."},
        {"name": "Wokwi Simulator", "url": "https://wokwi.com/", "description": "Browser-based electronics simulation tool with live coding."},
        {"name": "PlatformIO", "url": "https://platformio.org/", "description": "Professional cross-platform IDE for embedded C/C++ development."},
    ],
}

QA_RESOURCES = {
    "name": "QA Testing",
    "domain": "security",
    "domain_name": "Quality & Security",
    "youtube_channels": [
        {"name": "SDET- QA Automation Techie", "url": "https://www.youtube.com/@sdetQA", "description": "Comprehensive tutorials on Selenium, API testing, Postman, and testing frameworks."},
        {"name": "The Testing Academy", "url": "https://www.youtube.com/@TheTestingAcademy", "description": "Manual testing, test case design, automation roadmaps, and career advice."},
        {"name": "Automation Step by Step", "url": "https://www.youtube.com/@raghavpal", "description": "Beginner-friendly step-by-step tutorials on testing tools and automation."},
        {"name": "freeCodeCamp.org", "url": "https://www.youtube.com/@freecodecamp", "description": "Full-length bootcamps covering software testing and quality assurance."},
    ],
    "documentation": [
        {"name": "Selenium Documentation", "url": "https://www.selenium.dev/documentation/", "description": "Official guide for browser automation testing with Python and JavaScript."},
        {"name": "Postman Learning Center", "url": "https://learning.postman.com/", "description": "Official guides for automated API test scripts, collections, and assertions."},
        {"name": "Playwright Documentation", "url": "https://playwright.dev/docs/intro", "description": "Modern end-to-end web testing framework with multi-browser support."},
        {"name": "ISTQB Glossary of Testing Terms", "url": "https://glossary.istqb.org/", "description": "Standard international terminology for software testing and QA."},
    ],
    "free_courses": [
        {"name": "Test Automation University", "url": "https://testautomationu.applitools.com/", "description": "Free world-class courses on test automation, Selenium, API testing, and frameworks."},
        {"name": "Guru99 Software Testing Fundamentals", "url": "https://www.guru99.com/software-testing.html", "description": "Comprehensive manual testing basics, SDLC, STLC, and test case writing."},
        {"name": "Postman API Testing Student Program", "url": "https://www.postman.com/student-program/", "description": "Free hands-on student certification path in API testing."},
    ],
    "materials": [
        {"name": "Selenium Python Documentation", "url": "https://selenium-python.readthedocs.io/", "description": "Complete guide to writing browser test scripts with Python."},
        {"name": "Software Testing Help Test Case Guide", "url": "https://www.softwaretestinghelp.com/how-to-write-test-cases-with-examples/", "description": "Templates and examples for writing industry-standard test cases."},
    ],
    "practice": [
        {"name": "The Internet Test Site (Herokuapp)", "url": "https://the-internet.herokuapp.com/", "description": "Purpose-built test site with common UI scenarios (dropdowns, auth, dynamic loading)."},
        {"name": "Automation Exercise", "url": "https://automationexercise.com/", "description": "Full e-commerce website designed for end-to-end test automation practice."},
        {"name": "Restful-Booker API", "url": "https://restful-booker.herokuapp.com/", "description": "Practice API created specifically for exercising CRUD automated API tests."},
    ],
    "project_ideas": [
        "Comprehensive manual test plan & bug report suite for an e-commerce website",
        "Automated end-to-end regression test suite using Selenium with Python and PyTest",
        "Automated Postman API test collection with Newman CLI report generation",
        "Cross-browser login and checkout validation suite with HTML execution reports",
    ],
    "communities": [
        {"name": "Ministry of Testing Club", "url": "https://club.ministryoftesting.com/", "description": "Global community of passionate software testers and QA professionals."},
        {"name": "Reddit r/qualityassurance", "url": "https://www.reddit.com/r/qualityassurance/", "description": "Discussions on test automation, tooling, and best practices."},
    ],
    "tools": [
        {"name": "Selenium WebDriver", "url": "https://www.selenium.dev/", "description": "Industry-standard browser automation testing framework."},
        {"name": "Postman", "url": "https://www.postman.com/", "description": "Essential tool for API exploration and automated testing."},
        {"name": "Playwright", "url": "https://playwright.dev/", "description": "Fast and reliable modern end-to-end web testing framework."},
    ],
}

CYBERSECURITY_RESOURCES = {
    "name": "Cybersecurity",
    "domain": "security",
    "domain_name": "Quality & Security",
    "youtube_channels": [
        {"name": "Professor Messer", "url": "https://www.youtube.com/@professormesser", "description": "High-yield Security+ certification, network protocols, cryptography, and defense concepts."},
        {"name": "John Hammond", "url": "https://www.youtube.com/@_JohnHammond", "description": "Hands-on CTF walkthroughs, malware analysis, ethical hacking, and cyber threat labs."},
        {"name": "NetworkChuck", "url": "https://www.youtube.com/@NetworkChuck", "description": "Entertaining, hands-on tutorials on hacking labs, Wireshark, Linux, and security basics."},
        {"name": "David Bombal", "url": "https://www.youtube.com/@DavidBombal", "description": "Practical networking, Wireshark packet analysis, and ethical hacking tutorials."},
    ],
    "documentation": [
        {"name": "OWASP Web Security Testing Guide", "url": "https://owasp.org/www-project-web-security-testing-guide/", "description": "Authoritative guide to testing and preventing web application vulnerabilities."},
        {"name": "Cisco Networking Academy", "url": "https://www.netacad.com/", "description": "Official networking fundamentals and security learning pathways."},
        {"name": "CISA Cyber Careers & Pathways", "url": "https://www.cisa.gov/cyber-careers-pathways-tool", "description": "Official career roadmap for cybersecurity analyst and engineering roles."},
        {"name": "Wireshark User Guide", "url": "https://www.wireshark.org/docs/wsug_html_chunked/", "description": "Official reference for network packet capture and protocol analysis."},
    ],
    "free_courses": [
        {"name": "Cisco Introduction to Cybersecurity", "url": "https://www.netacad.com/courses/cybersecurity/introduction-to-cybersecurity", "description": "Free beginner cybersecurity course from Cisco Networking Academy."},
        {"name": "Fortinet Training Institute Security Fundamentals", "url": "https://training.fortinet.com/", "description": "Free industry-aligned security fundamentals and threat landscape training."},
        {"name": "Professor Messer CompTIA Security+ Training", "url": "https://www.youtube.com/@professormesser", "description": "Complete free video course on cybersecurity principles, encryption, and defense."},
        {"name": "TryHackMe Pre-Security Learning Path", "url": "https://tryhackme.com/path/outline/presecurity", "description": "Guided hands-on labs covering networking, web security, and Linux basics."},
    ],
    "materials": [
        {"name": "OWASP Top 10 Security Risks", "url": "https://owasp.org/www-project-top-ten/", "description": "Standard awareness document for web application security vulnerabilities."},
        {"name": "Professor Messer Security+ Course Notes", "url": "https://www.professormesser.com/security-plus/sy0-701/sy0-701-course-notes/", "description": "Free security fundamentals study notes."},
    ],
    "practice": [
        {"name": "TryHackMe", "url": "https://tryhackme.com/paths", "description": "Gamified browser-based cybersecurity labs for safe, legal hands-on practice."},
        {"name": "OverTheWire Bandit Wargame", "url": "https://overthewire.org/wargames/bandit/", "description": "Beginner-friendly terminal security wargame teaching Linux and permissions."},
        {"name": "OWASP Juice Shop", "url": "https://owasp.org/www-project-juice-shop/", "description": "Intentionally vulnerable modern web application for security practice."},
    ],
    "project_ideas": [
        "Web application security audit & hardening checklist for a Flask app",
        "Network traffic capture and malicious payload analysis report using Wireshark",
        "Automated password strength evaluator and hash identifier script in Python",
        "Port scanning and open port report generator script using Nmap and Python",
    ],
    "communities": [
        {"name": "OWASP Community", "url": "https://owasp.org/", "description": "Worldwide open community for software security awareness."},
        {"name": "TryHackMe Community", "url": "https://tryhackme.com/", "description": "Active community of cybersecurity learners and study groups."},
    ],
    "tools": [
        {"name": "Wireshark", "url": "https://www.wireshark.org/", "description": "World's foremost network protocol analyzer."},
        {"name": "Nmap", "url": "https://nmap.org/", "description": "Essential network exploration and security auditing tool."},
        {"name": "OWASP ZAP", "url": "https://www.zaproxy.org/", "description": "Free open-source web application security vulnerability scanner."},
    ],
}

# Unified Specialization Mapping
SPECIALIZATION_RESOURCES = {
    "frontend": FRONTEND_RESOURCES,
    "backend": BACKEND_RESOURCES,
    "fullstack": FULLSTACK_RESOURCES,
    "data_science": DATA_SCIENCE_RESOURCES,
    "machine_learning": ML_RESOURCES,
    "data_engineering": DATA_ENGINEERING_RESOURCES,
    "cloud": CLOUD_RESOURCES,
    "devops": DEVOPS_RESOURCES,
    "embedded": EMBEDDED_RESOURCES,
    "qa": QA_RESOURCES,
    "cybersecurity": CYBERSECURITY_RESOURCES,
}

# Domain-level fallbacks / references
WEB_RESOURCE_HUB = FRONTEND_RESOURCES
AI_RESOURCE_HUB = DATA_SCIENCE_RESOURCES
SYSTEMS_RESOURCE_HUB = CLOUD_RESOURCES
SECURITY_RESOURCE_HUB = CYBERSECURITY_RESOURCES

YOUTUBE_CHANNELS = FRONTEND_RESOURCES["youtube_channels"]

RESOURCE_COLLECTION_DOMAINS = {
    "web": {
        "name": "Web & Application Development",
        "description": "Resources for frontend, backend, and full-stack web development.",
        "focus_areas": ["Frontend", "Backend", "Full-Stack", "APIs", "Databases"],
    },
    "ai": {
        "name": "Data & Artificial Intelligence",
        "description": "Resources for data science, machine learning, AI, and data engineering.",
        "focus_areas": ["Data Science", "Machine Learning", "AI", "Data Engineering"],
    },
    "systems": {
        "name": "Systems & Infrastructure",
        "description": "Resources for cloud, DevOps, networking, and embedded systems.",
        "focus_areas": ["Cloud", "DevOps", "Networking", "Linux", "Embedded Systems"],
    },
    "security": {
        "name": "Quality & Security",
        "description": "Resources for software testing, quality assurance, and cybersecurity.",
        "focus_areas": ["QA Testing", "Automation Testing", "Cybersecurity", "Web Security"],
    },
}
