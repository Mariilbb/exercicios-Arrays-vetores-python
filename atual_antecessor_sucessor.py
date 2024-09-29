import random
N = 5

vetor = []

for i in range(5):
    vetor.append(random.randint(1,20))

print(vetor)

for i in range(1, len(vetor)-1):
    print("Valor atual:", vetor[i])
    print("Antecessor:", vetor[i-1])
    print("Sucessor:", vetor[i+1])
