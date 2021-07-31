from fastapi import FastAPI
from weasyprint import HTML
import os

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello world"}

@app.get("/download_pdf/{web_page:path}")
async def download(web_page: str):
    check_tmp_html2pdf_folder()
    file_location = "/tmp/html2pdf/" + web_page + ".pdf"
    get_pdf_from_url(web_page, file_location)
    return FileResponse(path=file_location)

def get_pdf_from_url(url, location):
    HTML(url).write_pdf(location)

def check_tmp_html2pdf_folder():
    try:
        os.makedirs("/tmp/html2pdf")
    except FileExistsError:
        pass
