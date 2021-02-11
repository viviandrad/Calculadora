#Calculadora
#numero 1
#numero 2
#tipo da operação (+,-,*,/)
# A função mod calcula o resto da divisão. Por isso ao colocar % 2 e mod > 0, está validando se o resto é igual a zero ou não para saber se é even or odd).

import sys
try:
    numero1 = int(input("Insira o primeiro número: "))
    mod = numero1 % 2
    if mod > 0:
        print("This is an odd number.")
    else:
        print("This is an even number.")
    numero2 = int(input("Insira o segundo número: "))
    mod = numero2 % 2
    if mod > 0:
        print("This is an odd number.")
    else:
        print("This is an even number.")
    operacao = input("Selecione a operação ")

except ValueError:
    print("Digite somente números!")
    sys.exit(1)


if operacao == "+":
    print("Resultado da soma:", numero1, "+", numero2, "=", numero1 + numero2)
elif operacao == "-":
    print("Resultado da subtração:", numero1, "-", numero2, "=", numero1 - numero2)
elif operacao == "*":
    print("Resultado da multiplicação:", numero1, "*", numero2, "=", numero1 * numero2)
elif operacao == "/":
    try:
        print("Resultado da divisão:", numero1, "/", numero2, "=", numero1 / numero2)
    except ZeroDivisionError:
        print("Operação inválida: Não é possível realizar a divisão por 0!")
        sys.exit(1)
else:
    print("Operador não encontrado")

print("Fim do Cálculo!")
