from flask import Flask, jsonify, request
from flask_cors import CORS 
from lambic import LAMBIC
from lagers import LAGER  
app = Flask(__name__)
CORS(app)
#WIKI DE EJEMPLO LOCAL
wiki_estilos = [LAMBIC,LAGER]

  
marcas = [ 
    {"nombre": "Cruzcampo", "origen": "Sevilla", "descripcion": "Descripción 1", "nota_media": 7.5, "urlImagen": 'https://www.liderlogo.es/wp-content/uploads/2022/12/pasted-image-0-2-6-768x538.png'},
    {"nombre": "Alhambra", "origen": "Granada", "descripcion": "Descripción 6", "nota_media": 5, "urlImagen":'https://upload.wikimedia.org/wikipedia/commons/d/d2/Cervezas_Alhambra_logo.png'},
    {"nombre": "La bestia", "origen": "Salamanca", "descripcion": "Descripción 3", "nota_media": 4.2, "urlImagen": 'https://labestiacraftbeer.com/wp-content/uploads/logo-1.png'},
    {"nombre": "La pirata", "origen": "Barcelona", "descripcion": "Descripción 2", "nota_media": 8, "urlImagen": "https://cervesalapirata.com/wp-content/uploads/2020/07/negro.png"},
    {"nombre": "German kraft", "origen": "Alemania", "descripcion": "Descripción 4", "nota_media": 4.7, "urlImagen": "https://assets-global.website-files.com/60cc890f8bc29df46a736033/616d50cf795308d24f721b1c_german-kraft-homepage-open-graph.jpg"},
    {"nombre": "Mahou", "origen": "Madrid", "descripcion": "Descripción 5", "nota_media": 3.9, "urlImagen":'https://www.atleticodemadrid.com/system/fotosponsorbigs/63/large/mahou_1200_color.png?1525800196'}
]

  
 
@app.route('/estilosWiki', methods=['GET'])
def stylesWiki():
    return jsonify([estilo.to_dict() for estilo in wiki_estilos])
  
 
@app.route('/marcas', methods=['GET'])
def marcass():
    return jsonify(marcas)
 
  
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
