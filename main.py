from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.responses import JSONResponse
from weasyprint import HTML
import os

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello world"}

@app.get("/download_pdf/{web_page:path}")
async def download(web_page: str):
    check_tmp_html2pdf_folder()
    file = str(abs(hash(web_page))) + ".pdf"
    file_location = "/tmp/html2pdf/" + file
    get_pdf_from_url(web_page, file_location)
    return FileResponse(path=file_location)

@app.delete("/delete_tmp")
def delete_tmp():
    folder = '/tmp/html2pdf/'
    try:
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        return JSONResponse(content={
            "removed": True
            }, status_code=200)   
    except Exception as e:
        return JSONResponse(content={
            "removed": False,
            "error_message": "Failed to clean /tmp/"
        }, status_code=404)


def get_pdf_from_url(url, location):
    HTML(url).write_pdf(location)

def check_tmp_html2pdf_folder():
    try:
        os.makedirs("/tmp/html2pdf")
    except FileExistsError:
        pass
