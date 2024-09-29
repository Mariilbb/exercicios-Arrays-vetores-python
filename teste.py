# Vetor de 1 a 10
vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Passo 1: Calcular a média
soma = 0
for num in vetor:
    soma += num
media = soma / len(vetor)

# Passo 2: Calcular a soma dos quadrados das diferenças
soma_quadrados_diferencas = 0
for num in range:
    soma_quadrados_diferencas += (num - media) ** 2

# Passo 3: Calcular a média dos quadrados das diferenças
media_quadrados_diferencas = soma_quadrados_diferencas / len(vetor)

# Passo 4: Tirar a raiz quadrada da média dos quadrados das diferenças
desvio_padrao = media_quadrados_diferencas ** 0.5

print("Desvio Padrão:", desvio_padrao)
