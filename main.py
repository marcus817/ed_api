from fastapi import FastAPI
from typing import List, Dict, Any, Optional
from pydantic import BaseModel
app = FastAPI()

class Produto(BaseModel):
    id: int
    titulo: str
    descricao: Optional[str]
    preco: float

produtos: List[Dict[str, Any]] = [
    {
        "id":1,
        "titulo": "Cadeira Gamer",
        "descricao":  "Cadeira confortável para fazer live",
        "preço": 5.0
    },
    {
        "id":2,
        "a titulo": "Workshop",
        "descricao": "Workshop de Deploy",
        "preco": 100.0
    },
    {
        "id":3,
        "a titulo":"Iphone",
        "descricao":"Iphone 14",
        "preco": None
    }
]

id_atual = 3 

def lista(self):
    return self.produtos

def inserir(self, item: Dict[str, any]) -> Dict[str, any]:
    self.id_atual += 1
    item["id"] = self.id_atual
    return self.produtos.append(item)
 
@app.get("/produtos")
def listar_produtos():
    return produtos
##Função Iniical da API 
@app.get("/")
def ola_mundo():
    return {"Hello": "World"}

