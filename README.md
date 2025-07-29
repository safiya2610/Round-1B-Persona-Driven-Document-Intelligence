# Round 1B: Persona-Driven Document Intelligence 🚀

This project analyzes multiple PDF documents and ranks the most relevant sections and subsections based on a provided **persona** and **job-to-be-done**. 
## Objective

Given a **persona** and a **job**, the system:
- Extracts textual content from multiple PDFs.
- Computes semantic similarity between content and the persona/job description.
- Ranks relevant sections and subsections.
- Outputs a structured JSON with stack-ranked results.

## Features

- Supports multi-PDF uploads.
- Persona + Job-driven contextual ranking.
- Outputs hierarchical JSON (Title > Section > Subsection).
- Fast (≤ 60s), offline, CPU-only.
- Containerized with Docker.
- Clean HTML frontend with glassmorphic design.

---
## Architecture diagram
<img width="500px" height="600px" alt="image" src="https://github.com/user-attachments/assets/0ec46ba5-4a5d-4b34-a860-fec8c5e1bce7" />

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/safiya2610/Round-1B-Persona-Driven-Document-Intelligence.git
cd Round-1B-Persona-Driven-Document-Intelligence
```

### 2. Create a Virtual Environment 
```bash
python -m venv venv
venv\Scripts\activate     # For Windows
# source venv/bin/activate  # For macOS/Linux
```
### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
### 4. Run Locally
```bash
python app.py
```
Open browser: http://localhost:5000

## Docker Support
### 1. Build Docker Image
```bash
docker build -t persona-analyzer .
```
### 2. Run Container
```bash
docker run -p 5000:5000 persona-analyzer
```

## Architecture
```css
[Documents] → [Text Extractor] → [Chunker] → [Vector Embedding] → [Search & Ranking]
Persona + Job → [Intent Extractor] → [Query Embedding] → [Ranking Engine]
→ [Summarizer] → [Output Dashboard]
```

![WhatsApp Image 2025-07-26 at 17 39 48_6d03d45e](https://github.com/user-attachments/assets/7c9f8420-be4f-4a73-89c5-2ffd3215b627)



