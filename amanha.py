# Crie um programa que receba como entrada uma data, isto é,
# dd/mm/aaaa, e exiba o dia seguinte.
# Obs.: Caso a data seja inválida, o programa deverá alertar
#       o usuário e encerrar a execução.

from funcoes import *

def main():
    """Esta é a função principal, isto é, onde inicia
       a lógica do programa."""
    d, m, a = map(int, input('Data? ').split('/'))

    if valida(d, m, a):
        exibe_ds(d, m, a)
    else:
        print('Data inválida!')

main()
