# Objetivo: crear un centro de control de vuelos, debe reconocer la 
# cantidad de vuelos que tienen lugar en todo momento, aparte del primer
# vuelo en llegar, y los vuelos por aeropuerto que todavia faltan por llegar
# Se necesita:
# A .Vuelo en el aire: ID de vuelo, tiempo de salida, tiempo de llegada, aeropuerto de salida
# , aeropuerto de llegada, ademas del avion que esta en vuelo
# B. Aeropuertos: nombre del aeropuerto y nombre del pais en que se encuentra
# C. Avion: capacidad y tipo de avion
# Funciones: Crear un objeto de vuelo con toda la informacion. Debe eliminar un vuelo determinado de acuerdo con su
# identificador, debe obteenr la cantidad de vuelos que se encuentran en el aire en ese momento, obtiene el vuelo que va a
# llegar primero y ademas muestra el aeropuerto al que se dirige y toda la informacion que se tenga sobre ese vuelo,
# devuelve por cada aeropuerto los vuelos que se dirigen a el, asi como los tiempos que deben aterrizar.


class Avion: 
    # tipo de avion -> carga, transporte, militar
    def __init__(self, identificador, capacidad, tipo):
        self.identificador = identificador
        self.capacidad = capacidad
        self.tipo = tipo

        
    # Identificador
    def setIdentificador(self, valor):
        self.identificador = valor
    def getIdentificador(self):
        return self.identificador

    # Capacidad
    def setCapacidad(self, valor):
        self.capacidad = int(valor)
    def getCapacidad(self):
        return self.capacidad

    # Tipo
    def setTipo(self, valor):
        self.tipo = valor
    def getTipo(self):
        return self.tipo

# ================== FIN CLASE AVION =================

class Aeropuerto:
    def __init__(self, nombreAeropuerto, nombrePais):
        self.nombreAeropuerto = nombreAeropuerto
        self.nombrePais = nombrePais

    # Nombre del aeropuerto
    def setNombreAeropuerto(self, valor):
        self.nombreAeropuerto = valor
    def getNombreAeropuerto(self, valor):
        return self.nombreAeropuerto

    # Nombre del país
    def setNombrePais(self, valor):
        self.nombrePais = valor
    def getNombrePais(self):
        return self.nombrePais
    
# ================= FIN CLASE AEROPUERTO ===============

class VueloActivo:
    def __init__(self, idVuelo, tiempoSalida, tiempoLlegada, origen, destino, avion):
        self.idVuelo = idVuelo
        self.tiempoSalida = tiempoSalida
        self.tiempoLlegada = tiempoLlegada
        self.origen = origen
        self.destino = destino
        self.avion = avion

    # identificador del vuelo
    def setIdVuelo(self, valor):
        self.idVuelo = valor
    def getIdVuelo(self):
        return self.idVuelo

    # tiempoSalida
    def setTiempoSalida(self, valor):
        self.tiempoSalida = valor
    def getTiempoSalida(self):
        return self.tiempoSalida
    
    # tiempo Llegada
    def setTiempoLlegada(self, valor):
        self.tiempoLlegada = valor
    def getTiempoLlegada(self):
        return self.tiempoLlegada

    # Origen
    def setOrigen(self, valor):
        self.origen = valor
    def getOrigen(self):
        return self.origen

    # Destino
    def setDestino(self, valor):
        self.destino = valor
    def getDestion(self):
        return self.destino

    def setAvion(self, valor):
        self.avion = valor
    def getAvion(self):
        return self.avion

# =================== FIN DE LA CLASE VUELO ACTVIO ==================

class ControladorVuelos:
    def __init__(self):
        # Contenedor de Vuelos
        self.vuelosActivos = []


    # Metodos Operativos
    def CrearVuelo(self, idVuelo, salida, llegada, nAeropuertoOrigen, nPaisOrigen, nAueropuertoDestino, nPaisDestino, idAvion, capacidadAvion, tipoAvion):
        vueloNuevo = VueloActivo(idVuelo, 
                                 salida,
                                 llegada, 
                                 Aeropuerto(nAeropuertoOrigen, nPaisOrigen),
                                 Aeropuerto(nAueropuertoDestino, nPaisDestino),
                                 Avion(idAvion, capacidadAvion, tipoAvion))
        self.vuelosActivos.insert(vueloNuevo)

    def buscarVuelo(self, idVuelo):
        return next((vuelo for vuelo in self.vuelosActivos if vuelo.getIdVuelo() == idVuelo), None)

    def eliminarVuelo(self, idVuelo):
        vuelo = self.buscarVuelo(idVuelo)
        if vuelo is not None:
            self.vuelosActivos.remove(vuelo)
            return True
        else:
            return False
        



