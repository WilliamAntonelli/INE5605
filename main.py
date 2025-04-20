from model.ativo_financeiro import AtivoFinanceiro
from model.despesa import Despesa
from model.meta import Meta
from model.usuario import Usuario
from util.enums import TipoDespesa, CategoriaDespesa, TipoPagamento, Genero, Parentesco, ClasseAtivo, TipoAtivo
from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}