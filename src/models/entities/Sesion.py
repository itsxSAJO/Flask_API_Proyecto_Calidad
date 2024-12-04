from utils.DateFormat import DateFormat

class Sesion():
    
    def __init__(self, id_intento, nui_paciente=None, fecha=None, duracion=None, puntaje=None):
        self.id_intento = id_intento
        self.nui_paciente = nui_paciente
        self.fecha = fecha
        self.duracion = duracion
        self.puntaje = puntaje

    def to_JSON(self):
        return {
            'id_intento': self.id_intento,
            'nui_paciente': self.nui_paciente,
            'fecha': DateFormat.convert_date(self.fecha),
            'duracion': self.duracion,
            'puntaje': self.puntaje
        }