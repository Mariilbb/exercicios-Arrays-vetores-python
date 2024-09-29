vetor = []
soma = 0

for i in range (1,101):
    vetor.append(i)

print(vetor)

for i in range(50):
    soma+=vetor[i] + vetor[100 - i -1]

print(soma)