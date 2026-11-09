@echo off
title Gemini AI Chatbot Server
echo ========================================================
echo Starting Gemini AI Chatbot at http://localhost:8080 ...
echo ========================================================
start "" "http://localhost:8080"
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0server.ps1"
pause
