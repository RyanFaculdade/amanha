# Crie um programa que receba como entrada uma data, isto é,
# dd/mm/aaaa, e exiba o dia seguinte.
# Obs.: Caso a data seja inválida, o programa deverá alertar
#       o usuário e encerrar a execução.

def bissexto(a):
    """Recebe um número inteiro e devolve como resposta
       um valor booleano indicando se o ano é bissexto."""
    if (a % 4 == 0 and a % 100 != 0) or \
       (a % 400 == 0):
        return True
    else:
        return False

def dia_maximo(m, a):
    """Recebe um mês e um ano e retorna um número 
       inteiro que representa o dia máximo daquele mês."""
    if m == 2: 
        return 28 + bissexto(a)
    elif m == 4 or m == 6 or m == 9 or m == 11:
        return 30
    else:
        return 31

def valida(d, m, a):
    """Recebe uma data e devolve um valor booleano
       indicando se é uma data válida."""
    if a < 1: return False
    if m < 1 or m > 12: return False
    if d < 1 or d > dia_maximo(m, a): return False
    return True

def exibe_ds(d, m, a):
    """Recebe em seus parâmetros números inteiros,
       representando dia (d), mês (m) e ano (a).
       A função exibirá o dia seguinte."""
    d += 1
    if d > dia_maximo(m, a):
        d = 1
        m += 1
        if m > 12:
            m = 1
            a += 1

    print(f'{d}/{m}/{a}')

def main():
    """Esta é a função principal, isto é, onde inicia
       a lógica do programa."""
    d, m, a = map(int, input('Data? ').split('/'))

    if valida(d, m, a):
        exibe_ds(d, m, a)
    else:
        print('Data inválida!')

main()