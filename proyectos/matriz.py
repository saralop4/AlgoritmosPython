from random import randint



def calcula_media(*args):

    return(sum(*args)/len(*args))





def CrearM(m,n):

    C=list()

    for i in range(m):

        C.append(list())

        for j in range(n):

            C[i].append(randint(10,99))

    return C




def Transpuesta(A):

    m=len(A) # lo hago para obtener el numero de filas de la matriz

    n=len(A[0])# aplicando la funcion len() al primer elemento de la lista, que es una lista tambien, obtengo el numero de columnas

    T=[]

    for j in range(n):

        T.append([])

        for i in range(m):

            T[j].append(A[i][j])



    return T

       

           

A=CrearM(2,3)

B=Transpuesta(A)

for i in A:

    print(i)

print()

for i in B:

    print(i)