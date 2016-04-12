# coding: utf-8
from __future__ import print_function
from time import time
import sys
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.decomposition import NMF, LatentDirichletAllocation
from sklearn.datasets import fetch_20newsgroups
import numpy as np
import lda

def get_vocab(data_samples):
    vocab = set()
    for v in data_samples:
        tokens = v.split()
        for token in tokens:
            vocab.add(token)
    return tuple(vocab)


if len(sys.argv) != 2:
    print('usage: python topics_extraction_with_nmf_lda.py text-deputados.txt')
    sys.exit()

n_features = 1000
n_topics = 20
n_top_words = 10

# lendo os dados dos deputados
dep_file = open(sys.argv[1], 'r')
linha = dep_file.readline()
data_samples = linha.split(',')

# calculando tf-idf
print("Extracting tf-idf features for NMF...")
tfidf_vectorizer = TfidfVectorizer(max_df=0.95, min_df=2, #max_features=n_features,
                                   stop_words='english')
tfidf = tfidf_vectorizer.fit_transform(data_samples)
tf_vectorizer = CountVectorizer(max_df=0.95, min_df=2, max_features=n_features,
                                stop_words='english')
tf = tf_vectorizer.fit_transform(data_samples)


# aplicando LDA. Escolher mais iterações quando for executar para valer
new_model = lda.LDA(n_topics=20, n_iter=30, random_state=1)
new_model.fit(tf)

# imprimindo deputado e o tópico ao qual ele está mais relacionado. Aqui é
# importante que você saiba quem é o deputado 0, o deputado 1 e assim por diante. 
doc_topic = new_model.doc_topic_
for i in range(len(data_samples)):
    print("deputado: {} (top topic: {})".format(i, doc_topic[i].argmax()))

#gerando vocab
vocab = get_vocab(data_samples)

# imprimindo o vocabulário de cada tópico
topic_word = new_model.topic_word_
for i, topic_dist in enumerate(topic_word):
    topic_words = np.array(vocab)[np.argsort(topic_dist)][:-n_top_words:-1]
    print('Topic {}: {}'.format(i, ' '.join(topic_words)))
