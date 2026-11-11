# El objetivo es crear una clase calculadora con 2 atributos a y b, con los
# metodos tipicos set y get, además de poseer metodos de calculo como
# sumar, restar, multiplicar, división entera, modulo y división normal

class Minicalculadora:
    def __init__(self):
        self.valorA = 0
        self.valorB = 0

    # Valor A
    def setValorA(self, val):
        self.valorA = val
    def getValorA(self):
        return self.valorA

    # Valor B
    def setValorB(self, val):
        self.valorB = val
    def getValorB(self):
        return self.valorB

    # Metodos de Calculo
    def Suma(self):
        print(f"Suma entre {self.valorA} y {self.valorB} es: {self.valorA + self.valorB}")

    def Resta(self):
        print(f"Resta entre {self.valorA} y {self.valorB} es: {self.valorA - self.valorB}")

    def Producto(self):
        print(f"Producto entre {self.valorA} y {self.valorB} es {self.valorA * self.valorB}")

    def DivisionEntera(self):
        print(f"División entera entre {self.valorA} y {self.valorB} es {self.valorA // self.valorB}")

    def DivisionNormal(self):
        print(f"División Normal entre {self.valorA} y {self.valorB} es {self.valorA / self.valorB}")

    def DivisionResiduo(self):
        print(f"Residuo de una división normal entre {self.valorA} y {self.valorB} es {self.valorA % self.valorB}")

# ===================== FIN CLASE MINICALCULADORA ======================

calculadora = Minicalculadora()

a = int(input("Ingrese el valor de A: "))
b = int(input("Ingrese el valor de B: "))

calculadora.setValorA(a)
calculadora.setValorB(b)


calculadora.Suma()
calculadora.Resta()
calculadora.Producto()
calculadora.DivisionEntera()
calculadora.DivisionNormal()
calculadora.DivisionResiduo()
    