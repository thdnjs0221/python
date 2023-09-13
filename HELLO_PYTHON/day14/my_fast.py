from fastapi import FastAPI, Form, Request
import uvicorn
from starlette.responses import HTMLResponse, RedirectResponse
from fastapi.params import Form
from fastapi.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles
from pydantic.main import BaseModel
from day11.daomember import DaoMem


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

class Item(BaseModel):
    m_id: str

class Mem(BaseModel):
    m_id: str =None
    m_name: str =None
    tel: str =None
    email: str =None
    
@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return RedirectResponse(url="/static/member.html")



@app.post("/mem_select")
def mem_select(e:Mem):
    #return {"item_id": item.id, "item_description": item.description}
    print(e)
    me=DaoMem()
    list=me.selectList()
    return {"list": list}

@app.post("/mem_select_one")
def mem_select_one(e:Mem):
    m_id=e.m_id
    me=DaoMem()
    emp=me.selectOne(m_id)
    return {"emp": emp}

@app.post("/mem_insert")
def mem_insert(e:Mem):
    me=DaoMem()
    cnt=me.insert(e.m_id, e.m_name, e.tel, e.email)
    return {"cnt": cnt}



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)