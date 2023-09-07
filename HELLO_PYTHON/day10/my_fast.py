from fastapi import FastAPI, Form, Request
import uvicorn
from starlette.responses import HTMLResponse
from fastapi.params import Form
from fastapi.templating import Jinja2Templates
import pymysql

conn = pymysql.connect(host='localhost', port=3305, user='root', passwd='python', db='python', charset='utf8')

curs = conn.cursor(pymysql.cursors.DictCursor)
sql = "select * from emp"
curs.execute(sql)
result = curs.fetchall()

templates = Jinja2Templates(directory="templates")
app = FastAPI()


@app.get("/", response_class=HTMLResponse)
@app.get("/emp_list", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse('emp_list.html',{'request':request,'empList':result})

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)


curs.close()
conn.close()