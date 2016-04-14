library(dplyr)
library(stringr)
library(tm)
library(rjson)
sw = stopwords("pt-br")

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
