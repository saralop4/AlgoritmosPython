mAlert1=0
fAlert1=0
mAlert2=0
fAlert2=0
mSinAlert=0
fSinAlert=0
cont=0

personas= int(input())
while cont<personas:
    validarGenero = True
    while validarGenero:
        hemoglobina = float(input()) 
        genero=int(input())

        if( (genero == 1) | (genero == 2 ) ):
         validarGenero = False

    cont+=1
    if hemoglobina<13.2 and genero==1: 
                                mAlert1+=1
    elif hemoglobina<11.6 and genero==2: 
                               fAlert1+=1
    elif hemoglobina>=13.2 and hemoglobina<=16.6 and genero==1: 
                                                 mSinAlert+=1
    elif hemoglobina>=11.6 and hemoglobina<=15 and genero==2: 
                                                    fSinAlert+=1
    elif hemoglobina>16.6 and genero==1: 
                                mAlert2+=1  
    elif hemoglobina>15 and genero==2: 
                       fAlert2+=1  
 

print(f"{fAlert1} {fAlert2} {fSinAlert} {mAlert1} {mAlert2} {mSinAlert}")       
 