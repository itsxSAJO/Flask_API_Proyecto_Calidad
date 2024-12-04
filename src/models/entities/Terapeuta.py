class Terapeuta():
    
    def __init__(self, nui=None, nombre=None, apellido=None, especialidad=None, estado=True) -> None:
        self.nui = nui
        self.nombre = nombre
        self.apellido = apellido
        self.especialidad = especialidad
        self.estado = estado
    
    def to_JSON(self):
        return {    
            'nui': self.nui,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'especialidad': self.especialidad,
            'estado': self.estado
        }