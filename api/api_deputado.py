# encoding: utf-8

import json
import csv
import unicodedata
import time
import os


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
				info_deputado = {"nome":nome_deputado,"uf":row['Autor..UF.'], "partido":row['Partido'], "id_deputado":autor_id, "TotalConvenios":row['TotalConvenios'],
				"cod_img": "http://www.camara.leg.br/internet/deputado/bandep/" + row['CodImg'] + ".jpg"}
				break
	print json.dumps(info_deputado)
		
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
			info_deputado = {"nome":nome_deputado,"uf":row['Autor..UF.'], "partido":row['Partido'], "id_deputado":autor_id, "TotalConvenios":row['TotalConvenios']}
			lista_deputados.append(info_deputado)
	return json.dumps(lista_deputados)

def	convenio(id_deputado,id_convenio):
	info_convenio = {}
	with open('../data/convenio_deputados.csv') as csvfile:
		reader = csv.DictReader(csvfile, delimiter=";")
		for row in reader:
			autor_id = str(row['Autor.id'])
			autor_id = force_decode(str(autor_id))
			autor_id = str(unicodedata.normalize('NFKD', autor_id).encode('utf-8','ignore'))
			convenio_id = str(unicodedata.normalize('NFKD', force_decode(row['ID_CONVENIO'])).encode('utf-8','ignore'))

			if (id_deputado == autor_id and id_convenio == convenio_id):
				objeto_convenio = str(unicodedata.normalize('NFKD', force_decode(row['TX_OBJETO_CONVENIO'])).encode('utf-8','ignore'))
				vl_global = str(unicodedata.normalize('NFKD', force_decode(row['VL_GLOBAL'])).encode('utf-8','ignore'))
				vl_repasse = str(unicodedata.normalize('NFKD', force_decode(row['VL_REPASSE'])).encode('utf-8','ignore'))
				dt_publicacao = str(unicodedata.normalize('NFKD', force_decode(row['DT_PUBLICACAO'])).encode('utf-8','ignore'))
				acao = str(unicodedata.normalize('NFKD', force_decode(row['acao.ab'])).encode('utf-8','ignore'))
				info_convenio = { 
					"id_deputado": id_deputado,
					"id_convenio": id_convenio,
					"objeto_convenio":objeto_convenio,
					"vl_global":vl_global, "vl_repasse":vl_repasse, 
					"dt_publicacao":dt_publicacao,
					"acao": acao}
	return json.dumps(info_convenio)

def	convenios_por_deputado(id_deputado):
	lista_convenios = []
	with open('../data/convenio_deputados.csv') as csvfile:
		reader = csv.DictReader(csvfile, delimiter=";")
		for row in reader:
			autor_id = str(row['Autor.id'])
			autor_id = force_decode(str(autor_id))
			autor_id = str(unicodedata.normalize('NFKD', autor_id).encode('utf-8','ignore'))

			if (id_deputado == autor_id):
				id_convenio = str(unicodedata.normalize('NFKD', force_decode(row['ID_CONVENIO'])).encode('utf-8','ignore'))
				objeto_convenio = str(unicodedata.normalize('NFKD', force_decode(row['TX_OBJETO_CONVENIO'])).encode('utf-8','ignore'))
				vl_global = str(unicodedata.normalize('NFKD', force_decode(row['VL_GLOBAL'])).encode('utf-8','ignore'))
				vl_repasse = str(unicodedata.normalize('NFKD', force_decode(row['VL_REPASSE'])).encode('utf-8','ignore'))
				dt_publicacao = str(unicodedata.normalize('NFKD', force_decode(row['DT_PUBLICACAO'])).encode('utf-8','ignore'))
				acao = str(unicodedata.normalize('NFKD', force_decode(row['acao.ab'])).encode('utf-8','ignore'))
				info_convenio = { 
					"id_deputado": id_deputado,
					"id_convenio": id_convenio,
					"objeto_convenio":objeto_convenio,
					"vl_global":vl_global, "vl_repasse":vl_repasse, 
					"dt_publicacao":dt_publicacao,
					"acao": acao}
				lista_convenios.append(info_convenio)
	return json.dumps(lista_convenios)

def busca(nome_deputado):
	deputados = json.loads(todos_deputados())
	out = []
	for deputado in deputados:
		nome = deputado['nome']
		if nome_deputado.lower() in nome.lower():
			out.append(deputado)

	return json.dumps(out)




def temas_por_deputado(id_deputado):
	info_deputado = {}
	with open('../data/dep_temas.csv') as csvfile:
		reader = csv.DictReader(csvfile, delimiter=",")
		for row in reader:
			autor_id = str(row['Autor.id'])
			autor_id = force_decode(str(autor_id))
			autor_id = str(unicodedata.normalize('NFKD', autor_id).encode('utf-8','ignore'))

			if (id_deputado == autor_id):
				info_deputado = {"id_deputado":autor_id, "Temas":row['TEMAS']}
				break
	return json.dumps(info_deputado)
