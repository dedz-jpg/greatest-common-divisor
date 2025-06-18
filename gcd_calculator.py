# Calculadora de Máximo Divisor Comum (GCD) - Projeto de Lógica de Programação

# Entrada de dados
a = int(input("Digite o primeiro número (A): "))
b = int(input("Digite o segundo número (B): "))

# Inicialização
gcd = 1
min_value = min(a, b)

# Loop para encontrar o GCD
for i in range(1, min_value + 1):
    if a % i == 0 and b % i == 0:
        gcd = i

# Saída
print(f"O Máximo Divisor Comum (GCD) entre {a} e {b} é: {gcd}")
