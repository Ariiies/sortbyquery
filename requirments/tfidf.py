from numpy import asarray as array, log10
class TF_IDF:
    def __init__(self, corpus):
        self.__corpus = corpus.get_corpus()
        self.__vocabulary = corpus.get_vocabulary()
        self.data = corpus.Data

        # function to calcute TF (term frecuency) with the operation tf = nt/tt where nt is the number of time
        # that a word is repeated in the doc and tt is the number of total words in the doc.
        # funcion que calcula el TF con la formula TF(palabra) = nt/tt donde: nt es el numero de veces
        # que se repite el termino y tt es elnumero total de terminos.
    @property 
    def TF(self): 
        tf = []
        for i in range(len(self.__corpus)):
            tfe=[]
            for word in self.__vocabulary:
                tfe.append(self.data[word][f'doc{i+1}']/len(self.__corpus[i].split()))
            tf.append(tfe)
        return array(tf)
    
        # function to calcute the IDF (inverse document frecuency) with the operation idf = log(n/wdf)
        # where n is the number of total documents and wdf is the amount of documents where the word appear
        # funcion que calcula el IDF usando la formula IDF(palabra)=log(n/wdf) donde: n es el numero de
        # documentos y wdf es la cantidad de documentos en los que aparece la palabra.
    @property 
    def IDF(self): 
        idf = []
        for text in self.__corpus:
            idfe = []
            for word in self.__vocabulary:
                n = log10((len(self.__corpus))/self.data[word]['exist in'])
                idfe.append(n)
            idf.append(idfe)
        return array(idf)
    
        # function to calculate the TF-IDF multiplicate the matriz of TF and IDF
        # funcion que calcula el TF-IDF multiplicando las matrices TF e IDF,
    @property 
    def TF_IDF(self):
        return self.TF*self.IDF