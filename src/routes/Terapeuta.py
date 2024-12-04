from flask import Blueprint, jsonify, request
import uuid # Para generar el id de terapeuta

# Entities
from models.entities.Terapeuta import Terapeuta

# Models
from models.TerapeutaModel import TerapeutaModel

main = Blueprint('terapeuta_blueprint', __name__)


@main.route('/')
def get_terapeutas():
    try:
        terapeutas = TerapeutaModel.get_terapeutas()
        return jsonify(terapeutas)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/<nui>')
def get_terapeuta(nui):
    try:
        terapeuta = TerapeutaModel.get_terapeuta(nui)
        if terapeuta != None:
            return jsonify(terapeuta)
        else:
            return jsonify({'message': 'Terapeuta not found'}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/add', methods=['POST'])
def add_terapeuta():
    try:
        nui = request.json.get('nui')
        nombre = request.json.get('nombre')
        apellido = request.json.get('apellido')
        especialidad = request.json.get('especialidad')
        estado = request.json.get('estado')

        # Validar que los campos no sean nulos
        if nui is None or nombre is None or apellido is None or especialidad is None or estado is None:
            return jsonify({'message': 'Todos los campos son obligatorios'}), 400
        
        # Validar tipo de dato y longitud
        if not isinstance(nui, str) or len(nui) > 10:
            return jsonify({'message': 'El NUI debe ser una cadena de texto de máximo 10 caracteres'}), 400
        if not isinstance(nombre, str) or len(nombre) > 20:
            return jsonify({'message': 'El nombre debe ser una cadena de texto de máximo 20 caracteres'}), 400
        if not isinstance(apellido, str) or len(apellido) > 20:
            return jsonify({'message': 'El apellido debe ser una cadena de texto de máximo 20 caracteres'}), 400
        if not isinstance(especialidad, str) or len(especialidad) > 100:
            return jsonify({'message': 'La especialidad debe ser una cadena de texto de máximo 100 caracteres'}), 400
        if not isinstance(estado, bool):
            return jsonify({'message': 'El estado debe ser un valor booleano (true o false)'}), 400
        
        
        terapeuta = Terapeuta(nui, nombre, apellido, especialidad, estado)
        
        affected_rows = TerapeutaModel.add_terapeuta(terapeuta)
        if affected_rows == 1:
            return jsonify({'id_terapeuta': terapeuta.nui, 'message': 'Terapeuta agregado exitosamente'}), 200
        else:
            return jsonify({'message': "Error on insert"}), 500
    
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    

@main.route('/update/<nui>', methods=['PUT'])
def update_terapeuta(nui):
    try:
        nombre = request.json.get('nombre')
        apellido = request.json.get('apellido')
        especialidad = request.json.get('especialidad')
        estado = request.json.get('estado')

        # Validar que los campos no sean nulos
        if nombre is None or apellido is None or especialidad is None or estado is None:
            return jsonify({'message': 'Todos los campos son obligatorios'}), 400
        
        # Validar tipo de dato y longitud
        if not isinstance(nombre, str) or len(nombre) > 20:
            return jsonify({'message': 'El nombre debe ser una cadena de texto de máximo 20 caracteres'}), 400
        if not isinstance(apellido, str) or len(apellido) > 20:
            return jsonify({'message': 'El apellido debe ser una cadena de texto de máximo 20 caracteres'}), 400
        if not isinstance(especialidad, str) or len(especialidad) > 100:
            return jsonify({'message': 'La especialidad debe ser una cadena de texto de máximo 100 caracteres'}), 400
        if not isinstance(estado, bool):
            return jsonify({'message': 'El estado debe ser un valor booleano (true o false)'}), 400
        
        terapeuta = Terapeuta(nui, nombre, apellido, especialidad, estado)
        
        affected_rows = TerapeutaModel.update_terapeuta(terapeuta)
        if affected_rows == 1:
            return jsonify({'id_terapeuta': terapeuta.nui, 'message': 'Terapeuta actualizado exitosamente'}), 200
        else:
            return jsonify({'message': "No terapist updated"}), 404
    
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/delete/<nui>', methods=['DELETE'])
def delete_terapeuta(nui):
    try:
        terapeuta = Terapeuta(nui)
        affected_rows = TerapeutaModel.delete_terapeuta(terapeuta)
        if affected_rows == 1:
            return jsonify({'nui': terapeuta.nui, 'message': 'Terapeuta eliminado exitosamente'}), 200
        else:
            return jsonify({'message': "No terapist deleted"}), 404
    
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
