
def is_prime(i):
    qtd_numeros = []

    for primo in range(1, i + 1):
        testar_numero = i / primo
        if testar_numero - int(testar_numero) == 0:
            qtd_numeros.append(primo)
              
    if len(qtd_numeros) == 2:
        return True
    else:
        return False

def numeros_primos():

    n1 = int(input("Digite o primeiro número inteiro: "))
    n2 = int(input("Digite o segundo número inteiro: "))

    if n1 > 0 and n2 > 0:
        print()
        print(f"Os números que são primos entre {n1} e {n2} são:  ")
        for i in range(n1, n2 + 1):
            primo = is_prime(i)
            if primo:
                print(f"{i} ", end=" ")
        print() 
    else:
        print()
        print("Números inválidos!!!! \nÉ necessário que ambos os números sejam positivos!!!")

# Rodar esse código aqui e não no menu!!!
if __name__ =="__main__":
    numeros_primos()
