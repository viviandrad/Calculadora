#Calculadora
#numero 1
#numero 2
#tipo da operação (+,-,*,/)

numero1 = int(input("Insira o primeiro número: "))
numero2 = int(input("Insira o segundo número: "))
operacao = input("Selecione a operação ")


if operacao == "+":
    print("Resultado da soma:", numero1, "+", numero2, "=", numero1 + numero2)
elif operacao == "-":
    print("Resultado da subtração:", numero1, "-", numero2, "=", numero1 - numero2)
elif operacao == "*":
    print("Resultado da multiplicação:", numero1, "*", numero2, "=", numero1 * numero2)
elif operacao == "/":
    print("Resultado da divisão:", numero1, "/", numero2, "=", numero1 / numero2)
else:
    print("Operador não encontrado")

print("Fim do Cálculo!")
