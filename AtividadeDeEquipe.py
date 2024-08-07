import random
cont = 1
while True:
    
    numero_Digitado = int(input('Digite um numero de 1 a 10: '))
    numero_aleatorio = random.randint(1, 10)
    if numero_Digitado == numero_aleatorio:
        print(f'Você Digitou: ({numero_Digitado}) e o numero sorteado foi: ({numero_aleatorio}) Parabéns você acertou.')
        break
    elif cont == 3:
        print(f'Você Digitou: ({numero_Digitado}) e o numero sorteado foi: ({numero_aleatorio})')
        print(f'Você atingio as três tentativas:Não foi dessa vez')
        break
        
    else:
        print(f'Você Digitou: ({numero_Digitado}) e o numero sorteado foi: ({numero_aleatorio}) você errou. Vamos tentar mais uma Vez!')
        cont += 1
        
