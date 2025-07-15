# 🎓 CareerGPT – AI Career Guidance

A personalized Gen AI-powered tool using **Gemini API + Streamlit + Vertex AI** to give career suggestions based on user input or resume uploads.

## Features
- Gemini-powered AI chat for career queries
- Resume upload and AI suggestions
- Streamlit UI
- Google AI integration

## Setup

1. Clone repo
2. Add your GCP Service Account key: `your-service-account-key.json`
3. Set up env:
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Tech Used
- Gemini API (Vertex AI)
- Google Cloud Storage (optional)
- PyPDF2 for resume reading
- Streamlit UI