from fastapi import FastAPI
from weasyprint import HTML

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello world"}

def get_pdf_from_url(url, location):
    HTML(url).write_pdf(location)
