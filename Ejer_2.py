# Crear una clase llamada CuentaBancaria con las siguientes especificaciones:
# a. La clase debe tener los atributos numero_de_cuenta , saldo , y propietario .
# b. La clase debe tener un método para depositar dinero en la cuenta.
# c. La clase debe tener un método para retirar dinero de la cuenta.

class Cuentabancaria:
    def __init__(self, numero_de_cuenta, saldo, propietario, password):
        self.numero_de_cuenta = numero_de_cuenta
        self.saldo = saldo
        self.propietario = propietario
        self.password = password

    def depositar(self, numero_de_cuenta, valor_a_depositar):
        if self.numero_de_cuenta == numero_de_cuenta:
            self.saldo += valor_a_depositar 
            print("Operación realizada exitosamente") 
        else:
            print("Su dinero fue consigando a una cuenta bancaria diferente")
        
    def retirar(self, password, valor_a_retirar):
        if self.password == password:
            self.saldo -= valor_a_retirar
            print("Operación realizada exitosamente")
        else:
            print("Operación declinada")
        
cuenta_1 = Cuentabancaria(987654321, 5000000, "Isabela", "Isa123")
cuenta_1.depositar(987654321, 300000)
print(cuenta_1.saldo)

cuenta_1.depositar(887654321, 300000)
print(cuenta_1.saldo)

cuenta_1.retirar("Isa123", 1000000)
print(cuenta_1.saldo)

cuenta_1.retirar("robar", 1000000)
print(cuenta_1.saldo)



