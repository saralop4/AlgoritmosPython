a = input("Digite el valor del primer lado")

b = input("Digite el valor del segundo lado")

c = input("Digite el valor del tercer lado")

a,b,c = float(a), float (b),float(c)



if (a>0 and b>0 and c>0) and (a+b > c or a+c >b or b+c > a):

    if (a==b==c):

        print ("El triángulo es equilatero")

    elif (a==b!=c) or (a==c!=b) or (b==c!= a):

        print ("Es isosceles")

    else:

        print ("Es escaleno")

else:

    print("Por favor digita valores positivos y que cumplan que la suma de dos lados sea igual al tercero")

    """ libras_presion=float(input("Escriba las libras de presion"))
temperatura=float(input(" Escriba la temperatura"))
if libras_presion>=25 or (temperatura>75 and temperatura<=95):
    print("alarma encendida")
else:
    print("alarma apagada")
    --------------------------------

    Se tienen 3 notas de 3 parciales; la primera nota vale el 20% . y la segunda y la tercera el 40% c/u. Haga un programa:

Averigue la nota definitiva
Valide si con los dos primeros parciales llevaba ganada la materia o no
Si la llevaba perdida averiguar cuanto necesitaba sacar en el tercer parcial para ganar la materia
    
    
    """
