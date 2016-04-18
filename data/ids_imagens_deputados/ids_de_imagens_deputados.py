##Unifica os ids dos deputados do site da camara com os ids do sistema (<nome_deputado>_<UF>)
import csv
id_deputados = open("pagina_deputados.csv","r")
lines = id_deputados.readlines()


deputados_estado = open("../info_deputados.csv", "r")
rows = deputados_estado.readlines()[1:]


f_out = open("deputados_id_camara.csv", "w")


for line in lines:
	line = line.split(";")

	for row in rows:
		row = row.split(";")

		if line[0] == row[1].replace('"', ""):
			line_resp = row[0].replace('"', "") + ";" + row[1].replace('"', "") + ";" + line[4] + "\n"
			print(line_resp)
			f_out.write(line_resp)

id_deputados.close()
deputados_estado.close()
f_out.close()