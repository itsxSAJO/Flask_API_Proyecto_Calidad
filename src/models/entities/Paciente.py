class Paciente():
    
    def __init__(self, id, id_terapeuta=None, nui=None, nombre=None, apellido=None, edad=None, direccion=None, estado=True) -> None:
        self.id = id
        self.id_terapeuta = id_terapeuta
        self.nui = nui
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.direccion = direccion
        self.estado = estado
        
    def to_JSON(self):  
        return {
            'id': self.id,
            'id_terapeuta': self.id_terapeuta,
            'nui': self.nui,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'edad': self.edad,
            'direccion': self.direccion,
            'estado': self.estado
        }