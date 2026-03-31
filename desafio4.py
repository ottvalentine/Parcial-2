print("=== CALCULADORA SIMPLES ===")
print("Siga as instruções abaixo:\n")

print("Passo 1: Digite o primeiro número")
num1 = float(input("→ Primeiro número: "))

print("\nPasso 2: Digite o segundo número")
num2 = float(input("→ Segundo número: "))

print("\nPasso 3: Escolha a operação digitando o símbolo")
print("+  para soma")
print("-  para subtração")
print("*  para multiplicação")
print("/  para divisão")

op = input("→ Operação: ")

print("\nPasso 4: Resultado")

if op == "+":
    print(f"{num1} + {num2} = {num1 + num2}")
elif op == "-":
    print(f"{num1} - {num2} = {num1 - num2}")
elif op == "*":
    print(f"{num1} * {num2} = {num1 * num2}")
elif op == "/":
    if num2 != 0:
        print(f"{num1} / {num2} = {num1 / num2}")
    else:
        print("Erro: não pode dividir por zero")
else:
    print("Operação inválida")