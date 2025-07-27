# Round 1B: Persona-Driven Document Intelligence 🚀

This project analyzes multiple PDF documents and ranks the most relevant sections and subsections based on a provided **persona** and **job-to-be-done**. It is built for **Adobe India Hackathon 2025 – Connecting the Dots**, Round 1B.

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

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/safiya2610/Round-1B-Persona-Driven-Document-Intelligence.git
cd Round-1B-Persona-Driven-Document-Intelligence
```

2. Create a Virtual Environment (optional but recommended)
```bash
python -m venv venv
venv\Scripts\activate     # For Windows
# source venv/bin/activate  # For macOS/Linux
```
3. Install Dependencies
```bash
pip install -r requirements.txt
```
5. Run Locally
```bash
python app.py
```
Open browser: http://localhost:5000

Docker Support
1. Build Docker Image
```bash
docker build -t persona-analyzer .
```
2. Run Container
```bash
docker run -p 5000:5000 persona-analyzer
```

