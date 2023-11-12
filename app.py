from flask import Flask, jsonify, render_template
from utils.pokeneas import createPokeNeas
import random
import os

app = Flask(__name__)
pokeneas_list = createPokeNeas()

@app.route('/pokeneas')
def get_pokeneas():
    pokenea = random.choice(pokeneas_list)
    response = {
        'id': pokenea['id'],
        'nombre': pokenea['name'],
        'altura': pokenea['height'],
        'habilidades': pokenea['abilities'],
    }
    return jsonify(response)

@app.route('/randompoke')
def randompoke():
    pokenea = random.choice(pokeneas_list)
    container_id = os.uname()[1]

    return render_template('random_pokenea.html', pokenea = pokenea, container_id = container_id)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)