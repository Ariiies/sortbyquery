from requirments.corpy import Corpy as cp
from requirments.tfidf import TF_IDF as tfidf
import requirments.simbycos as sc
from requirments.quicksort import quicksort as qs

# function to sort using the similitud by cosene with a query 
# and a matriz tf-idf
def sort_by_query(query, docs):
    corpus, new_doc = [], []
    for i in range(len(docs)):
        corpus.append(docs[i][1]) # extract the corpus, position 1 is for the position of the text in the list doc
    corp = cp(corpus) # create corpy object for TF-IDF object
    TF_IDF = tfidf(corp) # create TF-IDF object
    qv = sc.queryvector(query,corp.get_vocabulary(),TF_IDF.IDF) # create the query list 
    tf = TF_IDF.TF_IDF # for consume less resources, the tf object is asignated here
    for a in range(len(docs)):
        b= sc.sbc(qv,tf[a]) # similitud by cosene between queryvecyor and tf-idf of a doc
        new_doc.append([docs[a][0],docs[a][1],b]) # here includes values of the new doc with the ratios 
    size = len(new_doc) # need the size for one pointer
    qs(new_doc,0,size-1,True) # sort new doc with quicksort
    
    return new_doc



