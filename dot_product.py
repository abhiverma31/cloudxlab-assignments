class Vector:
    def __init__(self, values):
        self.values = values
        
    def dot_product(self, vector):
        if len(self.values) != len(vector.values):
            raise Exception("Invalid inputs")
        
        sum = 0
        for i, item in enumerate(self.values):
            sum += item * vector.values[i]
        
        return sum   
 
v1 = Vector([1,2,3])
v2 = Vector([4,5,6])
print(v1.dot_product(v2))   