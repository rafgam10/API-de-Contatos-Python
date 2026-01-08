from flask import (
    Blueprint,
    request,
    jsonify
)

from src.models.contato_model import Contato
from src.settings.extensions import db

contatos_bp = Blueprint("contatos", __name__, url_prefix="/contatos")

@contatos_bp.route("/", methods=["POST"])
def criar_contato():
    try:
        
        data = request.get_json()
        novo_contato = Contato(**data)
        db.session.add(novo_contato)
        db.session.commit()
        
        return jsonify({
            "message": "Contato criando com sucesso!",
            "contato": {
                "id": novo_contato.id,
                "nome": novo_contato.nome,
                "email": novo_contato.email,
                "telefone": novo_contato.telefone
            }
        }), 201
    
    except Exception as e:
        db.session.rollback()
        return jsonify({"erro": e})

@contatos_bp.route("/", methods=["GET"])
def listar_contato():
    try:
        
        array_contatos = Contato.query.all()
        return jsonify({array_contatos}), 200
    
    except Exception as e:
        return jsonify({"erro": e})

@contatos_bp.route("/", methods=["GET"])
def buscar_nome_ou_email():
    try:
        data = request.get_json()
    
        select_contato = None
    
        if data["entrada"] in "@":
            select_contato = db.session.query(Contato).filter(email=data["entrada"]).first()
        else:
            select_contato = db.session.query(Contato).filter(nome=data["entrada"]).first()
        
        if select_contato == None:
            jsonify({"message": "Contato não foi encontrado"}), 404
            
        return jsonify({"message": {
            "id": select_contato.id,
            "nome": select_contato.nome,
            "email": select_contato.email,
            "telefone": select_contato.telefone
        }})
    except Exception as e:
        return jsonify({"erro": e})

@contatos_bp.route("/", methods=["PUT"])
def editar_contato():
    pass

@contatos_bp.route("/", methods=["DELETE"])
def excluir_contato():
    pass