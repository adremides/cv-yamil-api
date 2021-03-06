#!flask/bin/python
# -*- coding: UTF-8 -*-

from flask import Flask, request, jsonify, abort

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


@app.route('/')
def index():
    info = {
        "mensaje": "Bienvenido a la API del curriculum vitae de Yamil Jaskolowski.",
        "acciones": [
            "GET /curriculum",
            "POST /mensajes"
        ]
    }
    return jsonify(info)


@app.route('/curriculum', methods=['GET'])
def cv():
    url_imagen = request.host_url + "static/yo.jpg"
    cv = {
        "nombre": "Yamil",
        "apellido": "Jaskolowski",
        "residencia": "Argentina",
        "experiencia": [{
            "posicion": "< describe tu posición>",
            "empresa": "< nombre de tu empresa >",
            "desde": "< cuándo empezaste a trabajar >",
            "hasta": "< si ya no trabajas más, cuándo >",
            "descripcion": "< detalles >"
        }],
        "educación": {
            "nivel": "< nivel de tus estudios >",
            "titulo": "< nombre de tu carrera >",
            "institucion": "< dónde estudiaste >",
            "facultad": "< más detalles >"
        },
        "intereses": ["python", "apis", "enseñar"],
        "redes": {
            "github": "https://github.com/",
            "twitter": "https://twitter.com/",
            "linkedin": "https://www.linkedin.com/in/"
        },
        "foto": url_imagen
    }
    return jsonify(cv)


@app.route('/mensajes', methods=['POST'])
def contacto():
    mensaje = request.get_data()
    if not mensaje:
        abort(400, description="Debe enviar su mensaje en el body del POST.")
    print("MENSAJE DE CONTACTO: " + str(mensaje))
    return "Gracias por su mensaje."


if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=5050, debug=True)
    app.run()
