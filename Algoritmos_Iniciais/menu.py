from os import system

def limpa_tela():
    return system('cls')

#Cabeçalho das atividades intermediarias
def menu_principal():
    print()
    titulo = 'ESCOLHA AS ATIVIDADES DE NÍVEL INTERMEDIÁRIO!'
    print('*'*50)
    print(titulo.center(50))
    print('*'*50)
    print('[0] Sair')
    print('[1] Números primos \n[2] Sequência de Fibonacci')
    print('[3] Número Fatorial \n[4] Algoritmo de Euclides')
    print('[5] Fórmula de Bhaskara')
    print()