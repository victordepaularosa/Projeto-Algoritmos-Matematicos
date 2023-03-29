

def sequencia_de_Fibonacci():
    elemento = int(input('Digite a quantidade de elementos que deseja na sequencia de Fibonacci: '))
    antepenultimo_elemento = 0
    ultimo_elemento = 1
    print(1, end=' ')
    for i in range(1, elemento):
        valor = ultimo_elemento + antepenultimo_elemento
        antepenultimo_elemento = ultimo_elemento
        ultimo_elemento = valor
        print(valor, end= ' ')
    print()

def fatorial():
    variavel = int(input("Digite um número inteiro para fazer seu fatorial: "))
    contador = 1
    for fatorial in range(1, variavel + 1):
        contador *= fatorial
    print(contador)

def algoritmo_de_euclides():
    n_dividido = int(input('Digite um número para ser o numerador: '))
    n_divisor = int(input('Digite um número para ser o denominador: '))
    n1 = n_dividido
    n2 = n_divisor

    while True:
        
        n_divisor_anterior = n_divisor
        n_divisor = n_dividido % n_divisor

        if n_divisor == 0:
            print(f'Como o último resto não nulo foi {n_divisor_anterior}, então o mdc({n1}, {n2}) = {n_divisor_anterior}')
            break
        n_dividido = n_divisor_anterior