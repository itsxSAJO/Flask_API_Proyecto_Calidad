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


@main.route('/<id>')
def get_terapeuta(id):
    try:
        terapeuta = TerapeutaModel.get_terapeuta(id)
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
        
        
        terapeuta = Terapeuta(None, nui, nombre, apellido, especialidad, estado)
        
        affected_rows = TerapeutaModel.add_terapeuta(terapeuta)
        if affected_rows == 1:
            return jsonify({'id_terapeuta': terapeuta.id, 'message': 'Terapeuta agregado exitosamente'}), 200
        else:
            return jsonify({'message': "Error on insert"}), 500
    
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    

@main.route('/update/<id>', methods=['PUT'])
def update_terapeuta(id):
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
        
        terapeuta = Terapeuta(id, nui, nombre, apellido, especialidad, estado)
        
        affected_rows = TerapeutaModel.update_terapeuta(terapeuta)
        if affected_rows == 1:
            return jsonify({'id_terapeuta': terapeuta.id, 'message': 'Terapeuta actualizado exitosamente'}), 200
        else:
            return jsonify({'message': "No terapist updated"}), 404
    
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/delete/<id>', methods=['DELETE'])
def delete_terapeuta(id):
    try:
        terapeuta = Terapeuta(id)
        affected_rows = TerapeutaModel.delete_terapeuta(terapeuta)
        if affected_rows == 1:
            return jsonify({'id': terapeuta.id, 'message': 'Terapeuta eliminado exitosamente'}), 200
        else:
            return jsonify({'message': "No terapist deleted"}), 404
    
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    
@main.route('/updateState/<id>', methods=['PUT'])
def update_state_terapeuta(id):
    try:
        estado = request.json.get('estado')
        
        # Validar que los campos no sean nulos
        if estado is None:
            return jsonify({'message': 'El estado es obligatorio'}), 400
        
        # Validar tipo de dato
        if not isinstance(estado, bool):
            return jsonify({'message': 'El estado debe ser un valor booleano (true o false)'}), 400
        
        terapeuta = Terapeuta(id, None, None, None, None, estado)
        
        affected_rows = TerapeutaModel.update_state_terapeuta(terapeuta, estado)
        if affected_rows == 1:
            return jsonify({'id_terapeuta': terapeuta.id, 'message': 'Estado del terapeuta actualizado exitosamente'}), 200
        else:
            return jsonify({'message': "No terapist updated"}), 404
    
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/pacientes/<id>')
def get_pacientes_terapeuta(id):
    try:
        pacientes = TerapeutaModel.get_pacientes_terapeuta(id)
        return jsonify(pacientes)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500