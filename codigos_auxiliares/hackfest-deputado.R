library(dplyr)
library(tm)
library(stringr)

data <- read.csv("dataJoinedDepFed.csv",sep=";",encoding = "UTF-8")
options(scipen=999)
data$VL_GLOBAL_NUMERIC <- gsub("[R$ ]","",data$VL_GLOBAL)
data$VL_GLOBAL_NUMERIC <- gsub("[.]","",data$VL_GLOBAL_NUMERIC)
data$VL_GLOBAL_NUMERIC <- gsub("[,]",".",data$VL_GLOBAL_NUMERIC)

data.deputados <- data %>%
        filter(Autor..Tipo. =="DEPUTADO FEDERAL") %>%
        distinct(Autor,Autor..UF.,Partido) %>%
        mutate(Autor.id = paste(Autor, Autor..UF., sep = '_')) %>%
        group_by(ID_PROPOSTA,Autor.id) %>%
        mutate(TotalConvenios = as.character(sum(as.numeric(VL_GLOBAL_NUMERIC)))) %>%
        ungroup() %>%
        select(Autor.id,Autor,Autor..UF.,Partido,TotalConvenios) %>%
        arrange(Autor.id)

#write.table(data.deputados,"/home/celio/Desenvolvimento/Estudo/NaEmendaDeputado/data/info_deputados.csv",sep=";",row.names = F)

convenio.deputados <- data %>%
        filter(Autor..Tipo. =="DEPUTADO FEDERAL" & !is.na(ID_CONVENIO)) %>%
        mutate(Autor.id = paste(Autor, Autor..UF., sep = '_')) %>%
        distinct(ID_CONVENIO,Autor.id) %>%
        select(Autor.id,ID_CONVENIO,TX_OBJETO_CONVENIO,
               VL_GLOBAL,VL_REPASSE,DT_PUBLICACAO,acao.ab)

#write.table(convenio.deputados,"/home/celio/Desenvolvimento/Estudo/NaEmendaDeputado/data/convenio_deputados.csv",sep=";",row.names = F)

sw = stopwords("pt-br")
topwords = function(words){
  txt_conv = str_replace_all(words, pattern = "c\\(", "")
  txt_conv = str_replace_all(txt_conv, pattern = "[[:punct:]]", "")
  txt_conv = str_replace_all(txt_conv, pattern = "\\s+", " ")
  txt_list = str_split(txt_conv, pattern = " ")
  title_words = tolower(unlist(txt_list))	
  
  title_words = title_words[!(tolower(title_words) %in% sw)]
  title_words = paste(title_words, collapse=" ")
  title_words
}

lda.data <- data %>%
  filter(Autor..Tipo. =="DEPUTADO FEDERAL" & !is.na(ID_CONVENIO)) %>%
  mutate(Autor.id = paste(Autor, Autor..UF., sep = '_')) %>%
  distinct(ID_CONVENIO,Autor.id) %>%
  mutate(TX_OBJETO_CONVENIO = gsub("[,]","",TX_OBJETO_CONVENIO)) %>%
  group_by(Autor.id) %>%
  summarise(TEXTO_POR_AUTOR = topwords(paste(TX_OBJETO_CONVENIO, collapse=" ")))

  
#write.table(lda.data,"/home/celio/Desenvolvimento/Estudo/NaEmendaDeputado/lda/lda_autor_conv.csv",row.names = F, sep=";")
