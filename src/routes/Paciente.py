from flask import Blueprint, jsonify, request

#Entities
from models.entities.Paciente import Paciente

# Models
from models.PacienteModel import PacienteModel

main = Blueprint('paciente_blueprint', __name__)

@main.route('/')
def get_pacientes():
    try:
        pacientes = PacienteModel.get_pacientes()
        return jsonify(pacientes)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    
@main.route('/<nui>')
def get_paciente(nui):
    try:
        pacientes = PacienteModel.get_paciente(nui)
        if pacientes != None:
            return jsonify(pacientes)
        else:
            return jsonify({'message': 'Paciente not found'}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    
@main.route('/add', methods=['POST'])
def add_paciente():
    try:
        nui = request.json.get('nui')
        nui_terapeuta = request.json.get('nui_terapeuta')
        nombre = request.json.get('nombre')
        apellido = request.json.get('apellido')
        edad = request.json.get('edad')
        direccion = request.json.get('direccion')
        estado = request.json.get('estado')
        
        # Validar que los campos no sean nulos
        if nui is None or nui_terapeuta is None or nombre is None or apellido is None or edad is None or direccion is None or estado is None:
            return jsonify({'message': 'Todos los campos son obligatorios'}), 400
        
        # Validar tipo de dato y longitud
        if not isinstance(nui, str) or len(nui) > 10:
            return jsonify({'message': 'El NUI debe ser una cadena de texto de máximo 10 caracteres'}), 400
        if not isinstance(nui_terapeuta, str) or len(nui_terapeuta) > 10:
            return jsonify({'message': 'El NUI del terapeuta debe ser una cadena de texto de máximo 10 caracteres'}), 400
        if not isinstance(nombre, str) or len(nombre) > 20:
            return jsonify({'message': 'El nombre debe ser una cadena de texto de máximo 20 caracteres'}), 400
        if not isinstance(apellido, str) or len(apellido) > 20:
            return jsonify({'message': 'El apellido debe ser una cadena de texto de máximo 20 caracteres'}), 400
        if not isinstance(edad, int):
            return jsonify({'message': 'La edad debe ser un valor numérico entero'}), 400
        if not isinstance(direccion, str) or len(direccion) > 100:
            return jsonify({'message': 'La dirección debe ser una cadena de texto de máximo 100 caracteres'}), 400
        if not isinstance(estado, bool):
            return jsonify({'message': 'El estado debe ser un valor booleano (true o false)'}), 400
        
        paciente = Paciente(nui, nui_terapeuta, nombre, apellido, edad, direccion, estado)
        affected_rows = PacienteModel.add_paciente(paciente)
        if affected_rows == 1:
            return jsonify({'nui': paciente.nui, 'message': 'Paciente añadido correctamente'}), 200
        else:
            return jsonify({'message': 'Error on insert'}), 500
    except Exception as ex: 
        return jsonify({'message': str(ex)}), 500
    
@main.route('/update/<nui>', methods=['PUT'])
def update_paciente(nui):
    try:
        nui_terapeuta = request.json.get('nui_terapeuta')
        nombre = request.json.get('nombre')
        apellido = request.json.get('apellido')
        edad = request.json.get('edad')
        direccion = request.json.get('direccion')
        estado = request.json.get('estado')
        
        # Validar que los campos no sean nulos
        if nui_terapeuta is None or nombre is None or apellido is None or edad is None or direccion is None or estado is None:
            return jsonify({'message': 'Todos los campos son obligatorios'}), 400
        
        # Validar tipo de dato y longitud
        if not isinstance(nui_terapeuta, str) or len(nui_terapeuta) > 10:
            return jsonify({'message': 'El NUI del terapeuta debe ser una cadena de texto de máximo 10 caracteres'}), 400
        if not isinstance(nombre, str) or len(nombre) > 20:
            return jsonify({'message': 'El nombre debe ser una cadena de texto de máximo 20 caracteres'}), 400
        if not isinstance(apellido, str) or len(apellido) > 20:
            return jsonify({'message': 'El apellido debe ser una cadena de texto de máximo 20 caracteres'}), 400
        if not isinstance(edad, int):
            return jsonify({'message': 'La edad debe ser un valor numérico entero'}), 400
        if not isinstance(direccion, str) or len(direccion) > 100:
            return jsonify({'message': 'La dirección debe ser una cadena de texto de máximo 100 caracteres'}), 400
        if not isinstance(estado, bool):
            return jsonify({'message': 'El estado debe ser un valor booleano (true o false)'}), 400
        
        paciente = Paciente(nui, nui_terapeuta, nombre, apellido, edad, direccion, estado)
        affected_rows = PacienteModel.update_paciente(paciente)
        if affected_rows == 1:
            return jsonify({'nui': paciente.nui, 'message': 'Paciente actualizado correctamente'}), 200
        else:
            return jsonify({'message': 'Error on update'}), 500
    except Exception as ex: 
        return jsonify({'message': str(ex)}), 500
    
@main.route('/delete/<nui>', methods=['DELETE'])
def delete_paciente(nui):
    try:
        paciente = Paciente(nui)
        affected_rows = PacienteModel.delete_paciente(paciente)
        if affected_rows == 1:
            return jsonify({'nui': paciente.nui, 'message': 'Paciente eliminado correctamente'}), 200
        else:
            return jsonify({'message': 'Error on delete'}), 500
    except Exception as ex: 
        return jsonify({'message': str(ex)}), 500