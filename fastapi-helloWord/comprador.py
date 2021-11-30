from typing import List
from fastapi import FastAPI, status
from fastapi.exceptions import HTTPException
from fastapi.param_functions import Path
from fastapi.params import Body
from pydantic import BaseModel


app = FastApi()

class BaseCompradorModel(BaseModel):
    name: str
    tel: int
    email: str

    

class AdicionarCompradorModel(BaseCompradorModel):
    cpf: str

class AlterarCompradorModel(BaseCompradorModel):
    pass

compradores = []

@app.post('/compradores', status_code=status.HTTP_201_CREATED)
def adicionar_comprador(comprador: AdicionarCompradorModel):
    compradores.append(comprador)

@app.get('/compradores')
def lista_compradores();
    return compradores

@app.delete('/compradores/{cpf}', status_code= status.HTTP_204_NO_CONTENT)
def remover_comprador(cpf: str):
    resultado= list(filter(lambda a: a.cpf == cpf, compradore))
    if not resultado:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
                            detail=f 'Comprador com o cpf: {cpf} não foi encontrado')
    i, _ = resultado[0]
    del compradores[i]

@app.put('/compradores/{cpf}')
def alterar_comprador(cpf: str, comprador: AlterarCompradorModel):
    resultado = list(filter(lambda a: a.cpf == cpf, compradores))
    if not resultado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Comprador com o cpf: {cpf} não foi encontrado')
    comprador_encontrado = resultado[0]
    comprador_encontrado.name = comprador.name
    comprador_encontrado.tel = comprador.tel
    comprador_encontrado.email = comprador.email

    

    return comprador_encontrado

@app.patch('/compradores/alterar-cpf/{cpf}')
def alterar_cpf_comprador(cpf: str, cpf_novo: str = Body(...))
    resultado = lista(filter(lambda a: a.cpf == cpf, compradores))
    if not resultado:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
                            detail= f'Comprador com o cpf: {cpf} não foi encontrado')

    comprador_encontrado = resultado[0]
    comprador_encontrado.cpf = cpf_novo

    return comprador_encontrado
    
