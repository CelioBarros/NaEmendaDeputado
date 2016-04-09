import json

def info_pessoais_deputado(id_deputado):
	return json.dumps({"deputado":"Joao Arthur"})

def	convenio(id_convenio):
	return json.dumps({"convenio":"Saude"})

def	convenios_por_deputado(id_deputado):
	return json.dumps({"convenios":["convenio1","convenio2"]})