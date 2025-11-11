# 🎓 University Policy Chatbot

An intelligent **University Policy Chatbot** built using **LangChain**, **Google Gemini API**, and **FAISS**, designed to help students and faculty instantly understand university rules, conduct policies, and academic procedures — all from uploaded university documents.

---

## 🚀 Features

- 🔍 **Retrieval-Augmented Generation (RAG)** pipeline for accurate, document-based responses  
- ⚡ Powered by **Google Gemini 2.5 Flash** for fast and intelligent answers  
- 🧠 **FAISS Vector Store** for efficient semantic document search  
- 🗂️ Supports both `.pdf` and `.txt` documents  
- 💬 **Interactive FastAPI Web Chat UI** (served via Uvicorn)  
- 🌌 Elegant dark glassmorphism theme for the frontend  

---

## 📁 Project Structure

```
university-application-chatbot/
│
├── app.py          # Core chatbot logic (Gemini + FAISS)
├── ingest.py       # Builds FAISS index from PDFs/TXT files
├── server.py       # FastAPI frontend + web chat interface
├── data/           # Folder for your university documents (.pdf, .txt)
├── faiss_index/    # Auto-generated FAISS vector index
├── .env            # Contains your GOOGLE_API_KEY
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/BURLAGADDA-AJAY-HARI-KRISHNA-221FA04286/Understanding-University-Policies-Resources.git
cd "Understanding-University-Policies-Resources"
```

### 2️⃣ Create a Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate      # On Windows
# or
source venv/bin/activate   # On macOS/Linux
```

### 3️⃣ Install Dependencies
```bash
pip install fastapi uvicorn python-dotenv google-genai faiss-cpu langchain langchain-community langchain-text-splitters sentence-transformers pypdf
```

---

## 🔑 Environment Setup

Create a `.env` file in your root directory:
```bash
GOOGLE_API_KEY=your_gemini_api_key_here
```

👉 Get your API key: [Google AI Studio](https://aistudio.google.com/app/apikey)

---

## 🧱 Step 1 — Build the Knowledge Base

Place `.pdf` or `.txt` documents in `data/` and run:
```bash
python ingest.py
```

✅ This loads, splits, and embeds your documents into a FAISS vector index.

---

## 💬 Step 2 — Run the Chatbot Locally

```bash
uvicorn server:app --reload
```

Then open:
```
http://127.0.0.1:8000/
```

---

## 🧠 Example Queries

**User:** What are the rules for attendance?  
**Bot:** Students must maintain a minimum of 75% attendance in each course.  

**User:** Are there any holidays in November?  
**Bot:** Based on the academic calendar, the university remains closed for Diwali.

---

## 🎥 Demo Preview

▶️ [**Watch the full demo video on Google Drive**](https://drive.google.com/file/d/1CTUTHD0Mukuu0WcWSU9k3HOglcrgyAHS/view?usp=sharing)

---

## 🧩 Tech Stack

| Component | Technology |
|------------|-------------|
| LLM | Google Gemini 2.5 Flash |
| Embedding Model | Sentence Transformers (MiniLM-L6-v2) |
| Vector Database | FAISS |
| Framework | FastAPI |
| Frontend | HTML + CSS (Glassmorphism Theme) |
| Runtime | Uvicorn |
| Document Loader | LangChain + PyPDF |

---

## 🧭 Troubleshooting

| Issue | Solution |
|--------|-----------|
| ⚠️ Out of Memory Error | Use lazy-loading FAISS (already included in `app.py`) |
| ❌ API Key Error | Ensure `.env` file exists with valid `GOOGLE_API_KEY` |
| 🗂️ No Documents Loaded | Check `data/` folder for `.pdf` or `.txt` files |
| 🧩 Index Not Found | Re-run `python ingest.py` before starting the server |

---

## 🧑‍💻 Author

**Burlagadda Ajay Hari Krishna**  
🎓 Final Year B.Tech (CSE)  
Vignan’s Institute of Information Technology  

📧 [ajayburlagadda@gmail.com](mailto:ajayburlagadda@gmail.com)  
🌐 [GitHub Profile](https://github.com/BURLAGADDA-AJAY-HARI-KRISHNA-221FA04286)

---

> _“Empowering students with instant access to university knowledge.”_ 🎓
