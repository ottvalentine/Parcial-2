print(" === JUROS SIMPLES === \n")

print("Passo 1: Digite o capital (C)")
C = float(input("→ Capital: "))

print("\nPasso 2: Digite a taxa de juros (%)")
I = float(input("→ Taxa (%): "))

print("\nPasso 3: Digite o tempo")
T = float(input("→ Tempo: "))

print("\nPasso 4: Calculando...")

J = (C * I * T) / 100

print(f"\nResultado: O juros é {J}")