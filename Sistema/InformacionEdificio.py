import time

class Edificio:

    def __init__(self, pisos, ascensores):
        self.pisos = pisos
        self.ascensores = ascensores


class Piso:
    def __init__(self, numero_piso, ascensor):
        self.numero_piso = numero_piso
        self.boton_arriba = False
        self.boton_abajo = False
        self.ascensor = ascensor

    def ir_piso_arriba(self):
        self.boton_arriba = True
        self.ascensor.abierto = True
        time.sleep(2)
        self.ascensor.abierto = False
        self.boton_arriba = False

    def ir_piso_abajo(self):
        self.boton_abajo = True
        self.ascensor.abierto = True
        time.sleep(3)
        self.ascensor.abierto = False
        self.boton_abajo = False


class Ascensor:
    def __init__(self, botones_de_piso, ascensorA, ascensorB):
        self.botones_de_piso = botones_de_piso
        self.piso = 0
        self.abierto = False
        self.ascensorA = ascensorA
        self.ascensorB = ascensorB

    def ir_al_piso(self, numero_de_piso):
        botones = list(filter(lambda button: button.numero_de_piso == numero_de_piso, self.botones_de_piso))
        if self.ascensorA in botones:
            boton_presionado = self.ascensorA
            print(f'Ir al Piso: {boton_presionado.numero_de_piso}')
        elif self.ascensorB in botones:
            boton_presionado = self.ascensorB
            print(f'Ir al Piso: {boton_presionado.numero_de_piso}')
        print('----------------')


class BotonDePiso:
    def __init__(self, numero_de_piso):
        self.numero_de_piso = numero_de_piso
        self.encendido = False


boton_piso0 = BotonDePiso(0)
boton_piso1 = BotonDePiso(1)
boton_piso2 = BotonDePiso(2)
boton_piso3 = BotonDePiso(3)
boton_piso4 = BotonDePiso(4)
boton_piso5 = BotonDePiso(5)


botones_de_pisos = [boton_piso0, boton_piso1, boton_piso2, boton_piso3, boton_piso4, boton_piso5]
ascensorA = Ascensor(botones_de_pisos)
ascensorB = Ascensor(botones_de_pisos)

piso0 = Piso(0, ascensorA)
piso0 = Piso(0, ascensorB)
piso1 = Piso(1, ascensorA)
piso1 = Piso(1, ascensorB)
piso2 = Piso(2, ascensorA)
piso2 = Piso(2, ascensorB)
piso3 = Piso(3, ascensorA)
piso3 = Piso(3, ascensorB)
piso4 = Piso(4, ascensorA)
piso4 = Piso(4, ascensorB)
piso5 = Piso(5, ascensorA)
piso5 = Piso(5, ascensorB)
pisos = [piso0, piso1, piso2, piso3, piso4, piso5]

edificio_carilo = Edificio(pisos, [ascensorA, ascensorB])


piso0.ir_piso_arriba()
ascensorA.ir_al_piso(3)
piso0.ir_piso_arriba()
ascensorB.ir_al_piso(3)
piso2.ir_piso_abajo()
ascensorA.ir_al_piso(1)
