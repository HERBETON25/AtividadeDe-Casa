# 1. Leia idade, sexo (m/f/x) e salário  de N habitantes, e ao final exiba
# - A maior idade
# - A menor idade
# - A quantidade de mulheres
# - Maior salario
# - Menor salario
# - Media salarial
# - Idade e sexo da pessoa com o maior salario
#  Encerre o programa quando uma idade negativa for digitada


idade = 0
sal = 0
IdadeMaior = 0
IdadeMenor = 0
SalarioMaior = 0
SalarioMenor = 0
sexo = 'x'
sexoTotal = 'x'
salarioT = 0
idade2 = 0
sexo2 = 0
SalarioTotal = 0
habitantesT = 0
while True:
    idade = int(input('Digite a idade: ou Digite a idade com (-)Negativo para sair: '))
    if idade >= 0:
        sexo = str(input('Digite seu sexo (M)masculino ou (F)feminino ou (x)desconhecido: '))
        salario = float(input('Digite seu salario: '))
        habitantes = float(input('Digite o numero de habitantes: '))

        sal = sal + ( salario * habitantes)
        SalarioTotal = SalarioTotal + salario 
        habitantesT = habitantesT + habitantes
        
        if idade >= IdadeMaior:
            IdadeMaior = idade

        if idade < IdadeMenor or IdadeMenor == 0:
            IdadeMenor = idade

        if salario >= SalarioMaior:
            SalarioMaior = salario

        if salario < SalarioMenor or SalarioMenor == 0:
            SalarioMenor = salario

        if sexo == 'M' or sexo == 'm':
            sexoTotal = sexo
            

        if salario >= SalarioMaior:
            idade2 = idade
            sexo2 = sexo
            
        

    elif idade < 0:
       
        SalarioTotal = ( habitantesT * SalarioTotal ) 
        print('Sua idade é nagativa você esta saindo...')
        break
        
            
        
sal = sal / habitantesT 
print('-------------------- resultado --------------------------')
print(f'a maior idade é: {IdadeMaior}')
print(f'a menor idade é: {IdadeMenor}')
print(f'a quantidade de mulheres é: {habitantesT}')
print(f'o maior salario é: {SalarioMaior}')
print(f'o menor salario é: {SalarioMenor}')
print(f'a media salarial é: {sal:.2f}')
print(f'a pessoa com maior salario tem a idade: {idade2} e é do sexo: {sexo2}')
print('-------- fim do projeto ----------')