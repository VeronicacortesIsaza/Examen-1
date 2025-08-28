from src.Hotel import Hotel 
from src.HabitacionEstandar import HabitacionEstandar
from src.HabitacionSuite import HabitacionSuite
from src.HabitacionPremium import HabitacionPremium

def menu():
    hotel = Hotel()
    while True:
        print("\n===== SISTEMA DE RESERVAS DE HOTEL =====")
        print("1. Reservar habitación")
        print("2. Cancelar reserva")
        print("3. Mostrar reservas")
        print("4. Salir")

        opcion = input("Elige una opción (1-4): ")

        if opcion == "1":
            cliente = input("Nombre del cliente: ")
            noches = int(input("Número de noches: "))
            print("Tipos de habitación:")
            print("1. Estándar ($200000/noche)")
            print("2. Suite ($30000/noche)")
            print("3. Premium ($450000/noche)")
            tipo = input("Seleccione tipo: ")

            if tipo == "1":
                hotel.reservar(cliente, noches, HabitacionEstandar)
            elif tipo == "2":
                hotel.reservar(cliente, noches, HabitacionSuite)
            elif tipo == "3":
                hotel.reservar(cliente, noches, HabitacionPremium)
            else:
                print("Tipo inválido.")

        elif opcion == "2":
            cliente = input("Ingrese el nombre del cliente para cancelar la reserva: ")
            hotel.cancelar_reserva(cliente)

        elif opcion == "3":
            hotel.mostrar_reservas()

        elif opcion == "4":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
