from database.db import get_connection
from .entities.Paciente import Paciente


class PacienteModel:

    @classmethod
    def get_pacientes(self):
        try:
            connection = get_connection()
            pacientes = []
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id, id_terapeuta, nui, nombre, apellido, edad, direccion, estado FROM paciente ORDER BY apellido ASC")
                resultset = cursor.fetchall()

                for row in resultset:
                    paciente = Paciente(
                        row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
                    pacientes.append(paciente.to_JSON())
            connection.close()
            return pacientes
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_paciente(self, id):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id, id_terapeuta, nui, nombre, apellido, edad, direccion, estado FROM paciente WHERE id = %s", (id,))
                row = cursor.fetchone()
                paciente = None
                if row != None:
                    paciente = Paciente(
                        row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
                    paciente = paciente.to_JSON()
            connection.close()
            return paciente
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def add_paciente(self, paciente):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO paciente (id_terapeuta, nui, nombre, apellido, edad, direccion, estado) VALUES (%s,%s, %s, %s, %s, %s, %s)", (
                    paciente.id_terapeuta, paciente.nui, paciente.nombre, paciente.apellido, paciente.edad, paciente.direccion, paciente.estado))
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def update_paciente(self, paciente):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("UPDATE paciente SET id_terapeuta = %s, nui = %s, nombre = %s, apellido = %s, edad = %s, direccion = %s, estado = %s WHERE id = %s", (
                    paciente.id_terapeuta,paciente.nui, paciente.nombre, paciente.apellido, paciente.edad, paciente.direccion, paciente.estado, paciente.id))
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def delete_paciente(self, paciente):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM paciente WHERE id = %s", (paciente.id,))
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_state_paciente(self, paciente):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("UPDATE paciente SET estado = %s WHERE id = %s", (
                    paciente.estado, paciente.id))
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)