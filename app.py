import streamlit as st
from google.cloud import aiplatform
from utils import extract_text_from_pdf
import os

# Initialize Gemini (set this before running or use Streamlit secrets)
PROJECT_ID = "your-gcp-project-id"
LOCATION = "us-central1"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "your-service-account-key.json"

aiplatform.init(project=PROJECT_ID, location=LOCATION)

@st.cache_resource
def get_model():
    from vertexai.preview.generative_models import GenerativeModel
    return GenerativeModel("gemini-pro")

model = get_model()

st.set_page_config(page_title="CareerGPT", page_icon="🧠")
st.title("🎓 CareerGPT – Your AI Career Guide")

mode = st.radio("How would you like to proceed?", ["Chat with CareerGPT", "Upload Resume for Suggestions"])

if mode == "Chat with CareerGPT":
    prompt = st.text_area("Ask anything about careers:", placeholder="e.g. What should I learn to become a Data Scientist?")
    if st.button("Ask"):
        if prompt.strip():
            with st.spinner("Thinking..."):
                res = model.generate_content(prompt)
                st.success(res.text)
        else:
            st.warning("Please enter a question.")
else:
    uploaded = st.file_uploader("Upload your resume (PDF)", type=["pdf"])
    if uploaded:
        resume_text = extract_text_from_pdf(uploaded)
        st.text_area("Extracted Resume Content:", resume_text, height=200)

        if st.button("Generate Suggestions"):
            with st.spinner("Analyzing your resume..."):
                input_prompt = f"""You are an AI career coach. A user has uploaded the following resume:\n\n{resume_text}\n\n
Suggest 3 ideal career paths based on their skills and background.
For each path, give required skills, salary range (in USD), and one popular online course to get started."""
                response = model.generate_content(input_prompt)
                st.markdown("### Career Recommendations")
                st.markdown(response.text)