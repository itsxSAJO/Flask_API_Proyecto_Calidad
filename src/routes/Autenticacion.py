from flask import Blueprint, jsonify, request
from flask_cors import CORS

import uuid  # Para generar el id de terapeuta

# Entities
from models.entities.Terapeuta import Terapeuta

# Models
from models.TerapeutaModel import TerapeutaModel

main = Blueprint('auth_blueprint', __name__)
CORS(main, resources={r"/*": {"origins": "*"}})

@main.route('/', methods=['POST'])
def auth_terapeuta():
    try:
        nui = request.json.get('nui')
        
        # Validate non-null fields
        if nui is None:
            return jsonify({'message': 'Todos los campos son obligatorios'}), 400
        
        # Validate data type and length
        if not isinstance(nui, str) or len(nui) > 10:
            return jsonify({'message': 'El NUI debe ser una cadena de texto de máximo 10 caracteres'}), 400
        
        # Get terapeuta by NUI
        terapeuta = TerapeutaModel.get_terapeuta_by_nui(nui)
        if terapeuta is not None:
            return jsonify(terapeuta)
        else:
            return jsonify({'message': 'Terapeuta not found'}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500