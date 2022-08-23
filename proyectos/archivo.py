from os import system, remove

system("cls")



# Con esta instruccion abrimos un archivo de texto en modo escritura. Si este no exste lo crea

texto=["Manzanas\n","Peras\n","Uvas\n", "Mangos\n"]



miarchivo=open("mi_archivo.txt", "w")

miarchivo.writelines(texto)

miarchivo.close()

print(texto)



miarchivo=open("mi_archivo.txt", "r")

texto=miarchivo.read()

print(texto.split())