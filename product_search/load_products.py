import pandas as pd
import numpy as np

from get_embeddings import get_embedding

def store_product_embeddings(): # on a local npy file
    
    pd.set_option('display.expand_frame_repr', False)
    df = pd.read_csv("product_search/product_catalog_10000.csv")

    df["text_for_embedding"] = (
        df["product_name"] + ". " +
        df["category"] + ". " +
        df["description"]
    )

    #print(df.head(10))
    #print(df["text_for_embedding"].iloc[4828])

    # store product embeddings in a local .npy file
    text_to_be_embedded = df['text_for_embedding'].tolist()
    embeddings = [get_embedding(item) for item in text_to_be_embedded[:2000]]
    embeddings_np = np.array(embeddings)

    np.save("product_embeddings.npy", embeddings)

    print(embeddings_np.shape)
    
       
         