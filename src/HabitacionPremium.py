from Habitacion import Habitacion
class HabitacionPremium(Habitacion):
    def __init__(self, numero):
        super().__init__(numero, "Premium", 450000)