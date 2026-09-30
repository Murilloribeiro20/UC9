import random
numero_secreto = random.randint(1, 5)
# print(numero_secreto)
num_tentativas = 0
print("Bem-vindo ao jogo de adivinhação!\nTente adivnhar um número entre 1 e 1000.")
while True:
    palpite = int(input("\nDigite um Número: "))
    print(type(palpite))
    num_tentativas =+1 
    if (palpite == numero_secreto): 
        print("👏👏👏👏👏👏👏👏👏👏👏")
2    elif(palpite < numero_secreto): 
        print("O número secreto é maior")
    else:
        print("O número secreto é menor!")