

def presiones(cantidad_medicamento1):

    while (cantidad_medicamento1>0):

      presion_sistolica = int(input())
      presion_diastolica = int(input())

    if presion_sistolica<90 and presion_diastolica<70: 
                                            
                                            if cantidad_medicamento1>0:
                                                                cantidad_medicamento1-=15
                                                                pacientes+=1
                                                                
    elif presion_sistolica>=90 and presion_sistolica<=129  and presion_diastolica>=70 and presion_diastolica<=89: 
                                                                              
                                                                               pacientes+=1  
    elif presion_sistolica>=130 and presion_sistolica<=139  and presion_diastolica>=90 and presion_diastolica<=94: 
                                                                       
                                                                        pacientes+=1   
    elif presion_sistolica>=140 and presion_sistolica<=149  and presion_diastolica>=95 and presion_diastolica<=99: 
                                                                       
                                                                        if cantidad_medicamento1>0:
                                                                            cantidad_medicamento1-=10
                                                                            pacientes+=1  
                                                                            
    elif presion_sistolica>=150 and presion_sistolica<=169  and presion_diastolica>=100 and  presion_diastolica<=109: 
                                                                          
                                                                           if cantidad_medicamento1>0:
                                                                            cantidad_medicamento1-=10
                                                                            pacientes+=1
                                                                           
    elif presion_sistolica>=170 and presion_sistolica<=189  and presion_diastolica>=110 and presion_diastolica<=119: 
                                                                          
                                                                          if cantidad_medicamento1>0:
                                                                            cantidad_medicamento1-=20
                                                                            pacientes+=1 
                                                                                                                                                                                                     
    elif presion_sistolica>=190  and presion_diastolica>=120:      
                                                      
                                                       if cantidad_medicamento1>0:
                                                                            cantidad_medicamento1-=50
                                                                            pacientes+=1 
                                                                             
    elif presion_sistolica>=150  and presion_diastolica<100:      

                                                     if cantidad_medicamento1>0:
                                                                            cantidad_medicamento1-=20
                                                                            pacientes+=1 
                                                                            
    else:
        pacientes+=1


  



while True:
    cantidad_sucursales = int(input("ingrese cantidad de sucursal: "))  
    cantidad_pacientes= int(input("ingrese total de pacientes: "))
    #print("entro al primero while")
  
    while True:
        if (cantidad_sucursales<1):
                                 break
                                                          
        elif(cantidad_sucursales>=1):
          
            while True:
                cantidad_medicamentos=int(input("ingrese cantidad medicamento: "))
                while True:
                  if (cantidad_medicamentos<1):
                                 break
                  elif(cantidad_medicamentos>=1):
                    print("entro al bucle de crear sucursales")


