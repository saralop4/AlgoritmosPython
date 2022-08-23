



#def leer_csv(nombre):
f=open("data.csv")
data=f.read()
#print(data)
f.close()
data=data.split("\n")
campos=data.pop(0).split(',')
print(campos)
lista=[]
for i in range(len(data)):
        info= data[i].split(',')
        #print(info)
        elemento={}
        for j,llave in enumerate(campos):
            elemento[llave]=info[j]
            #print(elemento)
        lista.append(elemento)
        #print(lista)
    #return lista

#datos=leer_csv("data.csv")
num=0
num_mujeres=0
num_mujeres_c=0
for i in lista:
    if i['gender']=='f':
        num_mujeres+=1
        if i['city_name']=='Barranquilla': 
            num_mujeres_c+=1
    num+=1
print(f'De {num} pacientes atendidos   son mujeres {num_mujeres} y  de Barranqulla son {num_mujeres_c} ')


