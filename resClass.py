from forResume import allPrompts, allPrompts2

class Prompt():
    def __init__(self, val):
        self.val = val
        
promptList = [line.split(']')[1].strip() for line in allPrompts2.split('\n') if ']' in line]

promptArr = []
for prompt in promptList:
    promptArr.append(prompt)


class Project7:
    def __init__(self, title, date, bullet1, bullet2, bullet3, description):
        self.title = title
        self.date = date
        self.bullet1 = bullet1
        self.bullet2 = bullet2
        self.bullet3 = bullet3
        self.description = description

    def __str__(self):
        return f"Title: {self.title}"

sevenLineProjects = []

sevenLineProjects.append(
    Project7(
        "Discord Bot (Javascript w/ discord.js and PostgreSQL)         		                      ",
        "Apr. 2023 - May. 2023",
        "Developed a feature-rich Discord bot with numerous slash commands, including several that interacted with various sports tracking APIs and a PostgreSQL database.",
        "Constructed a reminder command enabling users to set reminders and receive notifications leading up to the scheduled time.",
        "Conducted extensive backend testing using JestJS, executing over 20 tests to ensure optimal performance and functionality.",
        "A feature-rich Discord bot was developed, equipped with sports tracking APIs, a PostgreSQL database, and a reminder command, backed by comprehensive backend testing using JestJS.",
    )
)

sevenLineProjects.append(
    Project7(
        "Virtual Pharmacy (Java w/ Servlets, Docker, Kuberneates, MySQL)                         ",
        "Feb 2023 - Apr 2023",
        "Built a pharmacy website using microservice architecture, REST API, Java servlets, and MySQL database on an Apache Tomcat Server. Enabled users to browse, purchase and access information on medicines, while ensuring secure authentication with JSON web tokens.",
        "Utilized Docker, Kubernetes, and Google Cloud for containerizing microservices, orchestrating microservices, and deploying microservices.",
        "Implemented messaging (async and sync) with Kubernetes Queues.",
        "Built a secure pharmacy website with microservices, REST API, Java servlets, and MySQL, utilizing Docker, Kubernetes, and Google Cloud for deployment, while implementing async/sync messaging with Kubernetes Queues.",
    )
)
sevenLineProjects.append(
    Project7(
        "Blogging Platform (MERN Stack w/ fly.io and CypressJS)			        ",
        "Sep 2022 - Oct 2022",
        "Created and deployed a fully functional full-stack blog website with MongoDB database integration and fly.io deployment, enabling users to create, like, and comment on blogs. Incorporated Material UI to elevate the website design, ensuring a seamless user interface.",
        "Implemented advanced email authentication using nodemailer and json web tokens to enhance the website's security and user registration process.",
        "Utilized Cypress for comprehensive E2E testing, ensuring proper functionality across the stack.",
        "Developed a secure full-stack blog website with MongoDB integration, advanced email authentication, and comprehensive testing using Cypress. Website allowed users to like, comment, create and delete blogs.",
    )
)
sevenLineProjects.append(
    Project7(
        "Digital Bookstore (Java w/ JavaFX)						        ",
        "Apr 2022 - May 2022",
        "Developed a robust bookstore application with Java and JavaFX, offering users the ability to add books to their cart and purchase them at discounted rates via a point-based rewards system(Ex. Walmart Rewards).",
        "Implemented a session-save feature that saved each user's data after logging out.",
        "Utilized UML diagrams to facilitate a clear visualization of the project's components and screen flow, prior to implementation.",
        "Built a Java-based bookstore app with JavaFX, featuring cart functionality, discounted purchases through a rewards system, and UML diagrams for visual planning.",
    )
)

sevenLineProjects.append(
    Project7(
        "Quiz App (Swift)						          			         ",
        "Jul 2021 - Aug 2021",
        "Created a quiz app using Swift where users were given indicative feedback based on answer correctness. Also tracked and ranked user’s scores using Cloudkit.",
        "Implemented push notification feature using Apple Push Notification service (APNs) to send daily quiz reminders and updates to users, encouraging regular engagement with the app. Also incorporated social sharing using the Social framework.",
        "Utilized Core Animation and UIKit Dynamics for interactive visuals.",
        "Developed a Swift quiz app with indicative feedback, CloudKit for score tracking, APNs for push notifications, and interactive visuals with Core Animation and UIKit Dynamics.",
    )
)

