import statistics

# calculate distance when points in n dimension
def sq_distance_n_dim(p1, p2):
    sum = 0
    for i, item in enumerate(p1):
        sum += (item - p2[i]) ** 2
    return sum 

def find_k_closest_n_d(x_new, X, y, k, distance=sq_distance_n_dim):
    distances = []
    for i, X_pair in enumerate(X):
        # maintain a collection for all distances of x_new with elements of X
        separation = distance(x_new, X_pair)
        distances.append({'separation': separation, 'associated_index': i})
        
    # sort distances by 'separation' and take the top K from collection 'y'        
    distances.sort(key=lambda d: d['separation'])
    print(distances)
    nearest_k_entiries = distances[:k]
    nearest_k_y_vals = []
    for item in nearest_k_entiries:
        nearest_k_y_vals.append(y[item['associated_index']])
        
    # return average of values from y    
    return statistics.mean(nearest_k_y_vals)


# test
X = [[1,2,4,3],[2,4,2,4],[3,10,3,9],[4,10,1,9]]
y = [1000, 4000, 45000, 66000]
closest_n_neighbours = find_k_closest_n_d([2, 10, 6, 8], X, y, 2, sq_distance_n_dim)
print(closest_n_neighbours)