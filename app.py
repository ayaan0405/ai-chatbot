"""
=========================================================
My AI Chatbot Project - Student Edition
Course: Computer Science / AI Intro
Author: Ayaan
=========================================================
"""

import os
import streamlit as st
import google.generativeai as genai
from pypdf import PdfReader
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY", "")
MODEL_NAME = "gemini-3.8-flash"

# Page layout
st.set_page_config(page_title="My Student AI Chatbot", page_icon="🎓")
st.title("🎓 My AI Chatbot Project")
st.caption("A simple AI study assistant built with Python, Streamlit, and Google Gemini API.")

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar for file upload
with st.sidebar:
    st.header("📎 Attach Notes / PDF")
    uploaded_file = st.file_uploader("Upload a file to ask questions about it:", type=["pdf", "txt", "md", "py"])
    
    file_content = ""
    if uploaded_file:
        if uploaded_file.name.endswith(".pdf"):
            reader = PdfReader(uploaded_file)
            for page in reader.pages:
                file_content += page.extract_text() or ""
        else:
            file_content = uploaded_file.read().decode("utf-8", errors="ignore")
        st.success(f"Attached: {uploaded_file.name}")

    if st.button("🧹 Clear Chat History"):
        st.session_state.messages = []
        st.rerun()

# Display all previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# User input box
user_input = st.chat_input("Type your question here...")

if user_input:
    # 1. Add user message to display
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    # 2. Build prompt (attach document text if uploaded)
    full_prompt = user_input
    if file_content:
        full_prompt = f"[Attached Document Notes]:\n{file_content}\n\n[Question]: {user_input}"

    # 3. Call Gemini API
    with st.chat_message("assistant"):
        try:
            genai.configure(api_key=API_KEY)
            model = genai.GenerativeModel(
                model_name=MODEL_NAME,
                system_instruction="You are a friendly, encouraging AI study buddy. Help students understand concepts clearly."
            )
            
            # Format history for conversational memory
            history = [
                {"role": m["role"], "parts": [m["content"]]} 
                for m in st.session_state.messages[:-1]
            ]
            chat = model.start_chat(history=history)
            response = chat.send_message(full_prompt)
            
            # Display answer
            st.write(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})

        except Exception as e:
            st.error(f"Something went wrong: {e}")
