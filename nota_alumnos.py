#En este segundo ejercicio, tendréis que crear un programa que tenga una clase llamada Alumno
#  que tenga como atributos su nombre y su nota. Deberéis de definir los métodos para inicializar 
# sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.

#Creamos e inicializamos la clase Alumno
class Alumno():
    def __init__(self,nombre,nota):
        self.nombre=nombre
        self.nota=nota

    def __str__(self):
        return "Nombre del alumno: {}, Nota obtenida: {}".format(self.nombre,self.nota)

    def __ge__(self):
        if int (self.nota) > int (6):
            print("El alumno {} obtuvo un {} su condicion es Aprobado".format(self.nombre,self.nota))
        else:
            print("El alumno {} obtuvo un {} su condicion es No Aprobado".format(self.nombre,self.nota))

alumno1=Alumno("Rodriguez, José", 8)
print(alumno1)
alumno1.__ge__()

alumno2=Alumno("Juarez, Clara", 4)
print(alumno2)
alumno2.__ge__()