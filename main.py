from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()
templates = Jinja2Templates(directory="local_templates/")
# app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/testing_template", response_class=HTMLResponse)
async def testing_template(request: Request):
    return templates.TemplateResponse("test.html",{"request": request})