source("r_functions.R")

# Leitura de arquivos usados
emendas = read.csv("data/10_PropostasEmendaParlamentar.csv", sep=";")
convenios = read.csv("data/01_ConveniosProgramas.csv", sep=";")
deputados = read.csv("data/deputados.csv")

### 1. Tags por convênios

# Selecionando colunas úteis para criação do arquivo
convenios = convenios[c("ID_CONVENIO","TX_OBJETO_CONVENIO")]

# Criando topwords para cada ID_CONVENIO
convenios_topwords = data.frame(ID_CONVENIO=unique(convenios$ID_CONVENIO), TOPWORDS = NA)

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
sink("gen_data/jsonf-conv.json")
cat(toJSON(unname(split(convenios_topwords, 1:nrow(convenios_topwords)))))
sink()

### 1. Tags por deputados

# Linkar deputados a seus respectivos convênios 
emendas_sub = emendas[c("ID_CONVENIO","NM_RESPONS_PROPONENTE","CD_RESPONS_PROPONENTE")]
nas = which(is.na(emendas_sub$ID_CONVENIO))
emendas_sub = emendas_sub[-nas,]
depconv = merge(emendas_sub,convenios,by=c("ID_CONVENIO"))

# Juntando descrições de convênios com as mesmas IDs
descdep = with(depconv, aggregate(list(TX_OBJETO_CONVENIO = TX_OBJETO_CONVENIO), list(CD_RESPONS_PROPONENTE = CD_RESPONS_PROPONENTE), paste))
#write.csv(descdep,"depconv_csv",row.names=F)

# Criando topwords para cada ID_CONVENIO
deputados_topwords = data.frame(CD_RESPONS_PROPONENTE=unique(descdep$CD_RESPONS_PROPONENTE), TOPWORDS = NA)

# Iterando em cada conjunto de descrições e gerando as topwords
for (i in 1:nrow(descdep)){
	desc2 = topwords(paste(descdep[i,]$TX_OBJETO_CONVENIO,sep=" "))
	deputados_topwords[deputados_topwords$CD_RESPONS_PROPONENTE==descdep[i,]$CD_RESPONS_PROPONENTE,]$TOPWORDS = desc2
}

# Arquivo final com Nomes dos deputados e tags
dep_topwords = merge(deputados_topwords,emendas_sub[c("CD_RESPONS_PROPONENTE","NM_RESPONS_PROPONENTE")],by=c("CD_RESPONS_PROPONENTE"))
write.table(dep_topwords,"gen_data/deputados-tags.csv",sep=";",row.names=F)

# Criação do json file
sink("gen_data/jsonf-dep.json")
cat(toJSON(unname(split(dep_topwords, 1:nrow(dep_topwords)))))
sink()

