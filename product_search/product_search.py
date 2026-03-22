import numpy as np
import pandas as pd

from get_embeddings import get_embedding

embeddings = np.load("product_embeddings.npy")
print(embeddings.shape)

df = pd.read_csv("product_search/product_catalog_10000.csv")

def search_product_optimised(query, k=3):
    query_embeddings = get_embedding(query)
    
    # matrix multiplication with embeddings
    # (500 X 1536) @ (1536 X 1)
    # we get distance of query with each row  
    scores = embeddings @ query_embeddings # dot product (cosine)
    
    indexed_scores = [(score, idx) for idx, score in enumerate(scores)]
    indexed_scores.sort(reverse=True)
    top = indexed_scores[:k]
    
    top_indices = scores.argsort()[::-1][:k]
    print(df.iloc[top_indices][["product_name","category"]])