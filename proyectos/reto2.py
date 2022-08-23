cantidad_medicamento1= int(input())
cantidad_medicamento2= int(input())
pacientes=0
pacientes1=0
pacientes2=0


first = True

while (cantidad_medicamento1>0 and cantidad_medicamento2>0) | first :

    first = False
    presion_sistolica = int(input())
    presion_diastolica = int(input())

    if presion_sistolica<91 and presion_diastolica<63: 
                                            
                                            if cantidad_medicamento2>0:
                                                                cantidad_medicamento2-=12
                                                                pacientes+=1
                                                                pacientes2+=1  
    elif presion_sistolica>=91 and presion_sistolica<=133  and presion_diastolica>=63 and presion_diastolica<=76: 
                                                                              
                                                                               pacientes+=1  
    elif presion_sistolica>=134 and presion_sistolica<=161  and presion_diastolica>=77 and presion_diastolica<=104: 
                                                                       
                                                                        pacientes+=1   
    elif presion_sistolica>=162 and presion_sistolica<=187  and presion_diastolica>=105 and presion_diastolica<=118: 
                                                                       
                                                                        if cantidad_medicamento1>0:
                                                                            cantidad_medicamento1-=1
                                                                            pacientes+=1  
                                                                            pacientes1+=1
    elif presion_sistolica>=188 and presion_sistolica<=200  and presion_diastolica>=119 and  presion_diastolica<=125: 
                                                                          
                                                                           if cantidad_medicamento1>0:
                                                                            cantidad_medicamento1-=8
                                                                            pacientes+=1
                                                                            pacientes1+=1    
    elif presion_sistolica>=201 and presion_sistolica<=213  and presion_diastolica>=126 and presion_diastolica<=145: 
                                                                          
                                                                          if cantidad_medicamento1>0:
                                                                            cantidad_medicamento1-=12
                                                                            pacientes+=1 
                                                                            pacientes1+=1                                                                                                                          
    elif presion_sistolica>=214  and presion_diastolica>=146:      
                                                      
                                                       if cantidad_medicamento1>0:
                                                                            cantidad_medicamento1-=32
                                                                            pacientes+=1 
                                                                            pacientes1+=1  
    elif presion_sistolica>=152  and presion_diastolica<79:      

                                                     if cantidad_medicamento1>0:
                                                                            cantidad_medicamento1-=20
                                                                            pacientes+=1 
                                                                            pacientes1+=1 
    else:
        pacientes+=1

num=pacientes        

print(f"{num}")
if pacientes1 > 0 :
    resta1= num-pacientes1
    print(f"{pacientes1} {(100 - ((resta1/num)*100)):.2F}%")
else:   
    print(f"{0} {(0.00):.2F}%")  

if pacientes1 > 0 :
    resta2= num-pacientes2
    print(  f"{pacientes2} {(100 - ((resta2/num)*100)):.2F}%"  )
else:
    print(f"{0} {(0.00):.2F}%")      