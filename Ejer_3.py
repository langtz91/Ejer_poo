# Crea una clase llamada Empleado que tenga los atributos nombre , edad , y salario y
# que además, tenga los siguientes métodos:
# a. aumentar_salario - un método que toma un porcentaje como parámetro y
# aumenta el salario del empleado en ese porcentaje.
# b. mostrar_informacion - un método que imprime el nombre, la edad y el salario del
# empleado.

class Empleado:
    def __init__(self, nombre, edad, salario):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario
    
    def aumentar_salario(self, porcentaje):
        if porcentaje < 1 or porcentaje > 100:
            raise Exception("Porcentaje inválido")
        else:
            self.salario += self.salario * porcentaje / 100

    def mostrar_informacion(self):
        return f"{self.nombre} tiene {self.edad} años y se gana ${self.salario} anuales"
    
empleado1 = Empleado("Lan", 30, 100000)
try:
    empleado1.aumentar_salario(10)
except Exception:
    print("Hey loco que pasa vale mia? Pon un númerto válido")

print(empleado1.mostrar_informacion())

