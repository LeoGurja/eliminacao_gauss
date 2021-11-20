from linha import Linha


class Matriz:
    linhas: list[Linha]

    def parse(inputs: list[str]):
        return Matriz(list(map(Linha.parse, inputs)))

    def __init__(self, linhas: list[list[int]]):
        self.linhas = list(map(Linha, linhas))

    def quadrada(self) -> bool:
        tamanho_esperado = len(self)
        for linha in self.linhas:
            if tamanho_esperado != len(linha):
                return False

        return True

    def diagonal_principal(self) -> Linha:
        if not self.quadrada():
            raise ValueError('Matriz deve ser quadrada!')

        return Linha([self[i][i] for i in range(len(self))])

    def __len__(self):
        return len(self.linhas)

    def __getitem__(self, key: int) -> Linha:
        return self.linhas[key]

    def __setitem__(self, key: int, value: Linha):
        self.linhas[key] = value

    def __str__(self):
        return '\n'.join(map(str, self.linhas))
