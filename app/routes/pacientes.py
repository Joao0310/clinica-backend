from flask import Blueprint, request, jsonify, current_app
from datetime import datetime
from bson import ObjectId

pacientes_bp = Blueprint("pacientes", __name__)


@pacientes_bp.route("/", methods=["POST"])
def criar_paciente():
    try:
        dados = request.get_json()

        campos_obrigatorios = ["nome", "data_nascimento", "contato", "especialidade"]

        for campo in campos_obrigatorios:
            if campo not in dados:
                return jsonify({"erro": f"Campo obrigatório: {campo}"}), 400

        paciente = {
            "nome": dados["nome"],
            "data_nascimento": dados["data_nascimento"],
            "contato": dados["contato"],
            "especialidade": dados["especialidade"],
            "notas": dados.get("notas", ""),
            "criado_em": datetime.utcnow()
        }

        db = current_app.extensions["mongo_db"]
        resultado = db["pacientes"].insert_one(paciente)

        return jsonify({
            "mensagem": "Paciente criado com sucesso",
            "id": str(resultado.inserted_id)
        }), 201

    except Exception as e:
        return jsonify({"erro": str(e)}), 500
    
@pacientes_bp.route("/", methods=["GET"])
def listar_pacientes():
    try:
        db = current_app.extensions["mongo_db"]
        pacientes = list(db["pacientes"].find())

        resultado = []

        for p in pacientes:
            resultado.append({
                "id": str(p["_id"]),
                "nome": p.get("nome"),
                "data_nascimento": p.get("data_nascimento"),
                "contato": p.get("contato"),
                "especialidade": p.get("especialidade"),
                "observacoes": p.get("observacoes")
            })

        return jsonify(resultado), 200

    except Exception as e:
        return jsonify({"erro": str(e)}), 500
    
@pacientes_bp.route("/<id>", methods=["GET"])
def buscar_paciente_por_id(id):
    try:
        db = current_app.extensions["mongo_db"]

        paciente = db["pacientes"].find_one({"_id": ObjectId(id)})

        if not paciente:
            return jsonify({"erro": "Paciente não encontrado"}), 404

        resultado = {
            "id": str(paciente["_id"]),
            "nome": paciente.get("nome"),
            "data_nascimento": paciente.get("data_nascimento"),
            "contato": paciente.get("contato"),
            "especialidade": paciente.get("especialidade"),
            "observacoes": paciente.get("observacoes")
        }

        return jsonify(resultado), 200

    except Exception as e:
        return jsonify({"erro": "ID inválido ou erro na busca"}), 400
    
@pacientes_bp.route("/<id>", methods=["PUT"])
def atualizar_paciente(id):
    try:
        dados = request.get_json() or {}

        db = current_app.extensions["mongo_db"]

        campos_permitidos = ["nome", "data_nascimento", "contato", "especialidade", "observacoes"]
        atualizacoes = {k: v for k, v in dados.items() if k in campos_permitidos}

        if not atualizacoes:
            return jsonify({"erro": "Nenhum campo válido para atualizar"}), 400

        atualizacoes["atualizado_em"] = datetime.utcnow()

        resultado = db["pacientes"].update_one(
            {"_id": ObjectId(id)},
            {"$set": atualizacoes}
        )

        if resultado.matched_count == 0:
            return jsonify({"erro": "Paciente não encontrado"}), 404

        return jsonify({"mensagem": "Paciente atualizado com sucesso"}), 200

    except Exception:
        return jsonify({"erro": "ID inválido ou erro na atualização"}), 400
    
@pacientes_bp.route("/<id>", methods=["DELETE"])
def excluir_paciente(id):
    try:
        db = current_app.extensions["mongo_db"]

        resultado = db["pacientes"].delete_one({"_id": ObjectId(id)})

        if resultado.deleted_count == 0:
            return jsonify({"erro": "Paciente não encontrado"}), 404

        return jsonify({"mensagem": "Paciente removido com sucesso"}), 200

    except Exception:
        return jsonify({"erro": "ID inválido ou erro na remoção"}), 400