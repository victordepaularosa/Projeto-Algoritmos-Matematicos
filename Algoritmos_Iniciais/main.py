from atividade_01 import numeros_primos
from atividades_extras import sequencia_de_Fibonacci, fatorial, algoritmo_de_euclides
from menu import menu_principal

atividade = 10000

while atividade != 0:
    #Opções de atividade
    menu_principal()
    atividade = input('Qual atividade? ')
        
    if atividade == '0':
        atividade = int(atividade)
    
    elif atividade == '1':
        numeros_primos()
    
    elif atividade == '2':
        sequencia_de_Fibonacci()

    elif atividade == '3':
        fatorial()

    elif atividade == '4':
        algoritmo_de_euclides()

    else:
        print("Números inválidos!!!! \nPor favor inserir dados corretos!!!")    
