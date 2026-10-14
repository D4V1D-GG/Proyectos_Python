class animal:
    def __init__(self, nombre, peso):
        self.nombre = nombre
        self.peso = peso

class vaca(animal):
    def __init__(self, nombre, peso, tipo):
        self.tipo = tipo
        super().__init__(nombre, peso)

    def saludoV(self):
        print(f"Muu, muu, soy la vaca", self.nombre)

class cerdo(animal):
    def __init__(self, nombre, peso, den_origen):
        self.den_origen = den_origen
        super().__init__(nombre, peso)

    def saludoC(self):
        print(f"Oink, Oink, soy el cerdo", self.nombre)

class pollo(animal):
    def __init__(self, nombre, peso):
        super().__init__(nombre, peso)

    def saludoP(self):
        print(f"Pio, Pio, soy el pollo", self.nombre)

vaca = vaca("Lola", "100 kg", "Lechera")
vaca.saludoV()

cerdo = cerdo("Porky", "50 kg", "Iberico")
cerdo.saludoC()

pollo = pollo("Chiqui", "20 kg")
pollo.saludoP()