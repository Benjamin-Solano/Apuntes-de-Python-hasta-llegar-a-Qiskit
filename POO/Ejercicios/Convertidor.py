# Objetivo: Crear una clase llamada convertidor, con los siguientes atributos
# pulgadas, pies y yardas, además, agregará los siguientes metodos de conversión
# centimetros a pulgadas, pulgadas a pies, pies a yardas
# finalmente crear un objeto que ponga a prueba las conversiones
# 1 pulgada = 2.54cm
# 1 pie = 12 pulgadas
# 1 yarda = 3 pies

class Convertidor:
    # Pulgadas
    def setPulgadas(self, valor):
        self.pulgadas = valor
    def getPulgadas(self):
        return self.pulgadas

    # pies
    def setPies(self, valor):
        self.pies = valor
    def getPies(self):
        return self.pies

    # yardas
    def setYardas(self, valor):
        self.yardas = valor
    def getYardas(self):
        return self.yardas

    # Metodos de conversión
    def Pulgada_a_Centimetro(self, valorPulgada):
        return valorPulgada * 2.54

    def Pie_a_Pulgada(self, valorPie):
        return valorPie * 12

    def Yarda_a_Pie(self, valorYarda):
        return valorYarda * 3

# =========== Fin de la Clase Convertidor ==============

convertidor = Convertidor()

pulgadas = float(input("Ingrese el valor en pulgadas a convertir a centimetros: "))
pies = float(input("Ingrese el valor en pies a convertir a pulgadas: "))
yardas = float(input("Ingrese el valor en yardas a convertir a pies: "))

print(f"\nLa conversion de {pulgadas} pulgadas a centimetros: {convertidor.Pulgada_a_Centimetro(pulgadas)}")
print(f"La conversion de {pies} pies a pulgadas: {convertidor.Pie_a_Pulgada(pies)}")
print(f"La conversion de {yardas} yardas a pies es: {convertidor.Yarda_a_Pie(yardas)}")    
        