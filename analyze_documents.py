import os
import json
from datetime import datetime
from utils.pdf_parser import extract_sections_from_pdf
from ai.ranker import rank_sections

def analyze_documents(pdf_paths, persona, job):
    all_sections = []
    for pdf_path in pdf_paths:
        sections = extract_sections_from_pdf(pdf_path)
        for s in sections:
            s["document"] = os.path.basename(pdf_path)
        all_sections.extend(sections)

    results = rank_sections(all_sections, persona, job)

    output = {
        "metadata": {
            "input_documents": [os.path.basename(p) for p in pdf_paths],
            "persona": persona,
            "job_to_be_done": job,
            "processing_timestamp": datetime.now().isoformat()
        },
        "extracted_sections": results["top_sections"],
        "sub_section_analysis": results["sub_sections"]
    }

    with open("challenge1b_output.json", "w") as f:
        json.dump(output, f, indent=2)

    return output