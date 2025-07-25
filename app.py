from flask import Flask, request, send_file, render_template
import os
from analyze_documents import analyze_documents

UPLOAD_FOLDER = "uploaded_files"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def index():
    return open("frontend/index.html").read()

@app.route("/analyze", methods=["POST"])
def analyze():
    persona = request.form["persona"]
    job = request.form["job"]
    pdf_files = request.files.getlist("pdfs")

    paths = []
    for f in pdf_files:
        path = os.path.join(UPLOAD_FOLDER, f.filename)
        f.save(path)
        paths.append(path)

    analyze_documents(paths, persona, job)
    return send_file("challenge1b_output.json", as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
