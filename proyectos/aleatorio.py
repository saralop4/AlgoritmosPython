import os

os.system("cls")

def mayor(lista):
    may=lista[0]

    for i in lista:
        if may<i:
            may=i
    return may



def primo(x):
        if 1 <= x <= 2:
            return True
        elif x % 2 == 0:
         return False
        else:
            i = 3
            f = True
#while i < x and f:
  #      f = x % i != 0
   #     i += 2
  #         return f

def primos(lista):
    for item in lista:
        if primo(item):
            print(item)



def orden(lista):




    return 0




from random import randint

numeros=[]

for i in range(6):

    num=randint(1,20)

    numeros.append(num)

print(numeros)
print(mayor(numeros))
