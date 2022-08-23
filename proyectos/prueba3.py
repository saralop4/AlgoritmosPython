from os import system

system("cls")

# Si m o n no son validos debe pedir ingresar los datos

entrada=input()

valores=entrada.split()

    # Dado que en una linea me entrega dos valores separados por espacio en blanco

    # uso el metodo split para dividir la cadena y obtener los valores

n=int(valores[0]) # n es el número de sucursales

m=int(valores[1]) # m es el número de pacientes

print(n,m)