from typing import List
from fastapi import FastAPI, status
from fastapi.exceptions import HTTPException
from fastapi.param_functions import Path
from fastapi.params import Body
from pydantic import BaseModel


app = FastApi()

class BaseCategoriaModel(BaseModel):
    name: str
    

class AdicionarCategoriaModel(BaseCategoriaModel):
    cod: str

class AlterarCategoriaModel(BaseCategoriaModel):
    pass

categorias = []

@app.post('/categorias', status_code=status.HTTP_201_CREATED)
def adicionar_categoria(categoria: AdicionarCategoriaModel):
    categorias.append(categoria)

@app.get('/categoria')
def lista_categorias();
    return categorias

@app.delete('/categorias/{cod}', status_code= status.HTTP_204_NO_CONTENT)
def remover_categoria(cod: str):
    resultado= list(filter(lambda a: a.cod == cod, categorias))
    if not resultado:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
                            detail=f 'Categoria com o cod: {cod} não foi encontrado')
    i, _ = resultado[0]
    del categorias[i]

@app.put('/categorias/{cod}')
def alterar_categoria(cod: str, categoria: AlterarCategoriaModel):
    resultado = list(filter(lambda a: a.cod == cod, categorias))
    if not resultado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Categoria com o cod: {cod} não foi encontrado')
    categoria_encontrado = resultado[0]
    categoria_encontrado.name = categoria.name
    

    return categoria_encontrado

@app.patch('/categorias/alterar-cod/{cod}')
def alterar_cod_categoria(cod: str, cod_novo: str = Body(...))
    resultado = lista(filter(lambda a: a.cod == cod, categorias))
    if not resultado:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
                            detail= f'Categoria com o cod: {cod} não foi encontrado')

    categoria_encontrado = resultado[0]
    categoria_encontrado.cod = cod_novo

    return categoria_encontrado
    
