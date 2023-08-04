
#Leia Leia 5 números inteiros  e some somente os valores impares e mostre a quantidade de impares for i in rage(5):
soma=0
cont=0
for i in range(5):
    num=int(input("informe um valor:"))
    if num%2!=0:
        soma+=num
        cont+=1
print("A soma dos ímpares e:",soma)
print("a soma dos impares e:",cont)