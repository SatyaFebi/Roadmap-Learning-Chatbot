# 🚀 Adaptive Learning Architect

**Adaptive Learning Architect** is a specialized AI Tutor designed to build personalized learning roadmaps. This project integrates a backend powered by **Google AI ADK** and Gemini 2.5 Flash with a modern frontend built using **Vue 3**.

---

## 🌟 Key Features

- **Syllabus Generation**: Create a step-by-step roadmap for any topic. Each milestone includes clear explanations, core concepts, and realistic timeframes.
- **Project Scoping**: Design a "Starter Project" for every syllabus that is practical, achievable, and integrates the skills learned from the roadmap.
- **Mentorship Matching**: Identify professional roles relevant to the user's goals and recommend the types of mentors they should connect with from the database.
- **Adaptive Logic**: The AI adjusts content based on the user's background; skipping fundamentals they already know to jump straight into advanced topics.

---

## 🛠️ Tech Stack

### Backend (AI Agent)
- **Engine**: [Google Generative AI ADK](https://github.com/googleapis/genai-adk)
- **Model**: `gemini-2.5-flash` (via Vertex AI)
- **Framework**: FastAPI / Uvicorn
- **Package Manager**: `uv`

### Frontend (User Interface)
- **Framework**: Vue 3 + Vite
- **Styling**: Vanilla CSS (Premium Dark Mode & Glassmorphism)
- **Animations**: GSAP
- **State Management**: Vue Composition API

---

## 📂 Folder Structure

```text
.
├── AI/                         # Backend AI Folder
│   ├── roadmap/                # Core ADK Agent logic (Roadmap engine)
│   ├── scripts/                # Utility scripts (setup, database)
│   ├── .env                    # Environment Config (API Keys, Project ID)
│   ├── server.py               # Backend API Entry Point
│   └── tools.yaml              # Tool definitions for MCP Toolbox
├── frontend/                   # Frontend Web App Folder
│   ├── src/
│   │   ├── components/         # UI Components (Chat bubbles, Suggestions, etc.)
│   │   ├── services/           # API Integration (api.js)
│   │   └── composables/        # Chat & State Logic (useChat.js)
│   └── vite.config.js          # API Proxy Configuration
└── README.md                   # Project Documentation
```

---

## 🚀 Getting Started

### 1. Backend Setup
Ensure you have `uv` installed and access to a Google Cloud Project.

```bash
cd AI
# 1. Environment Setup
# Create an .env file based on the provided template
# GOOGLE_CLOUD_PROJECT=your-project-id
# ADK_MODEL=gemini-2.5-flash

# 2. Run the Backend Server
uv run python server.py
```
The backend server will run at `http://localhost:8080`.

### 2. Frontend Setup
```bash
cd frontend
# 1. Install Dependencies
npm install

# 2. Start the Development Server
npm run dev
```
Open `http://localhost:5173` in your browser.

---

## 📝 AI Usage Guide

- **Requesting a Roadmap**: Type *"Create a crash course on Learning Python for Data Science"*
- **Adjusting Difficulty**: Type *"I already understand JavaScript, please create a mid-level React roadmap"*
- **Final Project**: The AI will automatically provide a project idea at the end of every syllabus generation.

---

## 🤝 Contribution
This project was developed to make it easier for anyone to start learning something new in a structured way. Feel free to fork the repository and submit a Pull Request if you have any improvement ideas!

---

*Powered by Google ADK & Gemini 2.5 Flash*