sevenLineProjects.append(
    Project7(
        "Tailored Resume/Cover Letter Automator (Python w/ python-docx and rich)            ",
        "May. 2023 - Jun. 2023",
        "Created an engaging and user-friendly CLI tool using Python to effortlessly generate professional tailored resumes and cover letters based on individual preferences.",
        "By simply inputting project and qualification numbers, users can effortlessly select the most relevant projects and qualifications to highlight, without the need for manual content creation.",
        "The tool simplifies cover letter creation by prompting users for introductory sentences, job title, and company name, ensuring a personalized touch. Fun Fact: This resume was created using the tool!",
        "Developed a Python CLI tool for generating personalized resumes and cover letters. Input project and qualification numbers to highlight relevant experience. Streamlines cover letter creation with personalized prompts.",
    )
)

sevenLineProjects.append(
    Project7(
        "Quizzer App (PERN Stack)								        ",
        "Apr 2023 - May 2023",
        "Developed an interactive m/c quiz website resembling QuizUp using the PERN stack, allowing users to select quiz topics like Medical and General knowledge.",
        "Implemented timed questions with scoring based on response speed, utilizing a PostgreSQL database with 300+ questions.",
        "Utilized Figma for meticulous design and integrated interactive CSS animations for seamless transitions and engaging feedback.",
        "Created an engaging m/c quiz website with PERN stack, timed questions, topic selection, scoring, and 300+ question database. Designed using Figma with interactive CSS animations for smooth transitions and feedback.",
    )
)

sevenLineProjects.append(
    Project7(
        "Hangman Game (TypeScript, React, Express, PostgreSQL w/ matter.js, p5.js)       ",
        "May 2022 - Jun 2022",
        "Created an immersive hangman game by harnessing the capabilities of matter.js, which showcased visually appealing elements like letters gracefully falling into a gravity-driven trash bin whenever the user guessed incorrectly.",
        "Integrated p5.js for captivating hangman figure animations, enhancing gameplay experience.",
        "Enhanced the user experience by adding hint and definition capabilities for each word, while leveraging the capabilities of lottie.js and advanced CSS techniques to create immersive animations.",
        "Built an immersive hangman game with matter.js and p5.js, showcasing visually appealing elements and animations. Enhanced user experience with hints, definitions, and advanced CSS techniques.",
    )
)

sevenLineProjects.append(
    Project7(
        "NBA All-Star Prediction Model (Python w/ scikit-learn, pandas, matplotlib)           ",
        "May 2023 - Jun 2023",
        "Developed a powerful Python-based NBA All-Star prediction model using scikit-learn's Decision Tree Classifier for accurate NBA All-Star selection based on statistics and positions.",
        "Achieved a significant 25 percent improvement in accuracy, precision, recall, and F-1 scores by conducting comprehensive data cleaning.",
        "Data cleaning strategies included employing the SMOTE algorithm to tackle class imbalance, eliminating duplicates, and handling missing values with default values.",
        "Developed a powerful Python-based NBA All-Star prediction model using scikit-learn's Decision Tree Classifier for accurate NBA All-Star selection based on statistics and positions.",
    )
)

sevenLineProjects.append(
    Project7(
        "Basketball Action Tracking System (Python w/ TensorFlow)                                     ",
        "Oct 2023 - Dec 2023",
        "Developed a basketball action tracking system using a ConvLSTM model in TensorFlow to automate the identification of key actions such as dunks, three-pointers, and free throws.",
        "Implemented an action counter feature to automatically count the occurrences of specific actions, aiding in end-of-game statistics.",
        "Achieved a 21% performance improvement in accuracy, precision, recall, and F1 scores through hyperparameter tuning, including learning rate adjustment and regularization.",
        "Developed a basketball action tracking system using ConvLSTM, Python, and TensorFlow to automate key action identification. Implemented an action counter and achieved a 21% performance improvement through hyperparameter tuning.",
    )
)

sevenLineProjects.append(
    Project7(
        "Hoop Debate (React w/ Express and NeonDB)                                                           ",
        "May 2023 - Jun 2023",
        "Developed a dynamic website using React and Express, inspired by the popular 'Would You Rather' game, focusing on engaging basketball and NBA debates.",
        "Implemented animated selection counts to visually display the number of users who selected each option, enhancing user interaction.",
        "Utilized NeonDB as a cloud-hosted PostgreSQL database to efficiently store and manage user selection counts. Deployed the fully functional web application on Render.",
        "Built an interactive debate platform using React and Express, featuring animated selection counts and leveraging NeonDB for data storage. Hosted the application on Render.",
    )
)

