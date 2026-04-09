import pandas as pd
import numpy as np

# drop users who have not rated
# min max scaling
# row imputation (replace NAN with row average)
# build dict of user ratings
# convert each users' ratings -> unit vector
# build similarity matrix
def process_data():
    
    df = pd.read_csv("movie_ratings.csv")
    df = df.drop(columns=['Yukta', 'Priya', 'Harshita'])

    df = df.set_index("Movies_Name")
    pd.options.display.float_format = '{:.2f}'.format
    df = df.astype(float)

    df = min_max_scaling(df)
    df = replace_nan_with_row_avg(df)
    user_ratings = build_user_ratings(df)
    
    user_ratings = convert_to_unit_vector(user_ratings)
    #print(user_ratings)
    
    # build similarity matrix
    user_matrix = similarity_matrix(user_ratings)
    
    #print(user_matrix)
    
    df = pd.DataFrame(user_matrix)
    print(df)
    print(df.shape)
    
    
def min_max_scaling(df):
    m = df.values.copy()
    n = df.copy()
    print(m.shape)

    # column wise (axix = 0) min-max scaling
    rows, cols = m.shape
    for j in range(cols):    
     column_vals = []
     for i in range(rows):
         column_vals.append(df.iloc[i,j])
     
     min = np.nanmin(np.array(column_vals))
     max = np.nanmax(np.array(column_vals))
     for m in range(rows):
         if not np.isnan(df.iloc[m,j]):
            df.iloc[m,j] = (df.iloc[m,j] - min) / (max - min)  
     
    return df 

def replace_nan_with_row_avg(df):
    m = df.values.copy()
    #n = df.copy()
    print(m.shape)

    rows, cols = m.shape

    # row wise imputation
    for m in range(rows):
        row_sum = 0
        row_average = 0
        count_of_numbers = 0
        for n in range(cols):
            if not np.isnan(df.iloc[m,n]):
                count_of_numbers += 1
                row_sum+= df.iloc[m,n]
        row_average = row_sum / count_of_numbers
            
        for p in range(cols):
            if np.isnan(df.iloc[m, p]):
                df.iloc[m,p] = row_average
                
    return df


def build_user_ratings(df):
    rows, cols = df.shape
    users = df.columns
    user_ratings = {}
    for m in range(cols):
        ratings = []
        for g in range(rows):
            ratings.append(df.iloc[g,m])
        user_ratings[users[m]] = ratings
        
    return user_ratings 

def convert_to_unit_vector(ratings):
    for key, value in ratings.items():
        ratings[key] = unit_vector(value)
    
    return ratings    
           

def unit_vector(value):
    value = np.array(value)
    return value / np.sqrt(np.sum(value ** 2))
    
    
def similarity_matrix(user_ratings):
    similarity_matrix = {}
    # {
    #     'user1': {'user1': dot_product, 'user2':dot_product2},
    #     'user2': {'user2': dot_product, 'user1': dot_product}
    # }
    for key1, value1 in user_ratings.items():
        inner_dict = {}
        for key2, value2 in user_ratings.items():
            # value1, value2 are unit vectors, we can calculate dot product as:
            dot_product = np.sum(value1 * value2)
            inner_dict[key2] = dot_product
        similarity_matrix[key1] = inner_dict
        
    return similarity_matrix    
    
def build_user_similarity_matrix():
    process_data()    
        
if __name__ == "__main__":
    build_user_similarity_matrix()
                        