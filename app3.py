from flask import Flask, jsonify, request

app = Flask(__name__)

usuarios = []


@app.route("/info", methods=["GET"])
def info():
    return jsonify({
        "sistema": "Sistema de Gestión de Usuarios",
        "version": "1.0"
    })


@app.route("/crear_usuario", methods=["POST"])
def crear_usuario():
    data = request.json

    if not data or "nombre" not in data or "correo" not in data:
        return jsonify({
            "error": "El nombre y el correo son obligatorios"
        }), 400

    usuario = {
        "nombre": data["nombre"],
        "correo": data["correo"]
    }

    usuarios.append(usuario)

    return jsonify({
        "mensaje": "Usuario creado exitosamente",
        "usuario": usuario
    }), 201


@app.route("/usuarios", methods=["GET"])
def obtener_usuarios():
    return jsonify(usuarios)


if __name__ == "__main__":
    app.run(debug=True)