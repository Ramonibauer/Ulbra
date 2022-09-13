

altura=float(input("Digite a sua altura: "))
sexo=int(input("Digite 1 para mulher 2 para homem: "))
mulher=((62.1*altura)-44.7)
homem=((72.7*altura)-58)
if sexo==1:
    print(mulher)
else: 
    print(homem)
