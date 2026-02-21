import statistics

sorted_structure = []

# calculate distance when points in n dimension
def sq_distance_n_dim(p1, p2):
    sum = 0
    for i, item in enumerate(p1):
        sum += (item - p2[i]) ** 2
    return sum

def ingest_record(x_new): # x_new: ([1, 2, 3], 1000)
    # create a sorted collection 
    sorted_structure.append({'features': x_new[0], 'label': x_new[1]})
    #print(sorted_stucture)
    
    # sort by distances
    sorted_structure.sort(key=lambda x: sq_distance_n_dim(x['features'], x_new[0]))
    
    #sorted_stucture.sort(key = get_distance)
    

def query_knn(query, k):
    
    # I am ingesting the record we're computing KNN for just to 
    # reorder the collection w.r.t the record for which we're seeking KNN
    # This is not ideal as I'm adding every request to the global collection
    # but the benefit is I am able to relatively easily obtain the KNN for the point I'm querying
    ingest_record(query)
    
    # I am now deleting the query point as the objective has already been
    # achieved of re-ordering the collection w.r.t to the query point
    sorted_structure.pop(0)
    
    nearest_k = []
    for item in sorted_structure[:k]:
        nearest_k.append(item['label'])
        
    return statistics.mean(nearest_k)



# Testing
ingest_record(([1, 2, 4, 3], 1000))
ingest_record(([2, 4, 2, 4], 4000))
ingest_record(([3, 10, 3, 9], 45000))
ingest_record(([4, 10, 1, 9], 66000))

# ingest_record(([1, 2, 3, 4], 1000))
# ingest_record(([5, 2, 3, 6], 3000))
# ingest_record(([1, 5, 6, 2], 5000))
# ingest_record(([6, 7, 6, 2], 6000))
# ingest_record(([1, 6, 8, 2], 7000))
# ingest_record(([3, 5, 6, 2], 4000))
# ingest_record(([8, 3, 5, 2], 9000))
    

print(f"""Averge of the corresponding values for K nearest neightbours of the 
point we are querying is -> {query_knn(([2, 10, 6, 8],0), 2)}""")

print(f"Sorted structure -> {sorted_structure}")
