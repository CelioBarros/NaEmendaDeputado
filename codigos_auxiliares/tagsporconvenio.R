source("r_functions.R")

# Leitura de arquivos usados
emendas = read.csv("data/10_PropostasEmendaParlamentar.csv", sep=";")
convenios = read.csv("data/01_ConveniosProgramas.csv", sep=";")

### 1. Tags por convênios

# Selecionando colunas úteis para criação do arquivo
convenios = convenios[c("ID_CONVENIO","TX_OBJETO_CONVENIO")]

# Criando topwords para cada ID_CONVENIO
convenios_topwords = data.frame(ID=unique(convenios$ID_CONVENIO), TOPWORDS = NA)

# Juntando descrições de convênios com as mesmas IDs
desc = with(convenios, aggregate(list(TX_OBJETO_CONVENIO = TX_OBJETO_CONVENIO), list(ID_CONVENIO = ID_CONVENIO), paste))

# Iterando em cada conjunto de descrições e gerando as topwords
for (i in 1:nrow(desc)){
	desc2 = topwords(paste(desc[i,]$TX_OBJETO_CONVENIO,sep=" "))
	convenios_topwords[convenios_topwords$ID==desc[i,]$ID_CONVENIO,]$TOPWORDS = desc2
}

# Arquivo final com Ids dos convenios e tags
write.table(convenios_topwords,"gen_data/id_convenios-tags.csv",sep=";",row.names=F)


# Criação do json file
sink("gen_data/jsonf.json")
cat(toJSON(unname(split(convenios_topwords, 1:nrow(convenios_topwords)))))
sink()
