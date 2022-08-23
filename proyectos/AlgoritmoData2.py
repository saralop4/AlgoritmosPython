import statistics
import os
os.system("cls")

f=open("DataColombianos.csv")
data=f.read()
#print(data)
f.close()
data=data.split("\n")
campos=data.pop(0).split(',')
#print(campos)
lista=[]
for i in range(len(data)-1):
        info= data[i].split(',')
        #print(info)
        elemento={}
        for j,llave in enumerate(campos):
            elemento[llave]=info[j]
            #print(elemento)
        lista.append(elemento)
        #print(lista)
    #return lista

cantidadTotal=0
ctn=0
vector=[]
print("PAISES", "                    ", "CANTIDAD DE PERSONAS")
print(" ")

for i in lista:

    ctn += 1
    cantidadTotal+=int(i['cantidad_de_personas'])
    pais=i['paises']
    personas=int(i['cantidad_de_personas'])
    vector.append(personas)
    print(pais,"                    ",personas)
 

moda = statistics.mode(vector)
#media = statistics.mean(personas)   
media = cantidadTotal/(ctn) 
mediana = statistics.median(vector) 

print("*********************************************************")
print("Moda = ",moda)
print(f"Media = {media:.2f}")
print("Mediana = ",mediana)
print(f"Total de personas en el extranjero =  {cantidadTotal}")
print("*********************************************************")
