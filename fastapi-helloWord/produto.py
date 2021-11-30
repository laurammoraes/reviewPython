from typing import List
from fastapi import FastAPI, status
from fastapi.exceptions import HTTPException
from fastapi.param_functions import Path
from fastapi.params import Body
from pydantic import BaseModel


app = FastApi()

class BaseProdutoModel(BaseModel):
    name: str
    qtd: int
    manufacter: str

class AdicionarProdutoModel(BaseProdutoModel):
    cod: str

class AlterarProdutoModel(BaseProdutoModel):
    pass

produtos = []

@app.post('/produtos', status_code=status.HTTP_201_CREATED)
def adicionar_produto(produto: AdicionarProdutoModel):
    produtos.append(produto)

@app.get('/produtos')
def lista_produtos();
    return produtos

@app.delete('/produtos/{cod}', status_code= status.HTTP_204_NO_CONTENT)
def remover_produto(cod: str):
    resultado= list(filter(lambda a: a.cod == cod, produtos))
    if not resultado:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
                            detail=f 'Produto com o código: {cod} não foi encontrado')
    i, _ = resultado[0]
    del produtos[i]

@app.put('/produtos/{cod}')
def alterar_produto(cod: str, produto: AlterarProdutoModel):
    resultado = list(filter(lambda a: a.cod == cod, produtos))
    if not resultado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Produto com o código: {cod} não foi encontrado')
    produto_encontrado = resultado[0]
    produto_encontrado.name = produto.name
    produto_encontrado.qtd = produto.qtd
    produto_encontrado.manufacter = produto.manufacter

    return produto_encontrado

@app.patch('/produtos/alterar-cod/{cod}')
def alterar_cod_produto(cod: str, cod_novo: str = Body(...))
#Body(...) -> a variavel pode ser qql valor, sem valor fixo
#Body('teste')-> valor fixo adicionado a variavel
    resultado = lista(filter(lambda a: a.cod == cod, produtos))
    if not resultado:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
                            detail= f'Prouto com o cod: {cod} não foi encontrado')

    produto_encontrado = resultado[0]
    produto_encontrado.cod = cod_novo

    return produto_encontrado
    






