from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>app is up</p>"


@app.route('/hello', methods=['POST'])
def hello():
   name = request.form.get('name')
   msg = "hello " + name
   return msg

## especifico da app

musicas = [
    {
        "id": 1,
        "nome": "Wish You Were Here",
        "ano": 1975,
        "artista": "Pink Floyd"
    },
    {
        "id": 2,
        "nome": "Eduardo e Monica",
        "ano": 1986,
        "artista": "Legiao Urbana"
    },
    {
        "id": 3,
        "nome": "Happy",
        "ano": 2014,
        "artista": "Pharrell Williams"
    }
]

proximo_id = 4

def busca_musica(id):
    for m in musicas:
        if m['id'] == id:
            return m
    return False

@app.route('/musicas', methods=['GET'])
def get_musicas():
   return jsonify({"Musicas": musicas})


@app.route('/musicas/<indice>', methods=['GET'])
def get_musica_indice(indice):
   i = int(indice)
   m = busca_musica(i)
   if m:
      return jsonify(m)
   else:
      return '', 404

@app.route('/musicas', methods=['POST'])
def create_musica():
   global proximo_id
   m = request.get_json()
   m["id"] = proximo_id
   proximo_id += 1
   musicas.append(m)
   return jsonify(m), 201 

###

if __name__ == '__main__':
   app.run()