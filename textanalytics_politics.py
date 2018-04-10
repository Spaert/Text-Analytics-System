from pykafka import KafkaClient
import jieba
import sys
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import pandas as pd
import time
while True:
    client = KafkaClient(hosts="127.0.0.1:9092")
    topic = client.topics[b'politics']
    consumer = topic.get_simple_consumer(reset_offset_on_start=True,consumer_timeout_ms=5000)
    data = []
    for message in consumer:
        if message is not None:
            print (message.offset, (message.value).decode('utf-8'))
            data.append((message.value).decode('utf-8'))

    corpus = []

    for line in data:
        corpus.append(" ".join(jieba.cut(line.split(',')[0], cut_all=False)))    

    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform(corpus)
    print(tfidf.shape)

    words = vectorizer.get_feature_names()
    for i in range(len(corpus)):
        print('----Document %d----' % (i))
        for j in range(len(words)):
            if tfidf[i,j] > 1e-5:
                  print(words[j], tfidf[i,j])

    cv = CountVectorizer()
    term_doc = cv.fit_transform(corpus)

    transformer = TfidfTransformer()
    tfidf = transformer.fit_transform(term_doc)
    fv = tfidf.toarray()

    for i in range(len(fv)):
        print('----Document %d----' % (i))
        print(fv[i])

    top = [[0 for i in range(5)]for j in range(len(fv))]
    allx = [0 for i in range(len(fv))]
    sortx = [0 for i in range(len(fv))]

    for i in range(len(fv)):
        for j in range(len(fv)):
            if i != j:
                x = cosine_similarity(fv[i].reshape(1,-1),fv[j].reshape(1,-1)).astype(float)
                print(i,j,x[0][0])
                allx[j] = x[0][0]
                sortx[j] = x[0][0]
                array = np.array([i,j,x])
                #print(array)
        #print(allx) just have x
        sortx.sort(reverse = True)
        #print(sortx) sorted
        for k in range(5):
            for l in range(len(fv)):
                if sortx[k] == allx[l]:
                    #print(l) top5 will print
                    top[i][k] = l
                    break
    print(top)
    col = []
    for i in range(len(fv)):
        row = []
        row.append('Id_'+str(i))
        for j in range(5):
            row.append('sid_'+str(i)+str(top[i][j])) 
        col.append(row)
    pd.DataFrame(col).to_csv('politics.csv',index=False,header=False)
    time.sleep(108000)
