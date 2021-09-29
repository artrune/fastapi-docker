from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
class Alumno(BaseModel):
    name:str
    matricula:str

nombres=  [("Jorge", "a17016351"), ("Arturo","a17016352"), ("Rodolfo","a17016353"), ("Pinwinazo","a17016355")]
alumnos = [Alumno(name=nombre, matricula=matricula) for nombre, matricula in nombres]

def get_alumnos():
    return alumnos

app = FastAPI(docs_url="/")

@app.get("/alumnos")
async def api_alumnos():
    return get_alumnos()

if __name__=="__main__":
    uvicorn.run("main:app",host='localhost', port=8081, reload=True, debug=True)