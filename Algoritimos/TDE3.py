#Exercicio 1-
num1=int(input("Digite o primerio número: "))
num2=int(input("Digite o segundo número: "))
if num1%2 ==0:
    print("O primeiro número é par!")
else:
    print("O primeiro número é impar!")
if num2%2 ==0:
    print("O segundo número é par!")
else:
    print("O segundo número é impar!")

if num1 < 10:
    print("O primeiro número é menor que 10!")
else:  
    print("O primeiro número é maior que 10!")

if num2 < 10:
    print("O primeiro número é menor que 10!")
else:  
    print("O primeiro número é maior que 10!")


quadrado1=num1**2
quadrado2=num2**2
print(f"O número ao quadrado do primeiro número é: {quadrado1} \nO número ao quadrado do segundo número é {quadrado2}")

resto3=num1%2
resto4=num2%2
print(f"O resto da divisão do primeiro número é: {resto3} \nO resto da divisão do segundo número é: {resto4}")

soma=num1+num2
print("O valor da soma dos dois número é: ",soma)