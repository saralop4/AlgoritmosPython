#import os

#os.system("cls")

Categorias = [ "Hipotension", "Optima", "Normal", "Normal-alta", "HTA Grado 1", "HTA Grado 2", "HTA Grado 3", "Hipertension Solo Sistolica"];

validar_sucursales = True
cnt_sucursales = 0

validar_pacientes = True
cnt_pacientes = 0

sucursales = []


#validar validar_sucursales
while validar_sucursales: 
  cnt_sucursales = int(input())
  cnt_pacientes = int(input())  
  if( cnt_sucursales >= 1 ): validar_sucursales = False

#validar validar_pacientes
"""while validar_pacientes: 
  cnt_pacientes = int(input()) 
  if( cnt_sucursales >= 1 ): validar_pacientes = False """

for i in range(1,cnt_sucursales+1):
  
  #validar existencia por cada sucursal
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
  sucursal_id = int(input()) 
  presion_sistotica = int(input()) 
  presion_diastolica = int(input())

  if   ( ( presion_sistotica < 90  ) & ( presion_diastolica < 70) ): dispatch( sucursal_id, 0, True, 15  );
  elif ( ( (presion_sistotica >= 90) & (presion_sistotica < 130)  ) & ( (presion_diastolica >= 70) & (presion_diastolica < 90) ) ): dispatch( sucursal_id, 1, False, 0 );
  elif ( ( (presion_sistotica >= 130) & (presion_sistotica < 140)  ) & ( (presion_diastolica >= 90) & (presion_diastolica < 95) ) ): dispatch( sucursal_id, 2, False, 0  );
  elif ( ( (presion_sistotica >= 140) & (presion_sistotica < 150)  ) & ( (presion_diastolica >= 95) & (presion_diastolica < 100) ) ): dispatch( sucursal_id, 3, True, 10  );
  elif ( ( (presion_sistotica >= 150) & (presion_sistotica < 170)  ) & ( (presion_diastolica >= 100) & (presion_diastolica < 110) ) ): dispatch( sucursal_id, 4, True, 10  );
  elif ( ( (presion_sistotica >= 170) & (presion_sistotica < 190)  ) & ( (presion_diastolica >= 110) & (presion_diastolica < 120) ) ): dispatch( sucursal_id, 5, True, 20  );
  elif ( ( presion_sistotica >= 190  ) & ( presion_diastolica >= 120 ) ): dispatch( sucursal_id, 6, True, 50  );
  elif ( ( presion_sistotica >= 150  ) & ( presion_diastolica < 100 ) ): dispatch( sucursal_id, 7, True, 20  );
  else:
    dispatch( sucursal_id, 404, False, 0)


#Output Final
#print("\nTotal: ")

listaOrdenada = sorted(sucursales, key=lambda k: k['cnt'])

print(f"{listaOrdenada[0]['sucursal_id']} {listaOrdenada[0]['cnt']}")
print(f"{listaOrdenada[len(listaOrdenada)-1]['sucursal_id']} {listaOrdenada[len(listaOrdenada)-1]['cnt']}")

for sucursal in sucursales:
  
  resta1 = sucursal['init_cnt']-sucursal['cnt']
  print( f"{sucursal['sucursal_id']} {(((resta1/sucursal['init_cnt'])*100)):.2F}%" )




