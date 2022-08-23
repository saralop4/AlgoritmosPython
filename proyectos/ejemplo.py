#Este ejemplo nos muestra el poder y versatilidad de Python y sus estructuras de datos

# Creamos una lista lllamadas programas y guardamos en ella dos funciones ( ..si dos funciones)

# para poder usarlas como un menu de programas

# Las listas y el resto de estructuras de datos en Python nos permiten guardar cualquier tipo de clases

#y sus instancias



# Aca definimos dos funciones sencillas para demostrar lo mencionado

def suma(i,j):

    return i+j

def potencia(x,n):

    return x**n



# Aca inicializamos la lista programas

programas=[]

# Aqui con el metodo append guardamos en la posicion 0 la funcion suma

programas.append(suma)

# y nuevamente,  con el metodo append guardamos en la posicion 1 la funcion potencia

programas.append(potencia)



# Aca hacemos un menu de opciones para que el usuario escoga 0 o 1 dependiendo si quiere sumar o elevar a una potencia

print(programas) # Aca sin necesidad de un for imprimo la estructura ( lista )

print("         Menu ")

print(" 0. Programa de Suma")

print(" 1. Programa de Potencias")

# Aca le solicito al usuario del programa que digite la opcion y luego los dos literales

opcion=int(input(" Escoja opcion"))

a=int(input())

b=int(input())

# Dependiendo si el usuario escoge 0 o 1 y dependiendo de la respuesta uso la opcion como un indice y ejecuta la

# funcion que necesita

resultado= programas[opcion](a,b)

print("El resultado de la operacion escogida es -->", resultado)