sevenLineProjects.append(
    Project7(
        "Polymo (React)                                                                                                                    ",
        "May 2023 - Jun 2023",
        "Developed a responsive website using React to provide engaging and informative reading content on diverse topics, including business, finance, and government scandals (e.g., Panama Papers).",
        "Deployed the website on Render, achieving over 40 signups for the waitlist via Airtable within the first week.",
        "Engaged with users to gather feedback and iteratively improved website features and offerings based on their input, ensuring a user-centric development approach.",
        "Built a responsive content-focused website using React, deployed on Render. Successfully engaged users, resulting in rapid signups and iterative improvements based on feedback.",
    )
)

sevenLineProjects.append(
    Project7(
        "WhatNBAPlayerAmI (Python w/ scikit-learn)						 ",
        "May 2023 - Jun 2023",
        "Developed a K-Nearest Neighbors (K-NN) model to accurately predict which NBA player a user resembles based on characteristics such as playing style and mentality.",
        "Implemented a visually appealing interface using Gradio, allowing users to easily select their preferred inputs for the model.",
        "Deployed the application on HuggingFace to ensure accessibility and seamless performance for users.",
        "Created an engaging NBA player similarity predictor using Python and scikit-learn, with a user-friendly Gradio interface. Deployed on HuggingFace for optimal accessibility and performance.",
    )
)

sevenLineProjects.append(
    Project7(
        "AI Resume/Cover Letter Builder (Python w/ OpenAI API, Tkinter, Google Drive API) 		",
        "May 2024 - June 2024",
        "Developed an AI-driven Resume and Cover Letter generator using Python, integrating the OpenAI API to create customized job application materials based on user input and job descriptions.",
        "Implemented a user-friendly interface with Tkinter, allowing users to input job requirements and details, which are then processed by the AI to generate tailored resumes and cover letters.",
        "Also integrated Google Drive API for saving and retrieving documents directly from the user’s Google Drive account. Fun Fact: This resume was created using the tool!",
        "Created an engaging NBA player similarity predictor using Python and scikit-learn, with a user-friendly Gradio interface. Deployed on HuggingFace for optimal accessibility and performance.",
    )
)

sevenLineProjects.append(
    Project7(
        "Peer to Peer Application (C w/ Socket Programming)        			      ",
        "Sep 2023 - Dec 2023",
        "Developed a Peer to Peer (P2P) application using C for file sharing between peers, enabling dynamic roles as servers and clients through an index server.",
        "Utilized socket programming with TCP for reliable peer-to-peer transfers and UDP for server communication, incorporating error handling and firewall security.",
        "Performed extensive testing to ensure functionality, managing tasks such as content registration, deregistration, and efficient querying within the network.",
        "Created an engaging NBA player similarity predictor using Python and scikit-learn, with a user-friendly Gradio interface. Deployed on HuggingFace for optimal accessibility and performance.",
    )
)

sevenLineProjects.append(
    Project7(
        "Distributed Inventory and Delivery System (Python w/ FastAPI and gRPC)	       ",
        "Mar 2024 - Apr 2024",
        "Created a simulated distribution network using FastAPI and gRPC to manage multi-warehouse inventory and optimize delivery routes similar to Amazon's distribution.",
        "Utilized JSON for data storage and a detailed 25x25 grid map to plan logistics, facilitating server-client interactions and inventory management.",
        "Also designed a React-based frontend for user interaction, supporting product browsing, order placement, and delivery tracking, enhanced by algorithms to optimize warehouse coverage.",
        "Created an engaging NBA player similarity predictor using Python and scikit-learn, with a user-friendly Gradio interface. Deployed on HuggingFace for optimal accessibility and performance.",
    )
)

sevenLineProjects.append(
    Project7(
        "Home IoT EV Charger System (Raspberry Pi, Python, MotionEyeOS)	            ",
        "Sep 2023 - Apr 2024",
        "Developed an integrated Home IoT EV charger system using Raspberry Pi microcontrollers, featuring real-time motion detection, charging monitoring, and automated notifications.",
        "Configured MotionEyeOS for motion-triggered email alerts and video storage, utilizing local SSD and Dropbox cloud integration for secure data handling.",
        "Implemented hardware setups for Raspberry Pi, including WiFi configuration, and wrote Python scripts for LED motion alerts and simulated EV charging data transmission.",
        "Created an engaging NBA player similarity predictor using Python and scikit-learn, with a user-friendly Gradio interface. Deployed on HuggingFace for optimal accessibility and performance.",
    )
)


