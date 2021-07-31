from fastapi import FastAPI
from weasyprint import HTML

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello world"}

@app.get("/download_pdf/{web_page}")
async def download(web_page: str):
    file_location = "/tmp/html2pdf/" + web_page + ".pdf"
    get_pdf_from_url(web_page, file_location)
    return FileResponse(path=file_location)

def get_pdf_from_url(url, location):
    HTML(url).write_pdf(location)
