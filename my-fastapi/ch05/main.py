import uvicorn
from fastapi import FastAPI
from starlette.templating import Jinja2Templates
from starlette.requests import Request
from ch05.web import todo as todo_web
from ch05.service import todo as todo_service

app = FastAPI()
app.include_router(todo_web.router)
templates = Jinja2Templates(directory='templates')

@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request,
                                                     "todos":todo_service.find_all()})



if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)