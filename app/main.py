from fastapi import FastAPI, BackgroundTasks, HTTPException, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
import crud
import models
import schemas
from utils import perform_translation_with_chatgpt
from database import get_db, engine

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

# set up Jinja2 templates
templates = Jinja2Templates(directory="templates")

@app.get('/index', response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# enable CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],  # Allows all origins
    allow_credentials = True,
    allow_methods = ["*"],  # Allows all methods
    allow_headers = ["*"],  # Allows all headers
)

@app.post('/translate', response_model=schemas.TaskResponse)
def translate(request: schemas.TranslationRequest, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    task = crud.create_translation_task(db, request.text, request.languages)
    background_tasks.add_task(perform_translation_with_chatgpt, task.id, request.text, request.languages, db)
    return {"task_id": task.id}

@app.get('/translate/{task_id}', response_model=schemas.TranslationStatus)
def get_translate(task_id: int, db: Session = Depends(get_db)):
    task = crud.get_translation_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="task not found!")
    return {"task_id": task.id, "status": task.status, "translations": task.translations}

@app.get('/translate/content/{task_id}', response_model=schemas.TranslationContent)
def get_translate_content(task_id: int, db: Session = Depends(get_db)):
    task = crud.get_translation_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="task not found!")
    return {"translations": task.translations}
