from fastapi import FastAPI

app = FastAPI()

##Função Iniical da API 
@app.get("/")
def ola_mundo():
    return {"Hello": "World"}
