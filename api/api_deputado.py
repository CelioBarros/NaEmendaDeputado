# encoding: utf-8

import json
import csv
import unicodedata
import time


def info_pessoais_deputado(id_deputado):
	
	info_deputado = {}
	with open('../data/info_deputados.csv') as csvfile:
		reader = csv.DictReader(csvfile, delimiter=";")
		for row in reader:
			autor_id = str(row['Autor.id'])
			autor_id = force_decode(str(autor_id))
			autor_id = str(unicodedata.normalize('NFKD', autor_id).encode('ascii','ignore'))
			if (id_deputado == autor_id):
				info_deputado = {"nome":force_decode(row['Autor']),"uf":row['Autor..UF.'], "partido":row['Partido']}
				break
	return json.dumps(info_deputado)

def force_decode(string, codecs=['utf8', 'cp1252']):
    for i in codecs:
        try:
            return string.decode(i)
        except:
            pass

def todos_deputados():
	lista_deputados = []
	with open('../data/info_deputados.csv') as csvfile:
		reader = csv.DictReader(csvfile, delimiter=";")
		for row in reader:
			info_deputado = {}
			info_deputado = {"nome":row['Autor'],"uf":row['Autor..UF.'], "partido":row['Partido']}
			lista_deputados.append(info_deputado)
	return json.dumps(lista_deputados)

def	convenio(id_convenio):
	return json.dumps({"convenio":"Saude"})

def	convenios_por_deputado(id_deputado):
	return json.dumps({"convenios":["convenio1","convenio2"]})