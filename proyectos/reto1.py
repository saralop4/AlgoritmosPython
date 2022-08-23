hemoglobina= int(input())
genero= int(input())

if hemoglobina<13.2 and genero==1: 
                                print("alerta 1")
elif hemoglobina<11.6 and genero==2: 
                                print("alerta 1")
elif hemoglobina>=13.2 and hemoglobina<=16.6 and genero==1: 
                                                    print("sin alerta")
elif hemoglobina>=11.6 and hemoglobina<=15 and genero==2: 
                                                    print("sin alerta")   
elif hemoglobina>16.6 and genero==1: 
                                print("alerta 2")   
elif hemoglobina>15 and genero==2: 
                            print("alerta 2")
                                                       
elif genero!=2 and genero!=1: 
                        print("no es posible generar la alerta")  
 