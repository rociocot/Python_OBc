'''Describe una funcion que pueda 
decirte si un año (número entero) es bisiesto o no'''

def aniobisiesto():

    anio:int=int(input("Ingrese un año para saber si es bisiesto: "))
    if (anio % 4 == 0 and(anio % 100 != 0 or anio % 400 == 0)):
        print(anio,"es un año bisiesto")
    else:
        print(anio, "no es un año bisiesto")  

aniobisiesto()        