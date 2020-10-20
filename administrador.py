from particula import Particula

class Administrador:
    def __init__(self):
        self.__particulas = []

    def agregar_final(self, particula:Particula):
        self.__particulas.append(particula)

    def agregar_inicio(self, particula:Particula):
        self.__particulas.insert(0, particula)

    def mostar(self):
        for particula in self.__particulas:
            print(particula)


n01 = Particula(id="0520", origen_x="16", origen_y="73", destino_x="115", destino_y="100", velocidad="90", red="150",  green="34", blue="86", distancia="")
n02 = Particula(id="1331", origen_x="5", origen_y="7", destino_x="415", destino_y="340", velocidad="150", red="29",  green="94", blue="25", distancia="")
Administrador = Administrador()
Administrador.agregar_final(n01)
Administrador.agregar_inicio(n02)
Administrador.agregar_inicio(n01)
Administrador.mostar()