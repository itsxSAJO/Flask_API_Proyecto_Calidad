from database.db import get_connection
from .entities.Terapeuta import Terapeuta

class TerapeutaModel:
    
    @classmethod
    def get_terapeutas(self):
        try:
            connection = get_connection()
            terapeutas = []
            with connection.cursor() as cursor:
                cursor.execute("SELECT nui, nombre, apellido, especialidad, estado FROM terapeuta ORDER BY apellido ASC")  
                resultset = cursor.fetchall()
                
                for row in resultset:
                    terapeuta = Terapeuta(row[0], row[1], row[2], row[3], row[4])
                    terapeutas.append(terapeuta.to_JSON())  
            connection.close()
            return terapeutas
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_terapeuta(self, nui):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("SELECT nui, nombre, apellido, especialidad, estado FROM terapeuta WHERE nui = %s", (nui,))  
                row = cursor.fetchone()
                terapeuta=None
                if row != None:
                    terapeuta = Terapeuta(row[0], row[1], row[2], row[3], row[4]) 
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
                cursor.execute("UPDATE terapeuta SET nombre = %s, apellido = %s, especialidad = %s, estado = %s WHERE nui = %s", ( terapeuta.nombre, terapeuta.apellido, terapeuta.especialidad, terapeuta.estado, terapeuta.nui)) 
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
                cursor.execute("DELETE FROM terapeuta WHERE nui = %s", (terapeuta.nui,))  
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
