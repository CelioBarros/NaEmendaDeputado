from flask import Flask, make_response, request, Response
import json
import api_deputado
import unicodedata

app = Flask(__name__)


@app.route('/api/deputado/<id_deputado>')
def info_pessoais_deputado(id_deputado):
	response = api_deputado.info_pessoais_deputado(str(unicodedata.normalize('NFKD', id_deputado).encode('utf-8','ignore')))
	response = make_response(response)
	response.headers['Access-Control-Allow-Origin'] = "*"
	return response

@app.route('/api/todos_deputados')
def todos_deputados():
	response = api_deputado.todos_deputados()
	response = make_response(response)
	response.headers['Access-Control-Allow-Origin'] = "*"
	return response

@app.route('/api/deputado/<id_deputado>/convenio/<id_convenio>')
def convenio(id_deputado,id_convenio):
	id_deputado = str(unicodedata.normalize('NFKD', id_deputado).encode('utf-8','ignore'))
	id_convenio = str(unicodedata.normalize('NFKD', id_convenio).encode('utf-8','ignore'))
	response = api_deputado.convenio(id_deputado,id_convenio)
	response = make_response(response)
	response.headers['Access-Control-Allow-Origin'] = "*"
	return response
	
@app.route('/api/deputado/<id_deputado>/convenios')
def convenios_por_deputado(id_deputado):
	response = api_deputado.convenios_por_deputado(str(unicodedata.normalize('NFKD', id_deputado).encode('utf-8','ignore')))
	response = make_response(response)
	response.headers['Access-Control-Allow-Origin'] = "*"
	return response

@app.route('/api/busca/<nome_deputado>')
def busca_deputado(nome_deputado):
	response = api_deputado.busca(str(unicodedata.normalize('NFKD', nome_deputado).encode('utf-8','ignore')))
	response = make_response(response)
	response.headers['Access-Control-Allow-Origin'] = "*"
	return response

@app.route('/api/deputado/<id_deputado>/temas')
def temas_por_deputado(id_deputado):
	response = api_deputado.temas_por_deputado(str(unicodedata.normalize('NFKD', id_deputado).encode('utf-8','ignore')))
	response = make_response(response)
	response.headers['Access-Control-Allow-Origin'] = "*"
	return response
	
if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0', port=5002)