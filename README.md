# 📚 AI Study Buddy – Notes Summarizer + Quiz Generator

An AI-powered tool for students that:
- 📄 Takes a textbook or lecture PDF
- 🧠 Summarizes it using a local LLM (Mistral via Ollama)
- ❓ Generates MCQs to help with revision

Built with Python, Streamlit, and open-source LLMs. No internet or paid API needed.

---

## ✨ Features

- ✅ Upload any PDF file
- 📝 Generates a concise summary
- 🧪 Creates 3–5 multiple-choice questions based on the summary
- 💻 Runs **fully offline** using [Ollama](https://ollama.com/) and the `mistral` model

---

## 🛠 Tech Stack

- Python 3.8+
- Streamlit
- [Ollama](https://ollama.com/) (Local LLM runner)
- Mistral 7B (via Ollama)
- PyMuPDF (`fitz`) for PDF text extraction

---

## 🚀 Installation

1. **Clone the repository:**

```bash
git clone https://github.com/Stark6612/Study-Buddy.git
cd Study-Buddy
```

2. **Create a virtual environment (optional but recommended):**

```bash
python -m venv venv
# Activate it
source venv/bin/activate      # On Mac/Linux
venv\Scripts\activate       # On Windows
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

4. **Install and run Ollama:**

- Download and install from [https://ollama.com](https://ollama.com)
- Pull the Mistral model:

```bash
ollama pull mistral
```

---

## 🧪 Run the App

```bash
streamlit run app.py
```

1. Upload a PDF textbook or notes
2. Click "Generate Summary and MCQs"
3. Read the AI-generated summary and quiz yourself!

---

## 📂 Project Structure

```
ai-study-buddy/
│
├── app.py                # Streamlit frontend logic
├── ollama_client.py      # Local LLM call using subprocess
├── pdf_utils.py          # PDF to text extraction using PyMuPDF
├── requirements.txt      # All Python dependencies
└── README.md             # This file
```

---

## ⚠️ Notes

- Make sure `ollama` runs in your terminal and Mistral is available.
- Input is truncated at 7000 characters due to token limits.
- For large PDFs, consider chunking (future improvement).

---

