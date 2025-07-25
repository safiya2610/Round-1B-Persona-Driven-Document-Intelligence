## Approach Explanation - Adobe Hackathon Round 1B

### Objective
Build a system to extract and prioritize relevant content from PDF documents based on a given persona and job-to-be-done.

### Methodology
1. **Text Extraction**:
   - We use PyMuPDF to extract paragraphs from each page of the input PDFs.

2. **Persona-Job Query Encoding**:
   - We combine the persona and job strings into a unified semantic query.
   - The query is encoded into a vector using a lightweight sentence-transformer model (`all-MiniLM-L6-v2`).

3. **Section Embedding & Scoring**:
   - Each section of the document is embedded similarly.
   - Cosine similarity is used to measure relevance between each section and the persona-job query.
   - Top N (default: 5) sections are selected based on similarity scores.

4. **Subsection Analysis**:
   - For each top section, the refined paragraph content is extracted and cleaned.
   - These are returned in the `sub_section_analysis`.

### Output
The output follows the format defined in `challenge1b_output.json`:
- Metadata
- Extracted top-ranked sections
- Sub-section analysis

### Constraints Handled
- CPU-only: No GPU used
- Model <1GB: Uses ~90MB model
- Offline: No external API calls
- Performance: Executes under 60s for 3-5 documents

### Conclusion
This pipeline allows fast, semantic filtering of relevant sections from large text PDFs tailored to a user’s intent.