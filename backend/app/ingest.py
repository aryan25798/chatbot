from fastapi import UploadFile
from app.utils.scraper import scrape_website
from app.utils.file_parser import parse_file
from app.models.embeddings import index_content

async def ingest_content(url: str = None, file: UploadFile = None):
    if url:
        content = scrape_website(url)
    elif file:
        content = parse_file(await file.read())
    else:
        return {"error": "Provide a URL or file"}
    index_content(content)
    return {"status": "Content ingested"}
