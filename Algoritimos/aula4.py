#aula 4
num1=1
print("O número 1 é maior que 10", num1**2)   #modo de escrever incluindo a variavel

x=0
while x < 10:   #loop, ex: o a 9 (contador)
    print(x)
    x=x+1

x=0
while x < 10:   
   if x%2 ==0:  #x%2 ==0 para par, != impar +=, -=, *= ou /= ---control c para fechar o loop(interroper o processo) 
        print(x)
        x=x+1

while True:
    resposta=input("Qual a capital do Canadá? ") 
    if resposta == "Ottawa" or resposta == "ottawa":
        print("Acertou!")       
        break 
    else:
        print("Tente novamente")

variavel=["valor", "algoritmo", "itens"]
print(variavel[0]) #indice 0 é o primeiro:valor 
variavel[0] = "valor novo"   #aceitando alteração na lista, mostrando apenas um item da lista
print(variavel)

variavel=["valor", "algoritmo", "itens"]
cont=0
while cont <3:          #mostrar a lista
    print(variavel[cont]) #
    cont=cont+1

while True:
    cachorrocome=float(input("quantidade de raçao por dia em gramas: "))
    preço=float(input("preço por 10k"))
    pesoraçao=(int(input("Digite o quanto pesa (em gramas) o saco de raçao")))
    tempo=int(input("quantos dias?"))           #com o while True mantem o loop da pergunta
    rendimento=pesoraçao/cachorrocome           #selecionar tudo e colocar tab para identar 
    dias=tempo/rendimento
    total=dias*preço

    print(f"um saco de raçao necessário para {tempo} dias é de R$ {total:.2f}")