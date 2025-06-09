import streamlit as st
from pdf_utils import extract_text_from_pdf
from ollama_client import ollama_run_mistral
import tempfile

st.set_page_config(page_title="AI Study Buddy - Ollama + Mistral")

st.title("📚 AI Study Buddy (Ollama + Mistral)")

def clean_text(text):
    if not text:
        return ""
    return text.encode('ascii', errors='ignore').decode('ascii')

uploaded_file = st.file_uploader("Upload a PDF textbook", type=["pdf"])

if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded_file.read())
        pdf_path = tmp.name
    
    with st.spinner("Extracting text from PDF..."):
        raw_text = extract_text_from_pdf(pdf_path)
    
    st.write("### Extracted Text Preview:")
    st.text_area("Text (first 7000 chars)", raw_text[:7000], height=200)

    if st.button("Generate Summary and MCQs"):
        prompt_text = raw_text[:7000]

        summary_prompt = f"Summarize the following text concisely:\n\n{prompt_text}"
        with st.spinner("Generating summary..."):
            summary = ollama_run_mistral(summary_prompt)
        
        st.write("### Summary")
        st.write(clean_text(summary))

        mcq_prompt = f"""
Based on the following summary, generate 3 multiple-choice questions.
Provide 4 options for each question labeled a, b, c, d.
Indicate the correct answer after each question.

Summary:
{summary}
"""
        with st.spinner("Generating MCQs..."):
            mcqs = ollama_run_mistral(mcq_prompt)

        st.write("### Generated MCQs")
        st.text_area("MCQs", clean_text(mcqs), height=300)
