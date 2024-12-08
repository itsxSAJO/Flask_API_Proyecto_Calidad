class Terapeuta():
    
    def __init__(self, id, nui=None, nombre=None, apellido=None, especialidad=None, estado=True, contrasena=None) -> None:
        self.id = id
        self.nui = nui
        self.nombre = nombre
        self.apellido = apellido
        self.especialidad = especialidad
        self.estado = estado
        self.contrasena = contrasena
    
    def to_JSON(self):
        return {  
            'id': self.id,  
            'nui': self.nui,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'especialidad': self.especialidad,
            'estado': self.estado,
            'contrasena': self.contrasena
        }