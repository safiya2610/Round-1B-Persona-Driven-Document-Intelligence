FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN apt-get update && apt-get install -y build-essential poppler-utils  && pip install --no-cache-dir flask sentence-transformers pymupdf

EXPOSE 5000
CMD ["python", "app.py"]