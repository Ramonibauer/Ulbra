num1 = 2
num2 = 2
teste=num1==num2
print(teste)

num3 = 2
num4 = 3
teste=num3==num4
print(teste)

num5 = int(input("num5")) #le apenas número inteiro, teria que colocar float para ex:10.25
num6 = input("num6") #le número ou letras
teste=num5==num6
print(teste)

plv=input("Digite um palavra: ")
print(len(plv))

#if
num1=int(input("Digite o primerio número: "))
num2=2
resto=num1&num2     #if=se else=senão
print(resto)
if resto==0:
    print("O número é par!")
else:
    print("O número é impar!")    

num7=int(input("Digite o primerio número: "))
num8=int(input("Digite o primerio número: "))
resto=num7&num8    
print(resto%2)
if num1!=num1:
    if resto == 0:
        print("O número é par!")
    else:
        print("O número é impar!")  
else: 
    print("Os números são iguais!")



senha=input("Digite a sua senha")
if senha=="123teste":
    print("Senha correta")
else:
    print("Senha incorreta")


peso=float(input("Digite seu peso: "))          #exemplo de elif
altura=float(input("Digite sua altura: "))
imc=peso/altura**2
print(imc)

if imc < 17:
    print("Seu IMC é: ", imc , "está muito abaixo do peso")
elif imc >= 17.01 and imc <18.49:
    print("Seu IMC é:" , imc , "e está abaixo do peso")
elif imc >= 18.50 and imc <24.99:
    print("Seu IMC é:" , imc , "e está normal do peso")
elif imc >= 25.00 and imc <29.99:
    print("Seu IMC é:" , imc , "e está acima do peso")
elif imc >= 30.00 and imc <39.99:
    print("Seu IMC é:" , imc , "e está muito acima do peso")

