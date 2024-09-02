import json

# Função para calcular o valor de SOMA
def calcular_soma(indice):
    soma = 0
    for k in range(1, indice + 1):
        soma += k
    print(f"O valor final de SOMA é: {soma}")

# Função para verificar se um número pertence à sequência de Fibonacci
def is_fibonacci_number(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b == n or n == 0

# Função para calcular o faturamento diário
def calcular_faturamento(faturamento):
    dias_com_faturamento = [dia for dia in faturamento if dia > 0]
    menor_faturamento = min(dias_com_faturamento)
    maior_faturamento = max(dias_com_faturamento)
    media_mensal = sum(dias_com_faturamento) / len(dias_com_faturamento)
    dias_acima_media = len([dia for dia in dias_com_faturamento if dia > media_mensal])

    return menor_faturamento, maior_faturamento, dias_acima_media

# Função para calcular o percentual de representação do faturamento por estado
def calcular_percentual_faturamento(faturamento):
    total = sum(faturamento.values())
    print("Percentual de representação por estado:")
    for estado, valor in faturamento.items():
        percentual = (valor / total) * 100
        print(f"{estado}: {percentual:.2f}%")

# Função para inverter uma string sem usar funções prontas
def inverter_string(s):
    resultado = ""
    for char in s:
        resultado = char + resultado
    return resultado

# Execução das funções com exemplos

# 1. Calcular SOMA
calcular_soma(13)

# 2. Verificar se um número pertence à sequência de Fibonacci
num = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))
if is_fibonacci_number(num):
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} NÃO pertence à sequência de Fibonacci.")

# 3. Cálculo do faturamento diário
with open('faturamento.json', 'r') as file:
    dados = json.load(file)
    faturamento_diario = dados['faturamento']

menor, maior, acima_media = calcular_faturamento(faturamento_diario)
print(f"Menor valor de faturamento: R${menor:.2f}")
print(f"Maior valor de faturamento: R${maior:.2f}")
print(f"Dias com faturamento acima da média: {acima_media}")

# 4. Cálculo do percentual de representação por estado
faturamento_estados = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

calcular_percentual_faturamento(faturamento_estados)

# 5. Inverter uma string
string = input("Digite uma string para inverter: ")
print("String invertida:", inverter_string(string))
