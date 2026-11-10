# Esta es la clase persona, tiene un nombre, puedo cambiar el nombre,
# además puedo obtener su nombre y saludar.

class Persona:
    # Constructor con parametros
    def __init__(self, nombre, cedula, edad):
        self.nombre = nombre
        self.cedula = cedula
        self.edad = edad

    # nombre
    def setNombre(self, nombre):
        self.nombre = nombre
    def getNombre(self):
        return self.nombre
    # Cedula
    def setCedula(self, cedula):
        self.cedula = cedula
    def getCedula(self):
        return self.cedula
    # Edad
    def setEdad(self, edad):
        self.edad = edad
    def getEdad(self):
        return self.edad

    # Metodos
    def Saludar(self):
        print(f"Hola! soy {self.nombre} y mi edad es {self.edad} años.")
# ============= Fin de clase =============
    

persona = Persona("Benjamin", 118480367, 24)
persona.Saludar()
