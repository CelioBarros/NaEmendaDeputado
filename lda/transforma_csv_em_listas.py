# -*- coding: utf-8 -*-
import csv
import nltk

autores = []
convenios = []

with open('lda_autor_conv.csv') as csvfile:
	reader = csv.DictReader(csvfile, delimiter=";")
	for row in reader:
		autores.append(row['Autor.id'])
		convenios.append(row['TEXTO_POR_AUTOR'])

conv = open('convenios.txt', 'w')

conv.write(",".join(convenios))

conv.close()

aut = open('autores.txt', 'w')

aut.write(",".join(autores))

aut.close()