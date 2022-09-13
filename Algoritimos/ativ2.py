NF=int(input("Digite o seu número de funcionário: "))
H=int(input("Digite o nº de horas trabalhadas: "))
V=int(input("Digite o valor das horas: "))
QF=int(input("Quantos filhos melhores de 14 anos você tem? "))
INF=int(input("Insira a sua idade: "))
TS=int(input("Digite o tempo de serviço: "))
SF=60.00*QF
SB=(H*V)+SF
INSS= (SB/100)*8.5
if SB > 1500:
    print(f"O funcionário {NF}, com salário bruto de R$ {SB:.2f} Valor do IR é R$ {(SB/100)*15:.2f} +INSS é de R$ {INSS:.2f} e o salário liquido de R$ {SB-INSS+SF-(SB/100)*15:.2f}")
elif SB >500 and SB <= 1500:
    print(f"O funcionário {NF}, com salário bruto de R$ {SB:.2f} Valor do IR é R$ {(SB/100)*8:.2f} +INSS é de R$ {INSS:.2f} e o salário liquido de R$ {SB-INSS+SF-(SB/100)*15:.2f}")
elif SB <=500:
    print(f"O funcionário {NF}, com salário bruto de R$ {SB:.2f} Valor do IR é R$ 0,00 +INSS é de R$ {INSS:.2f} e o salário liquido de R$ {SB-INSS+SF-(SB/100)*15:.2f}")