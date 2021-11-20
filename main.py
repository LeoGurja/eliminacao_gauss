from matriz import Matriz
from functools import reduce
from gauss import eliminicao_de_gauss


def calcular_determinante(matriz: Matriz) -> float:
    try:
        eliminicao_de_gauss(matriz)
    except ValueError:
        return 0

    return reduce(
        lambda acc, curr: curr * acc,
        matriz.diagonal_principal()
    )


def obter_matriz():
    inputs = [input('linha 1: \n')]
    tamanho_da_matriz = len(inputs[0].split(' '))

    for i in range(1, tamanho_da_matriz):
        inputs.append(input(f'linha {i + 1}: \n'))

    return Matriz.parse(inputs)


matriz = obter_matriz()
if matriz.quadrada():
    print(f'o determinante é {calcular_determinante(matriz)}')
else:
    print(f'A matriz deve ser quadrada!')
