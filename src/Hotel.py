from HabitacionEstandar import HabitacionEstandar
from HabitacionSuite import HabitacionSuite
from HabitacionPremium import HabitacionPremium
from Reserva import Reserva

class Hotel:
    """Clase que administra habitaciones y reservas."""

    def __init__(self):
        self.habitaciones = [
            HabitacionEstandar(101),
            HabitacionEstandar(102),
            HabitacionSuite(201),
            HabitacionPremium(301)
        ]
        self.reservas = []

    def reservar(self, cliente, noches, tipo_habitacion):
        for habitacion in self.habitaciones:
            if isinstance(habitacion, tipo_habitacion) and habitacion.disponible:
                reserva = Reserva(habitacion, cliente, noches)
                self.reservas.append(reserva)
                print("Reserva realizada con éxito.")
                return reserva
        print("No hay habitaciones disponibles de ese tipo.")
        return None

    def cancelar_reserva(self, cliente):
        for reserva in self.reservas:
            if reserva.cliente.lower() == cliente.lower():
                reserva.cancelar()
                self.reservas.remove(reserva)
                print("Reserva cancelada correctamente.")
                return
        print("No se encontró una reserva a nombre de ese cliente.")

    def mostrar_reservas(self):
        if not self.reservas:
            print("No hay reservas activas.")
        else:
            for r in self.reservas:
                print(r)
