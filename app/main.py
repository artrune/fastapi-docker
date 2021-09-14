from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import random

nombres = ["Jorge", "Arturo", "Rodolfo", "Pinwinazo"]

class Alumno(BaseModel):
    name:str
    matricula:str

alumnos = [Alumno(name=nombre, matricula="a1701635"+str(random.randint(1,10))) for nombre in nombres]

app = FastAPI(docs_url="/")

@app.get("/alumnos")
async def alumnos():
    return alumnos

if __name__=="__main__":
    uvicorn.run("main:app",host='localhost', port=8080, reload=True, debug=True)