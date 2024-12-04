from flask import Flask, request, jsonify

app = Flask(__name__)

# Base de datos en memoria
BD = [
    {"alias": "cpaz", "nombre": "Christian", "contactos": [{"alias": "lmunoz", "nombre": "Luisa"}, {"alias": "mgrau", "nombre": "Miguel"}], "mensajes": []},
    {"alias": "lmunoz", "nombre": "Luisa", "contactos": [{"alias": "mgrau", "nombre": "Miguel"}], "mensajes": []},
    {"alias": "mgrau", "nombre": "Miguel", "contactos": [{"alias": "cpaz", "nombre": "Christian"}], "mensajes": []}
]

# Función auxiliar para buscar un usuario por alias
def buscar_usuario(alias):
    return next((usuario for usuario in BD if usuario["alias"] == alias), None)

# Endpoint: Listar contactos
@app.route("/mensajeria/contactos", methods=["GET"])
def listar_contactos():
    alias = request.args.get("mialias")
    usuario = buscar_usuario(alias)
    if not usuario:
        return jsonify({"error": "Usuario no encontrado"}), 404
    return jsonify({contacto["alias"]: contacto["nombre"] for contacto in usuario["contactos"]})

# Endpoint: Agregar un contacto
@app.route("/mensajeria/contactos/<alias>", methods=["POST"])
def agregar_contacto(alias):
    data = request.get_json()
    contacto_alias = data.get("contacto")
    contacto_nombre = data.get("nombre", "")

    usuario = buscar_usuario(alias)
    if not usuario:
        # Si el usuario no existe, lo creamos
        usuario = {"alias": alias, "nombre": "Nuevo Usuario", "contactos": [], "mensajes": []}
        BD.append(usuario)

    # Validar si el contacto ya existe
    if any(c["alias"] == contacto_alias for c in usuario["contactos"]):
        return jsonify({"error": "El contacto ya existe"}), 400

    # Añadir contacto
    usuario["contactos"].append({"alias": contacto_alias, "nombre": contacto_nombre})
    return jsonify({"mensaje": "Contacto agregado exitosamente"}), 201

# Endpoint: Enviar mensaje
@app.route("/mensajeria/enviar", methods=["POST"])
def enviar_mensaje():
    data = request.get_json()
    usuario_alias = data.get("usuario")
    contacto_alias = data.get("contacto")
    mensaje = data.get("mensaje")

    usuario = buscar_usuario(usuario_alias)
    if not usuario:
        return jsonify({"error": "Usuario remitente no encontrado"}), 404

    if not any(c["alias"] == contacto_alias for c in usuario["contactos"]):
        return jsonify({"error": "El contacto no esta en la lista"}), 400

    destinatario = buscar_usuario(contacto_alias)
    if not destinatario:
        return jsonify({"error": "Usuario destinatario no encontrado"}), 404

    destinatario["mensajes"].append({"de": usuario["nombre"], "mensaje": mensaje})
    return jsonify({"mensaje": "Mensaje enviado exitosamente"}), 201

# Endpoint: Ver mensajes recibidos
@app.route("/mensajeria/recibidos", methods=["GET"])
def mensajes_recibidos():
    alias = request.args.get("mialias")
    usuario = buscar_usuario(alias)
    if not usuario:
        return jsonify({"error": "Usuario no encontrado"}), 404

    return jsonify(usuario["mensajes"])

if __name__ == "__main__":
    app.run(debug=True)

