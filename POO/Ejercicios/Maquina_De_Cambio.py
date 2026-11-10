# Objetivo: crear una clase que reciba el precio de un articulo
# y la cantidad con la que paga el usuario, se debe retornar el vuelto
# con el minimo de mondeas de 500, 100, 50 y 25 a una persona que
# ha pagado con efectivo.

class Maquina:
    def __init__(self):
        self.monedas500 = 0
        self.monedas100 = 0
        self.monedas50 = 0
        self.monedas25 = 0

    # monedas de 500 colones
    def setMonedas500(self, monedas500):
        self.monedas500 = monedas500
    def getMonedas500(self):
        return self.monedas500

    # monedas de 100 colones
    def setMonedas100(self, monedas100):
        self.monedas100 = monedas100
    def getMonedas100(self):
        return self.monedas100

    # monedas de 50
    def setMonedas50(self, monedas50):
        self.monedas50 = monedas50
    def getMonedas50(self):
        return self.monedas50

    # monedas de 25
    def setMonedas25(self, monedas25):
        self.monedas25 = monedas25
    def getMoneda25(self):
        return self.monedas25

    # Metodo de calculo
    def calcular_Vuelto(self, pArticulo, pEfectivo): 
        vuelto = pEfectivo - pArticulo
        if (vuelto >= 500):
            self.setMonedas500(vuelto // 500)
            vuelto = vuelto - (self.monedas500 * 500)
        if (vuelto >= 100):
            self.setMonedas100(vuelto//100)
            vuelto = vuelto - (self.monedas100 * 100)
        if(vuelto >= 50):
            self.setMonedas50(vuelto//50)
            vuelto = vuelto - (self.monedas50 * 50)
        if (vuelto >= 25):
            self.setMonedas25(vuelto//25)
            vuelto = vuelto - (self.monedas25 * 50)

    # Imprimir vuelto
    def Imprimir_Vuelto(self):
        print(f"Monedas de 500: {self.monedas500}\nMonedas de 100: {self.monedas100}\nMonedas de 50: {self.monedas50}\nMonedas de 25: {self.monedas25}")

# =================== FIN DE LA CLASE MAQUINA ===================

maquina = Maquina()

precio_articulo = float(input("Ingrese el valor del producto en colones: "))
pago_en_efectivo = float(input("Ingrese el valor del efectivo para la compra en colones: "))

maquina.calcular_Vuelto(precio_articulo, pago_en_efectivo)
maquina.Imprimir_Vuelto()