from logic import Boletim


class Aplicacao:
    comandos = [
        (0, 'Notas: leitura de notas e cálculo de média'),
        (1, 'Cálculo de consoantes'),
        (2, 'ParesXImpares'),
        (3, 'Cálculo de média'),
        (4, 'Seleção de alunos'),
        (5, 'Temperatura anual'),
        (6, 'Classe das datas'),
        (7, 'Interrogatório'),
        (8, 'Ler valores'),
        (9,'Salário de funcionários'),
        (10, '')
    ]

    def __init__(self):
        self._exercicio = Exercicio()

    def executar(self):
        while True:
            self._exibir_menu()
            comando = input('> Selecione uma opcao acima: ')
            deve_sair = self.executar_comando(comando)
            if deve_sair:
                break
 
    def executar_comando(self, comando):
        if comando == '0':
            self._leitura_notas()
        elif comando == '1':
            self._calculo_consoantes()
        elif comando == '2':
            self._pares_impares()
        elif comando == '3':
            self._calculo_media()
        elif comando == '4':
            self._selecao_alunos()
        elif comando == '5':
            self._temperatura_anual()
        elif comando == '6':
            self._classe_datas()
        elif comando == '7':
            self._interrogatorio()
        elif comando == '8':
            self._ler_valores()
        elif comando == '9':
            self._salario_funcionarios()
        else:
            return True

    def _leitura_notas(self):
        nota1 = input('>Informe a primeira nota:')
        nota2 = input('> Informe a segunda nota: ')
        nota3 = input('> Informe a terceira nota:')
        nota4 = input('> Informe a quarta nota: ')
       
        boletim = Boletim(nota1, nota2, nota3, nota4)
        self._exercicio.boletim = boletim

    def _calculo_consoantes(self):
        print('Informe os dados: ')
        descricao = input('Descricao: ')
        codigo = input('Codigo: ')

        try:
            valor_unitario = float(input('Valor unitario: '))
            quantidade = int(input('Quantidade: '))
            desconto = int(input('Desconto: '))
        except ValueError:
            print('Informe um valor numerico!!!!')
            return

        produto = Produto(codigo=codigo, descricao=descricao, desconto=desconto,
                          valor_unitario=valor_unitario, quantidade=quantidade)
        self._carrinho.add_item(produto)

    def _pares_impares(self):
        codigo = input('Codigo: ')
        self._carrinho.incrementar_item(codigo)

    def _calculo_media(self):
        condigo = input('Código:')
        self._carrinho.decrementar_item(codigo)

    def _selecao_alunos(self):
        codigo = input('Codigo:')
        self._carrinho.remover_items(codigo)

    def _temperatura_anual(self):
        codigo = input('Codigo:')
        self._carrinho.exibir_resumo

    def _classe_datas(self):
        for op in Aplicacao.comandos:
            opcao, descricao = op
            print(f'[{opcao}] - {descricao}')
    def _interrogatorio(self):
        for op in Aplicacao.comandos:
            opcao, descricao = op
            print(f'[{opcao}] - {descricao}')
    def _ler_valores(self):
        for op in Aplicacao.comandos:
            opcao, descricao = op
            print(f'[{opcao}] - {descricao}')
    def _salario_funcionarios(self):
        for op in Aplicacao.comandos:
            opcao, descricao = op
            print(f'[{opcao}] - {descricao}')


app = Aplicacao()

app.executar()
