<p align="center">
  <img src="https://github.com/CGenius-FIAP/API-GPT/blob/main/logo.jpeg" alt="header" width="50%" />
</p>

<h1 align="center">Cart Genius</h1>

> Status: ⚠️⚠️ In development ⚠️⚠️


- [Introduction](#intro)
- [Installation](#install)
- [How to use](#manual)
- [Techs](#techs)
- [Endpoints](#endpoints)
- [Future Plans](#doc)
- [Credits](#credits)


## 🚀🚀 <a id="intro"></a>Introduction 🚀🚀

  We are proud to announce the 3rd Sprint of the 2023 FIAP + PLUSOFT Challenge. We aimed to deliver precisely what we were asked to: a new chatbot integrated with OpenAI's groundbreaking ChatGPT, trained toward a more focused area.

  Our project was to create a sales assistant capable of answering a wide range of questions, from stock availability to furniture dimensions, power consumption of a GPU, differences between newer and older generations of certain products, and more.

  Eventually, we plan to add features to complete purchases through the chatbot itself . But for now, we are focusing on core aspects of the project, such as cloud availability and code refactoring for improved performance and lower operation costs.

  We've just finished the core essentials of the system, and from now until Sprint 4, we intend to polish and improve the UI/UX for our customers. We will also enhance the training prompts given to GPT, as well as provide secure storage for conversation history and incorporate image displays in the chatbox for further immersion.

  Our main goal is to automate, to a certain extent, the adaptability of the chatbot, making it easier to create prompts so that it can be used in almost all types of businesses.


<p align="center"><b>We're not there yet, but we will be eventually.</b></p>

---


## 🔧🔧 <a id="install"></a>Installation 🔧🔧

  For this specific API, all you need to do is:
  ### 1. Clone the repository
  > git clone https://github.com/CGenius-FIAP/API-GPT.git
<br>

  ### 2. Navigate to the Directory
  > cd API-GPT
<br>

  ### 3. [OPTIONAL] Depending on your machine's Python or personal preferences, you might want to create a virtual environment
  > python -m venv venv
<br>

  ### 4. Install packages and dependencies
  > pip install -r requirements.txt

  Or 

  > python data/script_pip.py

---


## 📖📖 <a id="manual"></a>How to use 📖📖

To test the API, you will need an API CLIENT, such as Insomnia.

[Direct link for the official site download](https://updates.insomnia.rest/downloads/windows/latest?app=com.insomnia.app&source=website) <br>

Or else download it manually at their site: https://insomnia.rest/download

---


## <a id="endpoints"></a>Endpoints
  | METHOD | ADDRESS                   | ENDPOINT |
|--------|---------------------------|----------|
| POST   | http://20.226.206.195:8000| /query    |
| GET    | http://20.226.206.195:8000| /reset    |

---


## <a id="techs"></a>Main Technologies and Dependencies

For this project, we used a variety of technologies to develop a robust and scalable API.

### 💻 Main Technologies
- **Python**: Our primary language for developing the API, chosen for its simplicity and robust libraries.
- **Flask**: An easy, light and highly customizable framework for fast and efficient API development.
- **ACI/ACR**: Used for easy deployment and scaling via Azure Container Instances and Azure Container Registry.
- **Java 17**: Employed for other backend services, known for its robustness and extensive libraries.
- **PLSQL**: Utilized for seamless database interactions with Oracle Database.
- **JavaScript**: Scripting language that adds interactivity to our web and mobile interfaces.
- **React**: A JavaScript library focused on building dynamic and responsive UI for our web application.
- **React Native**: Enables native mobile app development using JavaScript.
- **Oracle Database**: Our primary database for storing and managing all project data.

<br>

### 💻 Frontend Specific

- **Stack Navigator**: Handles routes and navigation in our React Native application.
- **Async Storage**: Used for login validation, ensuring that only registered users can access the app.

<br>

### 📦 Others

- **React-Native**: Chosen for mobile development, allows code reuse for both iOS and Android.
- **Java-Spring**: Used in developing other backend services of the project.

<br>

### 📦 Dependencies

- **cx_Oracle**: Allowed us to interact seamlessly with Oracle databases.
- **langchain**: Assisted in language processing tasks.
- **chromadb**: Used for database management. (needs Desktop Development C++ Tools + SQLITE3)
- **unstructured**: Helped in handling unstructured data.
- **tiktoken**: Used for tokenization tasks.
- **gunicorn**: Served as our WSGI HTTP Server.
- **Flask-Session**: Managed user sessions in our Flask application.
- **openai**: Integrated the OpenAI GPT model for chat functionalities.

<br>
<p align="center">While some of these dependecies might not be active in the project for this sprint, they are present at the version we are currently working to deliver on the next sprint. Expect changes for the next sprint, as tests goes on. </p>

---


## <a id="doc"></a>Future Plans 🌱🛠️

We have several exciting features and improvements planned for the future sprint:

- **Security Measures**: 🛡️🔒 Working on several fronts to bolster security:
  - 🛡️ Implementing advanced authentication techniques for enhanced security.
  - 🔒 Improving the management of sensitive information using Azure Key Vaults and environment variables. (Note: These features are still in the process of being fully implemented.)

- **Data Visualization Tools**: 📊💡 
  - 📊 Creating intuitive dashboards and interactive charts to help our partner companies make data-driven decisions.
  - 💡 These tools will serve as strategic assets for businesses, enabling them to understand customer behaviors, track chatbot performance, and identify areas for improvement.

- **Other Short-Term Enhancements**: 
  - Continued performance optimizations, bug fixes, and UI/UX improvements.

We're committed to continuously improving the system based on feedback and technological advancements.

---


## <a id="credits"></a>Credits 👏🌟

This project was a collaborative effort and wouldn't have been possible without the contributions of:

- **Filipe Santos**: 👨‍💻🌩
  - **Role**: API Development, Cloud Deployment and GPT-Chatbot Training.
  - **Courses**: 
    - Enterprise Application Development
    - Digital Business Enablement
    - Disruptive Architectures - IOT, IOB, AI
    - DevOps
  
- **Jorge Camara**: 👨‍💻🎨
  - **Role**: Front-End Development and Testing.
  - **Courses**: 
    - Hybrid Mobile App Development
    - DevOps
  
- **Vitor Madureira**: 👨‍💻📊
  - **Role**: Database Management and Quality Assurance.
  - **Courses**: 
    - Compliance and Quality Assurance
    - Database Application and Data Science

Each individual brought unique skills and perspectives to the table, making the project more robust and well-rounded.

---


## <a id="conclusion"></a>Concluding Remarks 🎯🛠

This project is a work-in-progress and, while we are proud of what we have accomplished so far, we recognize that there is room for improvement. We are actively working to refine the system, address its limitations, and expand its capabilities. Your feedback is crucial for us, so feel free to open issues or contribute to the repository.

<p align="center"><b>We're not there yet, but we're committed to getting there. Thank you for being part of this journey with us.</b></p>

