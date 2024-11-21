print("nolasco_aguilar_martha_sofia_0948_3W")
class Persona:#inicia una clase
    def __init__(self, nombre='', edad=0, dni=''):#define los valores dentro de la clase
   
        self.nombre = nombre #define nombre
        self.edad = edad #define nombre
        self.dni = dni #define el DNI

  
    
    def nombre(self):
        return self._nombre#regresa a nombre 

  
    def nombre(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("El nombre debe ser una cadena no vacía.")
        self._nombre = value

  
    def edad(self):
        return self._edad #regresa edad

    
    def edad(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("La edad debe ser un número entero positivo.")
        self._edad = value

    
    def dni(self):
        return self._dni #regresa el dni

    
    def dni(self, value):
        if not value.isdigit() or len(value) != 8:
            raise ValueError("El DNI debe contener exactamente 8 dígitos.")
        self._dni = value

    def imprimir(self):
       
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"DNI: {self.dni}")

    def esMayorDeEdad(self):
       
        return self.edad >= 18

try:
    persona = Persona("Junior", 26, "12345678")
    persona.imprimir()
    print("¿Es mayor de edad?", persona.esMayorDeEdad())

    persona.edad = -5  
except ValueError as e:
    print(f"Error: {e}")
