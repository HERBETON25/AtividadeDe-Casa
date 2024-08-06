import random
while True:
    numero_Digitado = int(input('Digite um numero: '))
    numero_aleatorio = random.randint(1, 10)
    if numero_Digitado == numero_aleatorio:
        print(f'Você Digitou ({numero_Digitado}) e o numero sorteado foi ({numero_aleatorio}) então você acertou.')
        break
    else:
        print(f'Você Digitou ({numero_Digitado}) e o numero sorteado foi ({numero_aleatorio}) éntão você errou. Digite novamente!')
print('Você acertou então o programa encerrou!')