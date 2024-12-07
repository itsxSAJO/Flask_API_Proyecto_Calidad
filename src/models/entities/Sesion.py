from utils.DateFormat import DateFormat

class Sesion():
    
    def __init__(self, id_intento, id_paciente=None, fecha=None, duracion=None, puntaje=None, aciertos=None, errores=None):
        self.id_intento = id_intento
        self.id_paciente = id_paciente
        self.fecha = fecha
        self.duracion = duracion
        self.puntaje = puntaje
        self.aciertos = aciertos
        self.errores = errores

    def to_JSON(self):
        return {
            'id_intento': self.id_intento,
            'id_paciente': self.id_paciente,
            'fecha': DateFormat.convert_date(self.fecha),
            'duracion': self.duracion,
            'puntaje': self.puntaje,
            'aciertos': self.aciertos,
            'errores': self.errores
        }