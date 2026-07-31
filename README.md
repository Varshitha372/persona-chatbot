# 🤖 AI Interview Coach – Persona-Based Chatbot

## 📌 Project Overview

The **AI Interview Coach** is a Persona-Based Chatbot developed using **Python**, **Streamlit**, and **Google Gemini 2.5 Flash**. The chatbot acts as a professional Human Resources (HR) interviewer, helping users prepare for job interviews by asking relevant questions, evaluating responses, and providing constructive feedback.

This project demonstrates the practical implementation of **Generative AI**, **Prompt Engineering**, **Conversational AI**, **Memory Management**, and **Large Language Models (LLMs)**.

---

## 📂 Project Category

**Conversational AI – Persona-Based Chatbot**

---

## 🎯 Problem Statement

Many students and fresh graduates lack access to realistic mock interviews before attending actual job interviews. Traditional preparation methods often do not provide interactive feedback or personalized guidance.

This project addresses this challenge by providing an AI-powered HR Interview Coach that conducts mock interviews, evaluates responses, and offers constructive feedback while maintaining a consistent HR interviewer persona.

---

## 🎯 Project Objectives

- Build a Persona-Based AI Chatbot
- Implement Prompt Engineering using a System Prompt
- Simulate professional HR interviews
- Maintain conversation history during a session
- Evaluate candidate responses
- Provide interview feedback and suggestions
- Develop a user-friendly web application with Streamlit
- Prepare the application for deployment

---

## ✨ Features

- 🤖 Professional HR Interviewer Persona
- 💬 AI-Powered Interview Conversations
- 🧠 Session-Based Memory
- 🔄 Context-Aware Responses
- ❓ Interview Question Generation
- ✅ Candidate Answer Evaluation
- 📋 Personalized Feedback
- 🎨 User-Friendly Interface
- 🔐 Secure API Key Management
- ⚠️ Error Handling

---

## 🛠️ Technologies Used

### Programming Language
- Python 3.10+

### Frontend
- Streamlit

### AI Model
- Google Gemini 2.5 Flash

### Libraries
- google-genai
- streamlit
- python-dotenv

### Version Control
- Git
- GitHub

---

## 📁 Project Structure

```text
persona-chatbot/
│
├── app.py
├── chatbot.py
├── prompts.py
├── memory.py
├── assets/
├── requirements.txt
├── README.md
├── .gitignore
└── .env (not included in GitHub)
```

---

## ⚙️ System Workflow

```text
User
   │
   ▼
Streamlit Interface
   │
   ▼
HR Persona System Prompt
   │
   ▼
Google Gemini 2.5 Flash
   │
   ▼
Generate AI Response
   │
   ▼
Display Response
   │
   ▼
Store Chat History
```

---

## 🚀 Installation

### Clone the Repository

```bash
git clone https://github.com/Varshitha372/persona-chatbot.git
```

### Navigate to the Project

```bash
cd persona-chatbot
```

### Create a Virtual Environment

```bash
python -m venv venv
```

### Activate the Virtual Environment (Windows)

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Create a `.env` File

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

### Run the Application

```bash
streamlit run app.py
```

---

## 💬 Usage

1. Launch the application.
2. Start a mock interview.
3. Answer the interview questions.
4. Receive AI-generated feedback.
5. Continue until the interview is completed.

---

## 🧠 Prompt Engineering

The chatbot uses a System Prompt to maintain the role of a professional HR interviewer.

It can:

- Ask interview questions
- Evaluate responses
- Provide constructive feedback
- Suggest improvements
- Maintain a professional tone

---

## 💾 Memory Management

Conversation history is maintained using **Streamlit Session State**, allowing the chatbot to remember previous interactions and provide context-aware responses.

---

## ⚠️ Error Handling

The application handles:

- Invalid API Key
- Empty User Input
- Internet Connectivity Issues
- API Errors
- Unexpected Exceptions

---

## ✅ Testing

The application has been tested with:

- Greeting conversations
- HR interview sessions
- Technical interview questions
- Behavioural interview questions
- Follow-up conversations
- Empty input handling
- Chat history management

---

## 📷 Screenshots

_Add screenshots after deployment._

- Home Page
- Chat Interface
- Interview Questions
- AI Feedback
- Final Conversation

---

## 🌐 Deployment

**Platform:** Streamlit Community Cloud

**Live Demo:** *(Add your deployment link here after deployment.)*

---

## 🚀 Future Enhancements

- Voice-Based Interviews
- Resume Analysis
- Interview Score Dashboard
- Technical Interview Mode
- Multiple Interview Personas
- Multi-Language Support
- Downloadable PDF Report

---

## 📚 Learning Outcomes

- Generative AI
- Prompt Engineering
- Persona Design
- Conversational AI
- Memory Management
- Google Gemini API Integration
- Streamlit Application Development
- Git & GitHub Workflow

---

## 👩‍💻 Author

**Andaluri Varshitha**

**Project:** AI Interview Coach – Persona-Based Chatbot

**Assessment:** GenAI Assessment Framework 2026