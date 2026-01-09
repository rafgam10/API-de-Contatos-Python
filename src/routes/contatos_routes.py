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
        return jsonify({"erro": str(e)})

@contatos_bp.route("/", methods=["GET"])
def listar_contato():
    try:
        contatos = Contato.query.all()

        resultado = [
            {
                "id": c.id,
                "nome": c.nome,
                "email": c.email
            }
            for c in contatos
        ]

        return jsonify(resultado), 200

    except Exception as e:
        return jsonify({"erro": str(e)}), 500


@contatos_bp.route("/buscar", methods=["GET"])
def buscar_nome_ou_email():
    try:
        entrada = request.args.get("q", "").strip()

        if not entrada:
            return jsonify({"erro": "Parâmetro 'q' é obrigatório"}), 400

        # Decide automaticamente se é email ou nome
        if "@" in entrada:
            filtro = Contato.email.ilike(entrada)
        else:
            filtro = Contato.nome.ilike(f"%{entrada}%")

        contatos = Contato.query.filter(filtro).all()

        if not contatos:
            return jsonify([]), 200

        return jsonify([
            {
                "id": c.id,
                "nome": c.nome,
                "email": c.email,
                "telefone": c.telefone
            }
            for c in contatos
        ]), 200

    except Exception as e:
        return jsonify({"erro": "Erro interno do servidor"}), 500

@contatos_bp.route("/", methods=["PUT"])
def editar_contato():
    try:
        
        data = request.get_json()
        contato_id = data["id"]
        
        if db.session.query(Contato).filter(Contato.id == contato_id).first():
            select_contato = db.session.query(Contato).filter(Contato.id == contato_id).first()
            select_contato.nome = data["novo_nome"]
            select_contato.email = data["novo_email"]
            select_contato.telefone = data["novo_telefone"]
            
            db.session.commit()
            
            return jsonify({
                "message": {
                    "id": select_contato.id,
                    "novo_nome": select_contato.nome,
                    "novo_email": select_contato.email,
                    "novo_telefone": select_contato.telefone  
                }
            }), 200
        else:
            return jsonify({"message": "contato não foi localizado"}), 404

    except Exception as e:
        return jsonify({"erro": str(e)}), 500
    
@contatos_bp.route("/", methods=["DELETE"])
def excluir_contato():
    try:
        
        data = request.get_json()
        
        select_contato = db.session.query(Contato).filter(Contato.id == data["id"]).first()
        db.session.delete(select_contato)
        db.session.commit()
        
        return jsonify({"message": "Contato excluido com sucesso!"}), 200
    
    except Exception as e:
        return jsonify({"erro": str(e)}), 500