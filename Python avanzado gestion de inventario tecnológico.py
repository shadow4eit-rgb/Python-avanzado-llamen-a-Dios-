class Dispositivo:
    cantidad_total_registrada = 0

    def _init_(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.encendido = False
        Dispositivo.cantidad_total_registrada += 1

    def cambiar_estado(self):
        self.encendido = not self.encendido

class Telefono(Dispositivo):
    def _init_(self, marca, modelo):
        super()._init_(marca, modelo)
        self.aplicaciones = []

    def instalar_app(self, nombre_app):
        self.aplicaciones.append(nombre_app)

def mostrar_telefonos_encendidos(lista_telefonos):
    print("--- Teléfonos Encendidos ---")
    for t in lista_telefonos:
        if t.encendido:
            print(f"{t.marca} {t.modelo}")
