from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask import render_template

from resources.ConverteTemperatura import ConverteTemperatura

app = Flask(__name__,  static_url_path='/static')
api = Api(app)


parser = reqparse.RequestParser()
parser.add_argument('unidadeOrigem')
parser.add_argument('valor')
parser.add_argument('unidadeDestino')


class ConversorDeTemperatura(Resource):

    def post(self):
        args = parser.parse_args()
        return {
            'valorConvertido': ConverteTemperatura.checa_conversao(
                unidadeOrigem=args['unidadeOrigem'],
                unidadeDestino=args['unidadeDestino'],
                valor=args['valor']
            )
        }


api.add_resource(ConversorDeTemperatura, '/converte_temperatura/')


@app.route('/')
def index(name=None):
    return render_template('index.html', name=name)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
