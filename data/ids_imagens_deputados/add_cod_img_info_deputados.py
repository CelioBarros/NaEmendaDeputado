

dep_id_camara = open("deputados_id_camara.csv", "r")
lines = dep_id_camara.readlines()


info_deputados = open("../info_deputados.csv", "r")

# header = info_deputados.readlines()[0]
# header = header.rstrip() + ';"cod_img"'

rows = info_deputados.readlines()[1:]


f_out = open("info_deputados_out.csv","w")
# f_out.write(header)

for row in rows:
	row = row.rstrip().split(";")

	for line in lines:
		line = line.rstrip().split(";")

		print row[0].replace('"',"")
		print line[0]

		if row[0].replace('"',"") == line[0]:
			row.append('"' + line[2] + '"')

			row = ";".join(row) + "\n"
			f_out.write(row)




dep_id_camara.close()
info_deputados.close()
f_out.close()