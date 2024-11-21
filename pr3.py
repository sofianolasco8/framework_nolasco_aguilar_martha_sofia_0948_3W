print(" ")
print("nolasco_aguilar_martha_sofia_0948_3W")

class Cuenta:#se abre la clase
    def __init__(self, titular, cantidad=0.0): #se definen los valores de la clase
        self.titular = titular
        self.cantidad = cantidad

    def ingresar(self, cantidad):#se definen los valores de la clase
        if cantidad > 0:
            self.cantidad += cantidad

    def retirar(self, cantidad):#se definen los valores de la clase
        self.cantidad -= cantidad

    def mostrar(self):#se definen los valores de la clase
        print(f"Titular: {self.titular}, Cantidad: {self.cantidad:.2f}")

class CuentaJoven(Cuenta):#se abre otra clase
    def __init__(self, titular, cantidad=0.0, bonificacion=0.0):#se definen los valores de la otra clase 
        super().__init__(titular, cantidad)
        self.bonificacion = bonificacion

    def esTitularValido(self):#se definen los valores de la otra clase 
        return 18 <= self.cantidad < 25

    def retirar(self, cantidad):#se definen los valores de la otra clase 
        if self.esTitularValido():#si el titular es valido 
            super().retirar(cantidad)
        else:#si el titular no es valido 
            print("No se puede retirar dinero: el titular no es válido.")#se imprime mensaje de error 

    def mostrar(self):#se define otro valor de la clase 
        print(f"Cuenta Joven - Titular: {self.titular}, Cantidad: {self.cantidad:.2f}, Bonificación: {self.bonificacion}%")#imprime mensaje 

cuenta_joven = CuentaJoven("javier", cantidad=20, bonificacion=10)#imprime mensaje 
cuenta_joven.mostrar()#imprime mensaje 

cuenta_joven.ingresar(200)#imprime mensaje 
cuenta_joven.mostrar()#imprime mensaje 

cuenta_joven.retirar(100)#imprime mensaje 
cuenta_joven.mostrar()#imprime mensaje 

cuenta_joven.cantidad = 30  #imprime mensaje 
cuenta_joven.retirar(60)#imprime mensaje 

