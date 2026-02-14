import statistics


def sq_distance(p1, p2):
    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1]
    return (x1 - x2) ** 2 + (y1 - y2) ** 2

def find_closest_2d(x_new, X, y, distance=sq_distance):
    # x_new -> [2,5]
    minimum = None
    min_index = None
    for i, X_pair in enumerate(X):
        # find the difference of X_pair and X[i]
        distance = sq_distance(x_new, X_pair)
        
        if minimum == None or distance < minimum:
            minimum = distance
            min_index = i
            
    return y[min_index]  

def find_k_closest_2d(x_new, X, y, k=2, distance=sq_distance):
    distances = []
    for i, X_pair in enumerate(X):
        # maintain a collection for all distances of x_new with elements of X
        separation = distance(x_new, X_pair)
        distances.append({'separation': separation, 'associated_index': i})
        
    # sort distances by 'separation'
    # distances.sort(key=lambda d: d['separation'])
    # take the top 2 from collection 'y'        
    distances.sort(key=lambda d: d['separation'])
    closest_k = distances[:k]
    print(closest_k)
    closest_k_y = []
    for item in closest_k:
        closest_k_y.append(y[item['associated_index']])
    return statistics.mean(closest_k_y)


X = [[1,2,4,3],[2,4,2,4],[3,10,3,9],[4,10,1,9]]
y = [1000, 4000, 45000, 86000]
closest_neighbour = find_closest_2d([2, 10], X, y)
print(closest_neighbour)

closest_2_neighbours = find_k_closest_2d([2, 10], X, y)
print(closest_2_neighbours)
