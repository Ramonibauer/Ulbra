from tkinter import N


while True:
        valor=int(input("Digite o valor em R$: "))

        notas100=int(valor/100)
        resto100=valor%100
        notas50=int(resto100/50)
        resto50=resto100%50
        notas20=int(resto50/20)
        resto20=resto50%20
        notas10=int(resto20/10)
        resto10=resto20%10
        notas5=int(resto10/5)
        resto5=resto10%5
        notas2=int(resto5/2)
        resto2=resto5%2
        notas1=int(resto2)
        
        print(f"Para o valor R$: {valor} será necessário ")
        if notas100 > 0:
            print(f"{notas100} quantidade em notas de 100,00.")
        if notas50 > 0:
            print(f"{notas50} quantidade em notas de 50,00.")
        if notas20 > 0:
            print(f"{notas20} quantidade em notas de 20,00.")
        if notas10 > 0:
            print(f"{notas10} quantidade em notas de 10,00. ")
        if notas5 > 0:
            print(f"{notas5} quantidade em notas de 5,00.")
        if notas2 > 0:
            print(f"{notas2} quantidade em notas de 2,00.")
        if notas1 >0:
            print(f"{notas1} quantidade em notas de 1,00.")