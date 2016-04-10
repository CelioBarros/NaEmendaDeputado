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
			autor_id = str(unicodedata.normalize('NFKD', autor_id).encode('utf-8','ignore'))

			if (id_deputado == autor_id):
				nome_deputado = str(unicodedata.normalize('NFKD', force_decode(row['Autor'])).encode('utf-8','ignore'))
				info_deputado = {"nome":nome_deputado,"uf":row['Autor..UF.'], "partido":row['Partido'], "id_deputado":autor_id}
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
			autor_id = str(unicodedata.normalize('NFKD', force_decode(row['Autor.id'])).encode('utf-8','ignore'))
			nome_deputado = str(unicodedata.normalize('NFKD', force_decode(row['Autor'])).encode('utf-8','ignore'))
			info_deputado = {"nome":nome_deputado,"uf":row['Autor..UF.'], "partido":row['Partido'], "id_deputado":autor_id}
			lista_deputados.append(info_deputado)
	return json.dumps(lista_deputados)

def	convenio(id_convenio):
	return json.dumps({"convenio":"Saude"})

def	convenios_por_deputado(id_deputado):
	lista_convenios = []
	with open('../data/convenio_deputados.csv') as csvfile:
		reader = csv.DictReader(csvfile, delimiter=";")
		for row in reader:
			autor_id = str(row['ID_AUTOR'])
			autor_id = force_decode(str(autor_id))
			autor_id = str(unicodedata.normalize('NFKD', autor_id).encode('utf-8','ignore'))

			if (id_deputado == autor_id):
				objeto_convenio = str(unicodedata.normalize('NFKD', force_decode(row['TX_OBJETO_CONVENIO'])).encode('utf-8','ignore'))
				vl_global = str(unicodedata.normalize('NFKD', force_decode(row['VL_GLOBAL'])).encode('utf-8','ignore'))
				vl_repasse = str(unicodedata.normalize('NFKD', force_decode(row['VL_REPASSE'])).encode('utf-8','ignore'))
				dt_publicacao = str(unicodedata.normalize('NFKD', force_decode(row['DT_PUBLICACAO'])).encode('utf-8','ignore'))
				acao = str(unicodedata.normalize('NFKD', force_decode(row['acao.ab'])).encode('utf-8','ignore'))
				info_convenio = {
					"objeto_convenio":objeto_convenio,
					"vl_global":vl_global, "vl_repasse":vl_repasse, 
					"dt_publicacao":dt_publicacao,
					"acao": acao}
				lista_convenios.append(info_convenio)
	return json.dumps(lista_convenios)