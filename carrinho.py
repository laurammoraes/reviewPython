from typing import List


class Produto:
    def __init__(self, codigo: str, descricao: str, valor_unitario: float, quantidade: float, desconto: float):
        self.codigo = codigo
        self.descricao = descricao
        self.valor_unitario = valor_unitario
        self.quantidade = quantidade
        self.desconto = desconto

    def valor_final(self):
        return self.valor_unitario * self.quantidade

    def valor_com_desconto(self):
        return self.valor_unitario * self.quantidade - self.desconto


class Carrinho:
    def __init__(self) -> None:
        self._itens: List[Produto] = []

    def add_item(self, produto):
        self._itens.append(produto)

    def remover_item(self, codigo):
        resultado = list(
            filter(lambda i: i[1].codigo == codigo, enumerate(self._itens)))
        if resultado:
            indice, _ = resultado[0]
            del self._itens[indice]

    def incrementar_item(self, codigo, quantidade=1):
        resultado = list(
            filter(lambda i: i.codigo == codigo, self._itens))

        if resultado:
            produto = resultado[0]
            if produto.quantidade <= 3:
                produto.quantidade += quantidade

    def decrementar_item(self, codigo, quantidade=1):
        resultado = list(
            filter(lambda i: i.codigo == codigo, self._itens))

        if resultado:
            produto = resultado[0]
            if produto.quantidade == 1 or quantidade > produto.quantidade:
                self.remover_item(codigo)
            else:
                produto.quantidade -= quantidade

    def total_carrinho(self):
        valores = [p.valor_final() for p in self._itens]
        return sum(valores)


carrinho = Carrinho()
item1 = Produto('1', 'produto 1', 10, 2, 0)
item2 = Produto('2', 'produto 2', 14, 1, 12)
item3 = Produto('3', 'produto 3', 60, 4, 4)
item4 = Produto('4', 'produto 4', 70, 1, 20)

carrinho.add_item(item1)
carrinho.add_item(item2)
carrinho.add_item(item3)
carrinho.add_item(item4)

print(carrinho.total_carrinho())

carrinho.remover_item('4')
print(carrinho.total_carrinho())
