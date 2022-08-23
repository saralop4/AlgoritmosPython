from os import system
def entrega_med(ps, pd):
    if ps<90 and pd <70:
        return True
    elif 90<=ps<130 and 70<=pd<90:
        return False
    elif 130<=ps<140 and 90<=pd<95:
        return False
    elif 140<=ps<150 and 95<=pd<100:
        return True
    elif 150<=ps<170 and 100<=pd<110:
        return True
    elif 170<=ps<190 and 110<=pd<120:
        return True
    elif ps >= 190 and pd >=120:
        return True
    elif ps >= 150 and pd < 100:
        return True
    else:
        return False
system("cls")
f=open("archivodedatos.txt","r")
datos = f.read()
f.close()
lista = datos.split("\n")
n,k,m=lista[0].split()
n,k,m=int(n),int(k),int(m) # n es numeros de sucursales, k tipos de medicamentios., m numero de pacientes
existencias=[lista[i+1].split() for i in range(n)]
for i in range(n):
    for j in range(k):
        existencias[i][j]=int(existencias[i][j])
entregas_p=[[ 0 for i in range(k)] for i in range(n)]
pacientes_suc=[0 for i in range(n)]
pacientes_tipo_m=[0 for i in range(k)]

for i in range(m):
    suc, tipo_m, cant, ps, pd = lista[n+i+1].split()
    suc, tipo_m, cant, ps, pd = int(suc), int(tipo_m), int(cant), int(ps), int(pd)
    if entrega_med(ps,pd):
        entregas_p[suc-1][tipo_m-1]+=cant
    pacientes_suc[suc-1]+=1
    pacientes_tipo_m[tipo_m-1]+=1

existencias_finales=[[ existencias[i][j]- entregas_p[i][j] for j in range(k)] for i in range(n)]
for  i, valor in enumerate(existencias_finales):
    print(f"{i+1}")
    print(f"{valor.index(min(valor))+1}  {min(valor)}")
    print(f"{valor.index(max(valor))+1}  {max(valor)}")
    sum=0
    for j in entregas_p[i]:
        sum+=j
    print(f"{min(entregas_p[i]):.2f} {sum/k:.2f} {max(entregas_p[i]):.2f}")
    if pacientes_suc[i] !=0:
        print(f"{sum/pacientes_suc[i]:.2f}")
    else:
        print(f"{0:.2f}")



















