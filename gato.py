from datetime import datetime

class Gato:
    def __init__(self, nombre):
        self.nombre = nombre
        self.energia = 1
        self.vivo = True

    def correr(self, distancia):
        if self.vivo:
            self.energia -= distancia / 2
            if self.energia <= 0:
                self.energia = 0
                self.vivo = False
                print(f"[{datetime.now()}] {self.nombre}, Muy tarde. Ya me morí.")
            else:
                print(f"[{datetime.now()}] {self.nombre}, Corrí {distancia} metros.")

    def comer(self, peso):
        self.energia += peso / 10
        print(f"[{datetime.now()}] {self.nombre}, Comí {peso} gramos.")

    def jugar(self, tiempo):
        if self.vivo:
            self.energia -= tiempo * 0.1
            if self.energia <= 0:
                self.energia = 0
                self.vivo = False
                print(f"[{datetime.now()}] {self.nombre}, Muy tarde. Ya me morí después de jugar.")
            else:
                print(f"[{datetime.now()}] {self.nombre}, Jugamos durante {tiempo} minutos.")
        else:
            print(f"[{datetime.now()}] {self.nombre}, Ya me morí.")
            