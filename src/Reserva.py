class Reserva:
    """Una reserva contiene una habitación y un cliente."""

    def __init__(self, habitacion, cliente, noches):
        self.habitacion = habitacion
        self.cliente = cliente
        self.noches = noches
        self.habitacion.ocupar()

    def get_costo_total(self):
        return self.habitacion.calcular_costo(self.noches)

    def cancelar(self):
        self.habitacion.liberar()

    def __str__(self):
        return (f"Reserva de {self.cliente} en {self.habitacion} "
                f"por {self.noches} noches. "
                f"Costo total: ${self.get_costo_total()}")
