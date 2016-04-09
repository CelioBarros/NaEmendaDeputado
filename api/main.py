from flask import Flask, make_response, request, Response
import json
import api_deputado

app = Flask(__name__)


@app.route('/api/deputado/<id_deputado>')
def info_pessoais_deputado(id_deputado):
	response = api_deputado.info_pessoais_deputado(id_deputado)
	response = make_response(response)
	response.headers['Access-Control-Allow-Origin'] = "*"
	return response


if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0', port=5002)