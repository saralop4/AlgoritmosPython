Categorias = [ "Hipotension", "Optima", "Normal", "Normal-alta", "HTA Grado 1", "HTA Grado 2", "HTA Grado 3", "Hipertension Solo Sistolica"];

validar_sucursales = True
cnt_sucursales = 0

validar_pacientes = True
cnt_pacientes = 0

sucursales = []


#validar validar_sucursales
while validar_sucursales: 
  s = input()
  p= s.split()

  cnt_sucursales=int(p[0]) 
  cnt_pacientes=int(p[1]) 

  if( cnt_sucursales >= 1 ): validar_sucursales = False

#validar validar_pacientes
"""while validar_pacientes: 
  cnt_pacientes = int(input()) 
  if( cnt_sucursales >= 1 ): validar_pacientes = False """

for i in range(1,cnt_sucursales+1):
  
  #validar existencia por cada sucursal+
  validar_cnt_medicamento = True
  cnt_medicamento = 0
  while validar_cnt_medicamento: 
    cnt_medicamento = int(input()) 
    if( cnt_medicamento >= 1 ): 
      validar_cnt_medicamento = False

  sucursales.append({"sucursal_id":i, "cnt":cnt_medicamento,"init_cnt":cnt_medicamento})

#print(sucursales)

#Veroficar si una sucursal existe o no
def validateSucursal(sucursal_id):
  validate = False
  for sucursal in sucursales:
    if sucursal['sucursal_id'] == sucursal_id: validate = True
  return validate  

#Despachar a cada uno de los clientes
def dispatch(sucursal_id, case, medicamento, cnt):

  sucursal_exist = validateSucursal(sucursal_id)

  if(( case != 404) and sucursal_exist ):
    
   # print("Categoría: ", Categorias[case])
    #print("Sucursal: ",sucursal_id)

    if(medicamento):
      sucursales[sucursal_id-1]['cnt'] = sucursales[sucursal_id-1]['cnt'] - cnt;
   #   print("- ", cnt)
    #  print("quedan: ", sucursales[sucursal_id-1]['cnt'])

  #else: 
   # print("Sucursal no valida o categoria no encontrada")
  
#Pedir informacion de los clientes
for i in range(0,cnt_pacientes):

 # print("\nPaciente #",i+1)

  id= input()
  p= id.split()

  sucursal_id=int(p[0]) 
  presion_sistotica=int(p[1]) 
  presion_diastolica=int(p[2]) 

  if    ( presion_sistotica < 75  ) & ( presion_diastolica < 55 ): dispatch( sucursal_id, 0, True, 7  );
  elif ( ( (presion_sistotica >= 75) & (presion_sistotica < 114)  ) & ( (presion_diastolica >= 55) & (presion_diastolica < 74) ) ): dispatch( sucursal_id, 1, False, 0 );
  elif ( ( (presion_sistotica >= 115) & (presion_sistotica < 125)  ) & ( (presion_diastolica >= 75) & (presion_diastolica < 79) ) ): dispatch( sucursal_id, 2, False, 0  );
  elif ( ( (presion_sistotica >= 125) & (presion_sistotica < 134)  ) & ( (presion_diastolica >= 80) & (presion_diastolica < 84) ) ): dispatch( sucursal_id, 3, True, 1  );
  elif ( ( (presion_sistotica >= 135) & (presion_sistotica < 154)  ) & ( (presion_diastolica >= 85) & (presion_diastolica < 94) ) ): dispatch( sucursal_id, 4, True, 7  );
  elif ( ( (presion_sistotica >= 155) & (presion_sistotica < 174)  ) & ( (presion_diastolica >= 95) & (presion_diastolica < 104) ) ): dispatch( sucursal_id, 5, True, 15  );
  elif ( ( presion_sistotica >= 175  ) & ( presion_diastolica >= 105 ) ): dispatch( sucursal_id, 6, True, 30  );
  elif ( ( presion_sistotica >= 135  ) & ( presion_diastolica <85 ) ): dispatch( sucursal_id, 7, True, 15  );
  else:
    dispatch( sucursal_id, 404, False, 0)


#Output Final
#print("\nTotal: ")

listaOrdenada = sorted(sucursales, key=lambda k: k['cnt'])

print(f"{listaOrdenada[0]['sucursal_id']} {listaOrdenada[0]['cnt']}")
print(f"{listaOrdenada[len(listaOrdenada)-1]['sucursal_id']} {listaOrdenada[len(listaOrdenada)-1]['cnt']}")

for sucursal in sucursales:
  
  resta1 = sucursal['init_cnt']-sucursal['cnt']
  print( f"{sucursal['sucursal_id']} {(((resta1/sucursal['init_cnt'])*100)):.2F}%" );