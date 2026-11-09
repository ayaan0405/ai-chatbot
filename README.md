# 🤖 Gemini AI Chatbot Studio

A modern AI chatbot powered by **Google Gemini API**, featuring **multi-turn conversational memory** and **instant Document / PDF Q&A (RAG)**.

---

## 🌟 Key Features

- **Multi-turn Conversational Memory**: Remembers context across interactions in the conversation.
- **Document & File Q&A (RAG)**:
  - Drag and drop **PDFs, TXT, Markdown, CSV, and code files** (`.py`, `.js`, etc.).
  - Automatic client-side PDF text extraction using PDF.js.
  - Ask questions directly about your uploaded documents with source context.
- **Google Gemini API Support**:
  - `gemini-2.5-flash`: Ultra-fast, highly intelligent, and cost-effective.
  - `gemini-1.5-flash`: Fast, high context window.
  - `gemini-1.5-pro`: Deep analytical reasoning.
- **Streaming Responses**: Real-time word-by-word streaming responses.
- **System Personas**: Switch between *Helpful Assistant*, *Document Analyst*, *Coding Mentor*, *Patient Tutor*, or *Custom Persona*.
- **Chat Management**: Create new chats, review previous sessions (saved in local storage), clear chat, and export conversations to Markdown.
- **Zero Server Setup Needed**: Runs directly in any modern web browser!

---

## 🚀 How to Run

### Option 1: Instant Web App (No Installation Required! ⭐ Recommended)

You can run the web chatbot immediately in your browser without needing to install Python or Node.js:

1. Double-click **`open_web_chatbot.bat`** (or **`start_local_server.bat`** to run via `http://localhost:8080`).
2. Your API key is already configured and ready to go!
3. Start chatting or drag-and-drop your PDFs to ask questions!

---

### Option 2: Python + Streamlit App

If you prefer running a Python server backend using Streamlit:

1. **Install Python**:
   - Download and install Python from [python.org](https://www.python.org/downloads/) (make sure to check *"Add Python to PATH"* during installation).
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Set your API Key**:
   - Copy `.env.example` to `.env` and fill in `GEMINI_API_KEY=your_key_here`, or enter it directly in the Streamlit sidebar.
4. **Run the Streamlit application**:
   ```bash
   streamlit run app.py
   ```
   *(Or double-click `run_streamlit.bat`)*

---

## 📂 Project Structure

```text
ai-chatbot/
│
├── index.html             # Standalone modern Web UI (Tailwind + Lucide + PDF.js + Marked)
├── open_web_chatbot.bat   # 1-click batch script to open Web UI in your default browser
│
├── app.py                 # Streamlit Python application
├── requirements.txt       # Python dependencies (streamlit, google-generativeai, pypdf)
├── run_streamlit.bat      # 1-click batch script to run Streamlit app
├── .env.example           # Template for environment variables
└── README.md              # Project documentation
```

---

## 🔑 Getting a Gemini API Key

1. Go to [Google AI Studio](https://aistudio.google.com/app/apikey).
2. Sign in with your Google Account.
3. Click **"Create API key"** and copy your key.
4. Paste it into the chatbot API Key settings modal.
