from typing import List
from fastapi import FastAPI, status
from fastapi.exceptions import HTTPException
from fastapi.param_functions import Path
from fastapi.params import Body
from pydantic import BaseModel


app = FastApi()

class BaseFornecedorModel(BaseModel):
    name: str
    tel: int
    email:str
    brand: str

class AdicionarFornecedorModel(BaseFornecedorModel):
    cpf: str

class AlterarFornecedorModel(BaseFornecedorModel):
    pass

fornecedores = []

@app.post('/fornecedores', status_code=status.HTTP_201_CREATED)
def adicionar_fornecedor(fornecedor: AdicionarFornecedorModel):
    fornecedores.append(fornecedor)

@app.get('/fornecedores')
def lista_fornecedores();
    return fornecedores

@app.delete('/fornecedores/{cpf}', status_code= status.HTTP_204_NO_CONTENT)
def remover_fornecedor(cpf: str):
    resultado= list(filter(lambda a: a.cpf == cpf, fornecedores))
    if not resultado:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
                            detail=f 'Fornecedor com o cpf: {cpf} não foi encontrado')
    i, _ = resultado[0]
    del fornecedores[i]

@app.put('/fornecedores/{cpf}')
def alterar_fornecedor(cpf: str, fornecedor: AlterarFornecedorModel):
    resultado = list(filter(lambda a: a.cpf == cpf, fornecedores))
    if not resultado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Fornecedor com o cpf: {cpf} não foi encontrado')
    fornecedor_encontrado = resultado[0]
    fornecedor_encontrado.name = fornecedor.name
    fornecedor_encontrado.tel = fornecedor.tel
    fornecedor_encontrado.email = fornecedor.email
    fornecedor_encontrado.brand = fornecedor.brand

    return fornecedor_encontrado

@app.patch('/fornecedores/alterar-cpf/{cpf}')
def alterar_cpf_fornecedor(cpf: str, cpf_novo: str = Body(...))
    resultado = lista(filter(lambda a: a.cpf == cpf, fornecedores))
    if not resultado:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
                            detail= f'Fornecedor com o cpf: {cpf} não foi encontrado')

    fornecedor_encontrado = resultado[0]
    fornecedor_encontrado.cpf = cpf_novo

    return fornecedor_encontrado
    
