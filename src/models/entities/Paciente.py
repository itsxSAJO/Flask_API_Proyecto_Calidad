class Paciente():
    
    def __init__(self, nui=None, nui_terapeuta=None, nombre=None, apellido=None, edad=None, direccion=None, estado=True) -> None:
        self.nui = nui
        self.nui_terapeuta = nui_terapeuta
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.direccion = direccion
        self.estado = estado
        
    def to_JSON(self):  
        return {
            'nui': self.nui,
            'nui_terapeuta': self.nui_terapeuta,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'edad': self.edad,
            'direccion': self.direccion,
            'estado': self.estado
        }