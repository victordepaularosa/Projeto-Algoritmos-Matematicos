from math import sqrt


def formula_de_bhaskara():
    a = float(input("Digite o valor de A do seu X²: "))
    b = float(input("Digite o valor de B de X: "))
    c = float(input("Digite o valor da constante: "))

    delta = (b**2) -4*a*c

    if delta > 0:
        valor_positivo = (-b + sqrt(delta))/(2*a)
        valor_negativo = (-b - sqrt(delta))/(2*a)
        print("A sua equação tem dois valores reais, sendo eles:")
        print(f'{valor_positivo:.2f} e {valor_negativo:.2f}')

    elif delta == 0:
        valor = -b/(2*a)
        print("A sua equação tem um valor real, sendo ele:")
        print(f'{valor:.2f}')

    else:
        print(f"A sua equação não tem valores reais.")


if __name__ == "__main__":
    formula_de_bhaskara()
