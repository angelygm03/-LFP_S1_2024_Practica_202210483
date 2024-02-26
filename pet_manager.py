from gato import Gato
from datetime import datetime

class PetManager:
    def __init__(self):
        self.mascotas = {}

    def crear_gato(self, nombre):
        self.mascotas[nombre] = Gato(nombre)
        self._escribir_en_archivo("petmanager_result", f"Se creo el gato {nombre}")

    def dar_de_comer(self, nombre, peso):
        if nombre in self.mascotas:
            self.mascotas[nombre].comer(peso)
            self._escribir_en_archivo("petmanager_result", f"{nombre}, gracias ahora mi energia es {self.mascotas[nombre].energia}")
        else:
            print(f"[{datetime.now()}] No se encontró la mascota con nombre {nombre}")

    def jugar_con_mascota(self, nombre, tiempo):
        if nombre in self.mascotas:
            self.mascotas[nombre].jugar(tiempo)
            estado = "Vivo" if self.mascotas[nombre].vivo else "Muerto"
            self._escribir_en_archivo("petmanager_result", f"{nombre}, gracias por jugar conmigo ahora mi energia es {self.mascotas[nombre].energia}, {estado}")
        else:
            print(f"[{datetime.now()}] No se encontró la mascota con nombre {nombre}")

    def resumen_global(self):
        resumen = []
        for nombre, gato in self.mascotas.items():
            estado = "Vivo" if gato.vivo else "Muerto"
            resumen.append(f"[{datetime.now()}] {nombre}, Energia: {gato.energia}, Gato, {estado}")

        with open("petmanager_result.petmanager_result", 'a') as archivo:
            archivo.write("[{}] -------------------------- Resumen Global --------------------------\n".format(datetime.now()))
            archivo.write('\n'.join(resumen) + '\n')

    def _escribir_en_archivo(self, prueba, contenido):
        fecha_actual = datetime.now().strftime("%d/%m/%Y %H:%M")
        with open(f"{prueba}.petmanager_result", 'a') as archivo:
            archivo.write(f"[{fecha_actual}] {contenido}\n")
            
def leer_archivo(pet_manager):
    prueba = input("Ingresa el nombre del archivo .petmanager: ")
    try:
        with open(prueba, 'r') as archivo:
            lineas = archivo.readlines()
            for linea in lineas:
                if ':' in linea:
                    instruccion, parametros = linea.strip().split(':', 1)
                    parametros = parametros.split(',')
                    if instruccion == "Crear_Gato":
                        pet_manager.crear_gato(parametros[0])
                    elif instruccion == "Dar_de_Comer":
                        pet_manager.dar_de_comer(parametros[0], int(parametros[1]))
                    elif instruccion == "Jugar":
                        pet_manager.jugar_con_mascota(parametros[0], int(parametros[1]))
                    else:
                        print(f"Instrucción no reconocida: {instruccion}")
                else:
                    print("Formato incorrecto en la línea:", linea)
    except FileNotFoundError:
        print("El archivo especificado no existe.")

