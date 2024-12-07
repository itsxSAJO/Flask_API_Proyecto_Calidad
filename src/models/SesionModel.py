from database.db import get_connection
from .entities.Sesion import Sesion

class SesionModel:
    
    @classmethod
    def get_sesiones(self):
        try:
            connection = get_connection()
            sesiones = []
            with connection.cursor() as cursor:
                cursor.execute("SELECT id_intento, id_paciente, fecha, duracion, puntaje, aciertos, errores FROM sesion ORDER BY id_intento ASC")  
                resultset = cursor.fetchall()
                
                for row in resultset:
                    sesion = Sesion(row[0], row[1], row[2], str(row[3]), row[4], row[5], row[6])
                    sesiones.append(sesion.to_JSON())  
            connection.close()
            return sesiones
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_sesion(self, id_intento):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("SELECT id_intento, id_paciente, fecha, duracion, puntaje, aciertos, errores FROM sesion WHERE id_intento = %s", (id_intento,))  
                row = cursor.fetchone()
                sesion=None
                if row != None:
                    sesion = Sesion(row[0], row[1], row[2], str(row[3]), row[4], row[5], row[6]) 
                    sesion = sesion.to_JSON()
            connection.close()
            return sesion
        except Exception as ex: 
            raise Exception(ex)
    
    @classmethod
    def add_sesion(self, sesion):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO sesion (id_paciente, fecha, duracion, puntaje, aciertos, errores) VALUES (%s, %s, %s, %s,%s, %s)", (sesion.id_paciente, sesion.fecha, sesion.duracion, sesion.puntaje, sesion.aciertos, sesion.errores))  
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def update_sesion(self, sesion):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("UPDATE sesion SET id_paciente = %s, fecha = %s, duracion = %s, puntaje = %s, aciertos = %s, errores = %s WHERE id_intento = %s", (sesion.id_paciente, sesion.fecha, sesion.duracion, sesion.puntaje, sesion.aciertos, sesion.errores, sesion.id_intento)) 
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def delete_sesion(cls, sesion):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM sesion WHERE id_intento = %s", (sesion.id_intento,))  
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise ValueError("Error deleting session") from ex