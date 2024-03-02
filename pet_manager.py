from datetime import datetime
import re
import graphviz

class PetManager:
    def __init__(self):
        self.mascotas = {}

    def ejecutar_comando(self, comando):
        instruccion = comando[0]
        if instruccion == "Crear_Gato":
            self.crear_gato(comando[1])
        elif instruccion == "Dar_de_Comer":
            if len(comando) >= 3:  # Verificar que hay suficientes elementos en el comando
                self.dar_de_comer(comando[1], int(comando[2]))
            else:
                print("El comando Dar_de_Comer no tiene suficientes parámetros.")
        elif instruccion == "Jugar":
            if len(comando) >= 3:  # Verificar que hay suficientes elementos en el comando
                self.jugar_con_mascota(comando[1], int(comando[2]))
            else:
                print("El comando Jugar no tiene suficientes parámetros.")
        elif instruccion == "Resumen_Mascota":
            self.resumen_mascota(comando[1])
        elif instruccion == "Resumen_Global":
            self.resumen_global()
            
    def crear_gato(self, nombre):
        self.mascotas[nombre] = {"energia": 1, "vivo": True}
        self._escribir_en_archivo("petmanager_result", f"Se creo el gato {nombre}")

    def dar_de_comer(self, nombre, peso):
        if nombre in self.mascotas:
            self.mascotas[nombre]["energia"] += peso // 10
            if self.mascotas[nombre]["energia"] <= 0:
                self.mascotas[nombre]["vivo"] = False
                self._escribir_en_archivo("petmanager_result", f"Muy tarde. Ya me mori despues de comer.")
            else:
                self._escribir_en_archivo("petmanager_result", f"{nombre}, gracias ahora mi energia es {self.mascotas[nombre]['energia']}")
        else:
            print(f"[{datetime.now()}] No se encontró la mascota con nombre {nombre}")

    def jugar_con_mascota(self, nombre, tiempo):
        if nombre in self.mascotas:
            self.mascotas[nombre]["energia"] -= tiempo // 10
            if self.mascotas[nombre]["energia"] <= 0:
                self.mascotas[nombre]["energia"] = 0
                self.mascotas[nombre]["vivo"] = False
                self._escribir_en_archivo("petmanager_result", f"Muy tarde. Ya me mori despues de jugar.")
            else:
                self._escribir_en_archivo("petmanager_result", f"{nombre}, gracias por jugar conmigo ahora mi energia es {self.mascotas[nombre]['energia']}")
        else:
            print(f"[{datetime.now()}] No se encontró la mascota con nombre {nombre}")

    def resumen_mascota(self, nombre):
        if nombre in self.mascotas:
            estado = "Vivo" if self.mascotas[nombre]["vivo"] else "Muerto"
            self._escribir_en_archivo("petmanager_result", f"{nombre}, Energia: {self.mascotas[nombre]['energia']}, Gato, {estado}")
        else:
            print(f" No se encontró la mascota con nombre {nombre}")

    def resumen_global(self):
        resumen = "------------------Resumen Global------------------\n"
        fecha_actual = datetime.now().strftime("%d/%m/%Y %H:%M")
        for nombre, gato in self.mascotas.items():
            estado = "Vivo" if gato["vivo"] else "Muerto"
            resumen += f"[{fecha_actual}] {nombre}, Energia: {gato['energia']}, Gato, {estado}\n"
        self._escribir_en_archivo("petmanager_result", resumen)
        self.generar_grafico()
        resumen = "--------------------------------------------------\n"


    def generar_grafico(self):
        dot = graphviz.Digraph(comment='Mascotas')
        for nombre, gato in self.mascotas.items():
            estado = "Vivo" if gato["vivo"] else "Muerto"
            dot.node(nombre, f"{nombre}, Energia: {gato['energia']}, Gato, {estado}")
        dot.render('mascotas', format='png', cleanup=True)

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
                comando = re.split(r':|,', linea.strip())
                pet_manager.ejecutar_comando(comando)
    except FileNotFoundError:
        print("El archivo especificado no existe.")
