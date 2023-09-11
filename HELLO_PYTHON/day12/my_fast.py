from fastapi import FastAPI, Form, Request
import uvicorn
from starlette.responses import HTMLResponse
from fastapi.params import Form
from fastapi.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def forw(request: Request):
    return templates.TemplateResponse('forw.html', {'request':request})


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)