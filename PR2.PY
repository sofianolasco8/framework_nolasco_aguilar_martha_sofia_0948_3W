print("nolasco_aguilar_martha_sofia_00948_3W")
class Cuenta:
    def __init__(self, titular, cantidad=0.0):#se inicia la lista 
        if not titular or not isinstance(titular, str):#indica si el nombre no es valido
            raise ValueError("El titular debe ser un nombre válido.")#manda mensaje de error 
        self._titular = titular
        self._cantidad = float(cantidad)

    @property
    def titular(self):#define titular
        return self._titular

    @property
    def cantidad(self):#define cantidad
        return self._cantidad

    def mostrar(self):#se juntan los dos valores en un solo mensaje 
        print(f"Titular: {self.titular}, Cantidad: {self.cantidad:.2f}")

    def ingresar(self, cantidad):#se juntan los dos valores en un solo mensaje
        if cantidad > 0:
            self._cantidad += cantidad

    def retirar(self, cantidad):#se juntan los dos valores en un solo mensaje
        if cantidad > 0:
            self._cantidad -= cantidad


cuenta = Cuenta("jorge perez", 100.0)
cuenta.mostrar()
cuenta.ingresar(3000)
cuenta.retirar(100)
cuenta.mostrar()
