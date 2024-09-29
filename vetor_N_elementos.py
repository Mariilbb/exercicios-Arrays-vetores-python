import random

N = int(input("Digite o número de elementos do vetor: "))
vetor = []

for i in range (N):
    vetor.append(random.randint(0,100))

print(vetor)