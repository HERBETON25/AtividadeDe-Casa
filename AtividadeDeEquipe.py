inicio = int(input("Digite o início do intervalo: ")) 
fim = int(input("Digite o fim do intervalo: ")) 

somaPares = 0 

for numero in range(inicio, fim + 1):
    if numero % 2 == 0: 
        somaPares += numero

if somaPares == 0:
    print("Não há números pares no intervalo.")
else:
    print(f"A soma dos números pares no intervalo é: {somaPares}")