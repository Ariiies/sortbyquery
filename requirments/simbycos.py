from numpy import asarray as array, dot, linalg as norm 

# function to vectorize a query with tfidf data 
def queryvector(query, vocabulary, idf): 
    nq = []
    bow = {}
    for word in query.split():
        if word in bow: bow[word] = bow[word] + 1
        else: bow[word] = 1
    for ele in vocabulary:
        if ele in bow: 
            nq.append(bow[ele]/len(query.split()))
        else: nq.append(0)
    return array(nq*idf[0])  

# similitud by cosene: recuve 2 arrays of equal longitud
def sbc(A,B):
    pp, ma, mb = dot(A, B), norm.norm(A), norm.norm(B)   
    if pp == 0.0: 
        return 0.0
    sc = pp / (ma * mb) 
    return sc

