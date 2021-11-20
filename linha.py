from __future__ import annotations


class Linha:
    linha: list[float]

    def parse(input: str):
        return list(map(float, Linha(input.split(' '))))

    def __init__(self, linha: list[float]):
        self.linha = linha

    # multiplicação por escalar
    def __mul__(self, escalar: float):
        return Linha([n * escalar for n in self.linha])

    # adição de linhas
    def __add__(self, linha: Linha):
        if len(self) != len(linha):
            raise ValueError(
                'Linhas de tamanhos diferentes não podem ser somadas!')

        return Linha([self[i] + linha[i] for i in range(len(self))])

    def __len__(self):
        return len(self.linha)

    def __getitem__(self, key: int) -> int:
        return self.linha[key]

    def __setitem__(self, key: int, value: int):
        self.linha[key] = value

    def __str__(self):
        return str(self.linha)
