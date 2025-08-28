from Habitacion import Habitacion
class HabitacionSuite(Habitacion):
    def __init__(self, numero):
        super().__init__(numero, "Suite", 500000)