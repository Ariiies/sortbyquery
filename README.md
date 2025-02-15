## Sort by query

sortbyquery is a project that enables searching and ranking documents based on their similarity to a given query. Utilizing the TF-IDF model and cosine similarity, the system analyzes a corpus of documents and returns a sorted list of those that are most relevant to the query, facilitating information retrieval and effective searching in large datasets.
The requirements are:
- [**Corpy**](https://www.github.com/Ariiies/corpy).
    - *For to have data available about the words and documents that make up a corpus.*
- [**TF-IDF**](https://www.github.com/Ariiies/tfidf).
    - *For to have the weight of words in the coprus, use **corpy**.*
- **simbycos.**
    - *Brings two functios.*
        - *queryvector.*
            -*function to vectorize a query with *IDF* data. Needs three inputs, a **query**, the **vocabulary** of the corpus and the **IDF**.*
        - *SBC.*
            -*Calculate similitub by coseno, needs two vectors of equal longitud, a **queryvector** and a **TF-IDF** list.*
- [**Quicksort**](https://www.github.com/Ariiies/quicsort).
    - *A version of the classic sorting algorithm, this case use a modificated version that receives an input of three element by item of the list.*
        - *First element is the title.*
        - *Second element is the content.*
        - *Third element is a vector of the query with the **IDF** of the corpus (it appends during the sort_by_query functionality).*
