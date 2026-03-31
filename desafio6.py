print("=== CONVERSOR DE TEMPO ===\n")

print("Escolha uma opção:")
print("1 - Converter segundos para horas/minutos/segundos")
print("2 - Converter horas/minutos/segundos para segundos")

op = input("\n→ Opção: ")

# OPÇÃO 1
if op == "1":
    print("\nVocê escolheu: segundos → horas/minutos/segundos\n")
    
    segundos = int(input("Digite os segundos: "))

    horas = segundos // 3600
    resto = segundos % 3600
    minutos = resto // 60
    seg_final = resto % 60

    print(f"\nResultado: {horas}h {minutos}min {seg_final}s")

# OPÇÃO 2
elif op == "2":
    print("\nVocê escolheu: horas/minutos/segundos → segundos\n")
    
    horas = int(input("Horas: "))
    minutos = int(input("Minutos: "))
    segundos = int(input("Segundos: "))

    total = (horas * 3600) + (minutos * 60) + segundos

    print(f"\nResultado: {total} segundos")

else:
    print("\nOpção inválida")