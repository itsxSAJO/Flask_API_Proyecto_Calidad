from flask import Blueprint, jsonify, request

# Entities
from models.entities.Sesion import Sesion

# Models
from models.SesionModel import SesionModel

main = Blueprint('sesion_blueprint', __name__)

@main.route('/pacientes/<id_paciente>', methods=['GET'])
def get_sesiones_by_paciente(id_paciente):
    try:
        sesiones = SesionModel.get_sesiones_by_paciente(id_paciente)
        if sesiones:
            return jsonify(sesiones), 200
        else:
            return jsonify({'message': 'No sessions found for the given patient ID'}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/')
def get_sesiones():
    try:
        sesiones = SesionModel.get_sesiones()
        return jsonify(sesiones)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/<id_intento>')
def get_sesion(id_intento):
    try:
        sesion = SesionModel.get_sesion(id_intento)
        if sesion != None:
            return jsonify(sesion)
        else:
            return jsonify({'message': 'Sesion not found'}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/add', methods=['POST'])
def add_sesion():
    try:
        id_paciente = request.json.get('id_paciente')
        fecha = request.json.get('fecha')
        duracion = request.json.get('duracion')
        puntaje = request.json.get('puntaje')
        aciertos = request.json.get('aciertos')
        errores = request.json.get('errores')

        # Validar que los campos no sean nulos
        if id_paciente is None or fecha is None or duracion is None or puntaje is None or aciertos is None or errores is None:
            return jsonify({'message': 'Todos los campos son obligatorios'}), 400

        # Validar tipo de dato y longitud
        if not isinstance(fecha, str) or len(fecha) > 10:
            return jsonify({'message': 'La fecha debe ser una cadena de texto de máximo 10 caracteres'}), 400
        if not isinstance(duracion, str) or len(duracion) > 10:
            return jsonify({'message': 'La duración debe ser una cadena de texto de máximo 10 caracteres'}), 400
        if not isinstance(puntaje, int):
            return jsonify({'message': 'El puntaje debe ser un valor entero'}), 400
        if not isinstance(aciertos, int):
            return jsonify({'message': 'El aciertos debe ser un valor entero'}), 400
        if not isinstance(errores, int):
            return jsonify({'message': 'El errores debe ser un valor entero'}),

        sesion = Sesion(None, id_paciente, fecha, duracion, puntaje, aciertos, errores)
        affected_rows = SesionModel.add_sesion(sesion)
        return jsonify({'affected_rows': affected_rows})
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/update/<id_intento>', methods=['PUT'])
def update_sesion(id_intento):
    try:
        id_paciente = request.json.get('id_paciente')
        fecha = request.json.get('fecha')
        duracion = request.json.get('duracion')
        puntaje = request.json.get('puntaje')
        aciertos = request.json.get('aciertos')
        errores = request.json.get('errores')

        # Validar que los campos no sean nulos
        if id_paciente is None or fecha is None or duracion is None or puntaje is None:
            return jsonify({'message': 'Todos los campos son obligatorios'}), 400

        # Validar tipo de dato y longitud
        if not isinstance(fecha, str) or len(fecha) > 10:
            return jsonify({'message': 'La fecha debe ser una cadena de texto de máximo 10 caracteres'}), 400
        if not isinstance(duracion, str) or len(duracion) > 10:
            return jsonify({'message': 'La duración debe ser una cadena de texto de máximo 10 caracteres'}), 400
        if not isinstance(puntaje, int):
            return jsonify({'message': 'El puntaje debe ser un valor entero'}), 400
        if not isinstance(aciertos, int):
            return jsonify({'message': 'El aciertos debe ser un valor entero'}), 400
        if not isinstance(errores, int):
            return jsonify({'message': 'El errores debe ser un valor entero'}), 400

        sesion = Sesion(id_intento, id_paciente, fecha, duracion, puntaje, aciertos, errores)
        affected_rows = SesionModel.update_sesion(sesion)
        if affected_rows == 1:
            return jsonify({'nui_paciente': sesion.id_intento, 'message': 'Sesion updated successfully'}), 200
        else:
            return jsonify({'message': "Error on update"}), 500
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    
@main.route('/delete/<id_intento>', methods=['DELETE'])
def delete_sesion(id_intento):
    try:
        sesion = Sesion(id_intento)
        affected_rows = SesionModel.delete_sesion(sesion)
        if affected_rows == 1:
            return jsonify({'id_intento': sesion.id_intento, 'message': 'Sesion deleted successfully'}), 200
        else:
            return jsonify({'message': "No sesion deleted"}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
