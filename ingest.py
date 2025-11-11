import os
from pathlib import Path
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

load_dotenv()

# === CONFIGURATION ===
DATA_DIR = Path("data")                # Folder where PDFs/TXT files are stored
INDEX_DIR = "faiss_index"              # Folder to save FAISS index
EMBED_MODEL = "sentence-transformers/paraphrase-MiniLM-L3-v2"  # Lightweight model for Render

def load_documents(data_dir: Path):
    """Loads all .txt and .pdf files recursively from the data directory."""
    docs = []

    if not data_dir.exists():
        raise FileNotFoundError("⚠️ Folder 'data/' not found. Create it and add your files.")

    for file_path in data_dir.rglob("*"):
        if file_path.suffix.lower() == ".txt":
            print(f"📄 Loading text: {file_path.name}")
            loader = TextLoader(str(file_path), encoding="utf-8")
            docs.extend(loader.load())

        elif file_path.suffix.lower() == ".pdf":
            print(f"📘 Loading PDF: {file_path.name}")
            loader = PyPDFLoader(str(file_path))
            docs.extend(loader.load())

    if not docs:
        print("⚠️ No .txt or .pdf files found in data/. Add files and rerun.")
    return docs


def main():
    # Step 1: Load documents
    raw_docs = load_documents(DATA_DIR)
    if not raw_docs:
        return

    # Step 2: Split text into chunks
    print("✂️ Splitting documents into chunks...")
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=150,
        separators=["\n\n", "\n", " ", ""]
    )
    docs = splitter.split_documents(raw_docs)
    print(f"✅ Created {len(docs)} text chunks.")

    # Step 3: Generate embeddings
    print("🔢 Generating embeddings using HuggingFace...")
    embeddings = HuggingFaceEmbeddings(model_name=EMBED_MODEL)

    # Step 4: Store vectors in FAISS
    print("💾 Building FAISS index...")
    vectordb = FAISS.from_documents(docs, embeddings)
    vectordb.save_local(INDEX_DIR)
    print(f"✅ FAISS index saved at '{INDEX_DIR}' with {len(docs)} chunks.")


if __name__ == "__main__":
    main()
