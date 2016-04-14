library(dplyr)
library(stringr)
library(tm)
library(jsonlite)
library(ngram)
sw = stopwords("pt-br")

dados = read.csv("dadosunidos.csv",sep=";")

# 1. Subset de arquivo de input 
nas = which(is.na(dados$ID_CONVENIO))
dados2 = dados[-nas,]
desc_conv_dados = dados2[c("ID_CONVENIO","TX_OBJETO_CONVENIO","TX_JUSTIFICATIVA")]
#write.table(desc_conv_dados,"dadosconvenientes.csv",row.names=F,sep=";")

convenios_topwords = data.frame(ID=unique(desc_conv_dados$ID_CONVENIO), TOPWORDS = NA)

# Função para retornar ID_CONVENIO  e lista de top tags com valores
topwords = function(words){
txt_conv = str_replace_all(words, pattern = "c\\(", "")
txt_conv = str_replace_all(txt_conv, pattern = "[[:punct:]]", "")
txt_conv = str_replace_all(txt_conv, pattern = "\\s+", " ")
txt_list = str_split(txt_conv, pattern = " ")
title_words = tolower(unlist(txt_list))	
	
title_words = title_words[!(tolower(title_words) %in% sw)]


top_freqs = data.frame(word = as.factor(title_words)) %>% 
  group_by(word) %>% 
  tally(sort = TRUE) %>% 
  slice(1:50)

  top_freqs$wc = paste(top_freqs$word, top_freqs$n, sep=":")
  levels(droplevels((top_freqs)))
  res = paste(top_freqs$wc, collapse=', ' )
  res
}


# Juntando descrições de convênios com as mesmas IDs
desc = with(desc_conv_dados[-3], aggregate(list(TX_OBJETO_CONVENIO = TX_OBJETO_CONVENIO), list(ID_CONVENIO = ID_CONVENIO), paste))

# Iterando em cada conjunto de descrições e gerando as topwords
for (i in 1:nrow(desc)){
	desc2 = topwords(paste(desc[i,]$TX_OBJETO_CONVENIO,sep=" "))
	convenios_topwords[convenios_topwords$ID==desc[i,]$ID_CONVENIO,]$TOPWORDS = desc2
}

# Arquivo final com Ids dos convenios e tags
write.table(convenios_topwords,"id_convenios-tags.csv",sep=";",row.names=F)


# Criação do json file
sink("jsonf.json")
cat(toJSON(unname(split(convenios_topwords, 1:nrow(convenios_topwords)))))
sink()


	
