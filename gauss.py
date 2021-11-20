from matriz import Matriz


def eliminicao_de_gauss(matriz: Matriz):
    for linha in range(len(matriz) - 1):
        pivo = matriz[linha][linha]

        if pivo == 0.0:
            pivo = encontra_outro_pivo(matriz, linha)

        zera_coluna_abaixo(matriz, pivo, linha)


def zera_coluna_abaixo(matriz: Matriz, pivo: int, linha_inicial: int):
    for linha in range(linha_inicial + 1, len(matriz)):
        multiplicador = -matriz[linha][linha_inicial] / pivo
        print(
            f'l{linha + 1} = l{linha + 1} + l{linha_inicial + 1} * {multiplicador}')
        matriz[linha] += matriz[linha_inicial] * multiplicador


def encontra_outro_pivo(matriz: Matriz, indice: int) -> int:
    linha = encontra_nao_zero_em_coluna(matriz, indice + 1, indice)
    matriz[indice], matriz[linha] = matriz[linha] * -1, matriz[indice]
    print(f'l{indice + 1} <-> -l{linha + 1}')
    return matriz[indice][indice]


def encontra_nao_zero_em_coluna(matriz: Matriz, indice: int, coluna: int) -> int:
    for i in range(indice, len(matriz)):
        if matriz[i][coluna] != 0:
            return i

    raise ValueError(
        f'Não há uma linha disponível com um valor diferente de zero na coluna {coluna}')
