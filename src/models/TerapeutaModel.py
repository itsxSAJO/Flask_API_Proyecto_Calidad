from database.db import get_connection
from .entities.Terapeuta import Terapeuta
from .entities.Paciente import Paciente

class TerapeutaModel:
    
    @classmethod
    def get_terapeutas(self):
        try:
            connection = get_connection()
            terapeutas = []
            with connection.cursor() as cursor:
                cursor.execute("SELECT id, nui, nombre, apellido, especialidad, estado FROM terapeuta ORDER BY apellido ASC")  
                resultset = cursor.fetchall()
                
                for row in resultset:
                    terapeuta = Terapeuta(row[0], row[1], row[2], row[3], row[4], row[5])
                    terapeutas.append(terapeuta.to_JSON())  
            connection.close()
            return terapeutas
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_terapeuta(self, id):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("SELECT id, nui, nombre, apellido, especialidad, estado FROM terapeuta WHERE id = %s", (id,))  
                row = cursor.fetchone()
                terapeuta=None
                if row != None:
                    terapeuta = Terapeuta(row[0], row[1], row[2], row[3], row[4], row[5]) 
                    terapeuta = terapeuta.to_JSON()
            connection.close()
            return terapeuta
        except Exception as ex:
            raise Exception(ex)
        

    @classmethod
    def add_terapeuta(self, terapeuta):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO terapeuta (nui, nombre, apellido, especialidad, estado) VALUES (%s,%s, %s, %s, %s)", (terapeuta.nui, terapeuta.nombre, terapeuta.apellido, terapeuta.especialidad, terapeuta.estado))  
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
        
    
    @classmethod
    def update_terapeuta(self, terapeuta):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("UPDATE terapeuta SET nui = %s, nombre = %s, apellido = %s, especialidad = %s, estado = %s WHERE id = %s", (terapeuta.nui, terapeuta.nombre, terapeuta.apellido, terapeuta.especialidad, terapeuta.estado, terapeuta.id)) 
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def delete_terapeuta(self, terapeuta):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM terapeuta WHERE id = %s", (terapeuta.id,))  
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def update_state_terapeuta(self, terapeuta):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("UPDATE terapeuta SET estado = %s WHERE id = %s", (terapeuta.estado, terapeuta.id)) 
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise RuntimeError("Error updating state of terapeuta") from ex
        
    @classmethod
    def get_pacientes_terapeuta(self, terapeuta):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("SELECT id, nui, nombre, apellido, edad, direccion, estado FROM paciente WHERE id_terapeuta = %s", (terapeuta,))  
                pacientes = []
                resultset = cursor.fetchall()
                for row in resultset:
                    paciente = {
                        'id': row[0],
                        'nui': row[1],
                        'nombre': row[2],
                        'apellido': row[3],
                        'edad': row[4],
                        'direccion': row[5],
                        'estado': row[6]
                    }
                    pacientes.append(paciente)
            connection.close()
            return pacientes
        except Exception as ex:
            raise Exception(ex)
