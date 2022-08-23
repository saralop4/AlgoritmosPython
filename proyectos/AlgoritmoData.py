import statistics
import os

os.system("cls")
print("************************")
n= int(input("Digite la cantidad: "))
print("************************")
map=[]
map1=[]

for i in range(n):

    pais= input("Pais: ")
    valor= int(input("Cantidad Poblacional: "))
    map1.append(pais)
    map.append(valor)


moda= statistics.mode(map)
media = statistics.mean(map)    
mediana = statistics.median(map) 

print("******************************************************************************")

print("Paises= ",map1," -    Cantidad de Personas= ",map)

print("*******************************************")
print("Moda= ",moda)
print("Media= ",media)
print("Mediana= ",mediana)
print("*******************************************")