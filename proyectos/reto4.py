from audioop import reverse


Categorias = [ "Hipotension", "Optima", "Normal", "Normal-alta", "HTA Grado 1", "HTA Grado 2", "HTA Grado 3", "Hipertension Solo Sistolica"];

validar_info = True
cnt_sucursales = 0
cnt_medicamentos = 0
cnt_pacientes = 0
sucursales = []


# validar sucursales
while validar_info: 
 #aqui
  info = input()
  datos = info.split()

  if( (int(datos[0]) > 0) & (int(datos[1]) > 0) & (int(datos[2]) > 0)): 
    cnt_sucursales=int(datos[0]) 
    cnt_medicamentos=int(datos[1]) 
    cnt_pacientes=int(datos[2]) 
    validar_info = False

for i in range(1,cnt_sucursales+1):

  medicamentos_local_list = []
 #aqui
  existencias = input()
  existencias = existencias.split()

  if(len(existencias) == cnt_medicamentos):
    for i2 in range(0,cnt_medicamentos):
      medicamentos_local_list.append({ "id_medicamento":i2+1, "init_cnt": int(existencias[i2]), "cnt": int(existencias[i2]) })
    
  sucursales.append({ "sucursal_id":i, "medicamentos": medicamentos_local_list, "atendidos":0 })
  # sucursales.append({"sucursal_id":i, "cnt":cnt_medicamento,"init_cnt":cnt_medicamento})
#aqui
#print(sucursales)

#Verificar si una sucursal existe o no
def validateSucursal(sucursal_id):
  validate = False
  for sucursal in sucursales:
    if sucursal['sucursal_id'] == sucursal_id: validate = True
  return validate  

#Despachar a cada uno de los clientes
def dispatch(sucursal_id, case, id_dispatch, medicamento_id, cnt_medicamento_id):

  sucursal_exist = validateSucursal(sucursal_id)

  if(( case != 404) ):
    
    #print("Categoría: ", Categorias[case])
    #print("Sucursal: ",sucursal_id)
    #print("Medicamento: ",medicamento_id)

    if(id_dispatch):

      ctn = sucursales[sucursal_id-1]['medicamentos'][medicamento_id-1]['cnt']
      sucursales[sucursal_id-1]['medicamentos'][medicamento_id-1]['cnt'] = int(ctn) - int(cnt_medicamento_id)
      # sucursales[sucursal_id-1]['cnt'] = sucursales[sucursal_id-1]['cnt'] - cnt_medicamento_id;
     # print("- ", cnt_medicamento_id)
  sucursales[sucursal_id-1]['atendidos'] = int(sucursales[sucursal_id-1]['atendidos']) + 1
     # print("quedan: ", sucursales[sucursal_id-1]['medicamentos'][medicamento_id-1]['cnt'])

  
#Pedir informacion de los clientes
for i in range(0,cnt_pacientes):
  a = input()
  datos = a.split()

  sucursal_id = int(datos[0]) 
  medicamento_id = int(datos[1]) 
  cnt_medicamento_id =  int(datos[2]) 
  presion_sistotica = int(datos[3]) 
  presion_diastolica = int(datos[4]) 

  if   ( ( presion_sistotica < 90  ) & ( presion_diastolica < 70) ): dispatch( sucursal_id, 0, True, medicamento_id, cnt_medicamento_id  )
  elif ( ( (presion_sistotica >= 90) & (presion_sistotica < 130)  ) & ( (presion_diastolica >= 70) & (presion_diastolica < 90) ) ): dispatch( sucursal_id, 1, False, medicamento_id, cnt_medicamento_id )
  elif ( ( (presion_sistotica >= 130) & (presion_sistotica < 140)  ) & ( (presion_diastolica >= 90) & (presion_diastolica < 95) ) ): dispatch( sucursal_id, 2, False, medicamento_id, cnt_medicamento_id )
  elif ( ( (presion_sistotica >= 140) & (presion_sistotica < 150)  ) & ( (presion_diastolica >= 95) & (presion_diastolica < 100) ) ): dispatch( sucursal_id, 3, True, medicamento_id, cnt_medicamento_id )
  elif ( ( (presion_sistotica >= 150) & (presion_sistotica < 170)  ) & ( (presion_diastolica >= 100) & (presion_diastolica < 110) ) ): dispatch( sucursal_id, 4, True, medicamento_id, cnt_medicamento_id )
  elif ( ( (presion_sistotica >= 170) & (presion_sistotica < 190)  ) & ( (presion_diastolica >= 110) & (presion_diastolica < 120) ) ): dispatch( sucursal_id, 5, True, medicamento_id, cnt_medicamento_id )
  elif ( ( presion_sistotica >= 190  ) & ( presion_diastolica >= 120 ) ): dispatch( sucursal_id, 6, True, medicamento_id, cnt_medicamento_id )
  elif ( ( presion_sistotica >= 150  ) & ( presion_diastolica < 100 ) ): dispatch( sucursal_id, 7, True, medicamento_id, cnt_medicamento_id )
  else: dispatch( sucursal_id, 404, False, medicamento_id, cnt_medicamento_id )


#Output Final
#print("\nTotal: ")

VectorEntregados = []
list_medicamento_1 = []



for i in range(0,cnt_sucursales):
   VectorlistaOrdenada = []
   ListaInicial = sucursales[i]["medicamentos"]
   for i2 in range(0,len(ListaInicial)):
      encargados = ListaInicial[i2]['init_cnt'] - ListaInicial[i2]['cnt']
      VectorlistaOrdenada.append(encargados)
      
   VectorEntregados.append(VectorlistaOrdenada)
   

for i in range(0, cnt_sucursales):
  
    ListaInicial = sucursales[i]["medicamentos"]
    list_medicamento_1.append({"sucursal_id":sucursales[i]['sucursal_id'],"cnt": ListaInicial[0]['init_cnt'] - ListaInicial[0]['cnt']})

    print(sucursales[i]['sucursal_id'])
    lista_ordenada = sorted(sucursales[i]["medicamentos"], key=lambda k: k['cnt'])
    print(f"{lista_ordenada[0]['id_medicamento']} {lista_ordenada[0]['cnt']}")
    print(f"{lista_ordenada[len(lista_ordenada)-1]['id_medicamento']} {lista_ordenada[len(lista_ordenada)-1]['cnt']}")

    sum=0
    for j in VectorEntregados[i]:
        sum+=j

    atendidos = 0
    for i3 in range(0, cnt_sucursales):
        if(i3 == i):
         atendidos += sucursales[i]["atendidos"]  

    print(f"{min(VectorEntregados[i]):.2f} {sum/cnt_medicamentos:.2f} {max(VectorEntregados[i]):.2f}")

    
    if  atendidos !=0:
        print(f"{sum/atendidos:.2f}")
    else:
        print(f"{0:.2f}")

  
min_medicamento_1 = sorted(list_medicamento_1, key=lambda k: k['cnt'])[0] 
max_medicamento_1 = sorted(list_medicamento_1, key=lambda k: k['cnt'], reverse=True)[0] 
print(f"{min_medicamento_1['sucursal_id']} {min_medicamento_1['cnt']}")
print(f"{max_medicamento_1['sucursal_id']} {max_medicamento_1['cnt']}")