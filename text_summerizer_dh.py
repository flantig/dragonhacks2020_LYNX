import pandas as pd
import numpy as np
import networkx as nx
import nltk
from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance

def main():
    top_n=2
    create_summary("test2.txt",top_n)



def read_art(file_name):
    #check if is None for diff aspects of file
    #sept functions to get sept date, text etc

    file=open(file_name,"r", encoding='utf-8')
    filedata=file.readlines()
    article=filedata[0].split(". ")
    sentences=[]

    for sentence in article:
        #print(sentence)
        sentences.append(sentence.replace("[^a-zA-Z]", " ").split(" "))
    sentences.pop()

    return sentences


def sent_sim(sent1, sent2, stop_words=None):

        if stop_words==None:
            stopwords=[]

        sent1=[k.lower() for k in sent1]
        sent2=[k.lower()for k in sent2]


        all_words = list(set(sent1 + sent2))

        #size of vector
        vector1=[0]* len(all_words)
        vector2=[0]*len(all_words)

        #all_words = (set(sent1 * sent2))
        #1st sentence vector
        for i in sent1:
            if i in stopwords:
                continue
            vector1[all_words.index(i)] +=1


        #2nd sentence vector

        for j in sent2:
            #check this
            if j in stopwords:
                continue
            vector2[all_words.index(j)]+=1

        #find cosine distance. How close are two vectors
        #is how similar they are

        return 1-cosine_distance(vector1,vector2)

def build_sim_matrix(sentences):
    #create empty matrix first
    sim_matrix=np.zeros((len(sentences),len(sentences)))

    for i1 in range(len(sentences)):
        for i2 in range(len(sentences)):
            if i1==i2:#make sure it is not the same sentence
                continue;
            #similarity matrix equals the corresponding
            # similarity of sentences list at index 1 and index2
            #send to function

            sim_matrix[i1][i2]=sent_sim(sentences[i1],sentences[i2])

        return sim_matrix

def create_summary(file_name, top_n=5):

    stop_words=stopwords.words('english')
    summarize_text=[]

    sentences=read_art(file_name)

    sent_sim_matrix=build_sim_matrix(sentences)

    sent_sim_graph=nx.from_numpy_array(sent_sim_matrix)
    sent_scores=nx.pagerank(sent_sim_graph)
    #to rank sentences

    ranked_sent=sorted(((sent_scores[i],s)for i,s in enumerate(sentences)),reverse=True)


    #print("indexes are:", ranked_sent)

    #for i in range(len(ranked_sent)):
    for i in range(top_n):
        summarize_text.append(" ".join(ranked_sent[i][1]))
        if i ==None:
            break
        #summarize_text.append(" ".join(ranked_sent[i][1]))
        #summarize_text.append(" ".join(str(i)))
    print("Summary: \n",".".join(summarize_text))



if __name__ == "__main__":
    main()
    exit(0)







