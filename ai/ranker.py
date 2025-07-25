from sentence_transformers import SentenceTransformer, util
import numpy as np

# Load the sentence transformer model
model = SentenceTransformer("all-MiniLM-L6-v2")

def rank_sections(sections, persona, job):
    if not sections:
        return {
            "top_sections": [],
            "sub_sections": [],
            "error": "No sections found to rank."
        }

    # Combine persona and job for semantic matching
    query = f"{persona}. {job}"
    query_vec = model.encode(query)

    # Extract section contents and encode them
    contents = [s["content"] for s in sections]
    content_vecs = model.encode(contents)

    # Compute cosine similarity between query and all contents
    scores = util.cos_sim(query_vec, content_vecs)[0]
    scores = np.array(scores)  # Ensure proper NumPy array

    # Handle edge case: empty or invalid similarity scores
    if scores.size == 0:
        return {
            "top_sections": [],
            "sub_sections": [],
            "error": "No scores generated. Possibly empty inputs."
        }

    # Sort sections by similarity score (descending)
    ranked = np.argsort(scores)[::-1]

    # Build output lists for top 5 sections
    top_sections = []
    sub_sections = []
    for rank, idx in enumerate(ranked[:5], 1):
        s = sections[idx]
        top_sections.append({
            "document": s["document"],
            "page_number": s["page_number"],
            "section_title": s["title"],
            "importance_rank": rank
        })
        sub_sections.append({
            "document": s["document"],
            "refined_text": s["content"],
            "page_number": s["page_number"]
        })

    return {
        "top_sections": top_sections,
        "sub_sections": sub_sections
    }
