# Hacer una clase llamada Password con las siguientes especificaciones:
# a. La clase debe tener los atributos longitud y password . La longitud por defecto
# será de 8.
# b. La clase debe tener un método que indique si la contraseña es fuerte teniendo
# en cuenta que para ser fuerte debe tener mínimo una longitud de 6.
# c. La clase debe tener un método para cambiar la contraseña.

class Password:
    def __init__(self, longitud, password):
        self.longitud = len(password)
        self.password = password

    def seguridad_password(self, password):
        if len(password) < 6:
            print("Nivel de seguridad de contraseña débil")
        else: 
            print("Nivel de seguridad de contraseña fuerte")

    def nuevo_password(self, password_actual, new_password):
        if password_actual == self.password:
            self.password = new_password
            self.longitud = len(self.password)
            print("Su contraseña fue cambiada exitosamente")
        else:
            print("Contraseña actual incorrecta")

password_1 = Password("", "isa12")
print(password_1.longitud)
print(password_1.password)
password_1.seguridad_password("isa12")

password_1.nuevo_password("isa12", "isabelagutierrez")
print(password_1.longitud)
print(password_1.password)
password_1.seguridad_password("isabelagutierrez")

password_1.nuevo_password("isabelagutierrez", "isa")
print(password_1.longitud)
print(password_1.password)
password_1.seguridad_password("isa")

