import os
from pet_manager import PetManager, leer_archivo

def limpiar_pantalla():
    if os.name == 'nt':
        os.system('cls')

def main():
    while True:
        limpiar_pantalla()
        print("     Lenguajes Formales y de Programación")
        print("                 Sección B-")
        print("             Carnet: 202210483")
        print("Menú Principal")
        print("1. Ir al módulo PetManager")
        print("2. Salir")
        respuesta = input("Ingresa la acción que quieras realizar: ").strip().lower()

        if respuesta == "1":
            limpiar_pantalla()
            print("******** Bienvenido a PetWorld Manager ******")
            print("Menú PetManager")
            print("1. Cargar archivo ")
            print("2. Salir")
            respuesta_modulo1 = input("Ingresa la opción a realizar: ").strip().lower()

            if respuesta_modulo1 == "1":
                pet_manager = PetManager()  
                leer_archivo(pet_manager)
            elif respuesta_modulo1 == "2":
                print("¡Hasta luego!")
                break
            else:
                print("Respuesta inválida, intenta nuevamente")
        elif respuesta == "2":
            print("¡Hasta luego!")
            break
        else: 
            print("Respuesta no válida. Intenta nuevamente")

if __name__ == "__main__":
    main()


