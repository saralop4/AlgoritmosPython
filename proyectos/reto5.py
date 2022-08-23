f=open("data.csv")
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

#datos=leer_csv("data.csv")
total=0
num_hombres=0
num_mujeres=0
nom_ciudad=""
nom_dpto=""
cantidadTotal=0
media=0
pacientes = 0
id = input()
for i in lista:
    
    if i['id_branch']==id:
      
        atendido = False

        if   ( ( int(i['systolic_pressure']) < 91  ) & ( int(i['diastolic_pressure']) < 63) ): atendido = True
        elif ( ( (int(i['systolic_pressure']) >= 91) & (int(i['systolic_pressure']) < 134)  ) & ( (int(i['diastolic_pressure']) >= 63) & (int(i['diastolic_pressure']) < 77) ) ): atendido = False
        elif ( ( (int(i['systolic_pressure']) >= 134) & (int(i['systolic_pressure']) < 162)  ) & ( (int(i['diastolic_pressure']) >= 77) & (int(i['diastolic_pressure']) < 105) ) ):  atendido = False
        elif ( ( (int(i['systolic_pressure']) >= 162) & (int(i['systolic_pressure']) < 188)  ) & ( (int(i['diastolic_pressure']) >= 105) & (int(i['diastolic_pressure']) < 119) ) ):  atendido = True
        elif ( ( (int(i['systolic_pressure']) >= 188) & (int(i['systolic_pressure']) < 201)  ) & ( (int(i['diastolic_pressure']) >= 119) & (int(i['diastolic_pressure']) < 126) ) ):  atendido = True
        elif ( ( (int(i['systolic_pressure']) >= 201) & (int(i['systolic_pressure']) < 214)  ) & ( (int(i['diastolic_pressure']) >= 126) & (int(i['diastolic_pressure']) < 146) ) ):  atendido = True
        elif ( ( int(i['systolic_pressure']) >= 214  ) & ( int(i['diastolic_pressure']) >= 146 ) ):  atendido = True
        elif ( ( int(i['systolic_pressure']) >= 152  ) & ( int(i['diastolic_pressure']) < 77 ) ):  atendido = True
        else: False
       
       
        if(atendido):

            pacientes += 1
            cantidadTotal+=int(i['medicine_quantity'])
            
            if i['gender']=='m':
                num_hombres+=1
            if i['gender']=='f':
                num_mujeres+=1
            nom_ciudad=i['city_name']
            nom_dpto=i['department_name']


        
media = cantidadTotal/(pacientes)

print(f'{id} {nom_ciudad} {nom_dpto}')
print('scheduled patients')
print(f'male {num_hombres}')
print(f'female {num_mujeres}')
print(f'total {num_hombres+num_mujeres}')
print('scheduled medicine quantity')
print(f"mean {media:.2f}")
print(f"total {cantidadTotal}")








