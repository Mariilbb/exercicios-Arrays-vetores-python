import random

N = int(input("Digite o número de elementos do vetor: "))
vetor = []

while len(vetor) < N:
    num = int(input("Digite um número par: "))
    if num % 2 == 0:
        vetor.append(num)
    else:
        print("Esse numero não é par! ")

print(vetor)