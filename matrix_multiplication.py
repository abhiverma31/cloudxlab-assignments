m1=[
      [0,4,7,9], 
      [4,3,2,1],
      [6,3,2,1]
   ] # 3 * 4
m2=[
      [0,1,2,3], 
      [4,3,2,1],
      [6,3,2,1],
      [5,6,7,8]
   ] # 4 * 4

# For testing Vector rotation using mat_mult
# import math
# m1 = [
#         [1,1]
#      ]

# m2 = [
#         [math.cos(math.radians(30)), math.sin(math.radians(30))],
#         [- math.sin(math.radians(30)), math.cos(math.radians(30))]
#      ]

resultant_matrix = []

def mat_mult(m1, m2):
    
    columns_m1 = len(m1[0]) # 4
    columns_m2 = len(m2[0]) # 4
    rows_m1 = len(m1) # 3
    rows_m2 = len(m2) # 4
    
    if columns_m1 != rows_m2:
        raise Exception("Invalid inputs")
      
    for i, item in enumerate(m1): # item -> [0, 4, 7, 9]
        k = 0
        sum = 0
        inner_array = [] # re-initialize
        
        while (k < len(m2)): # for item[] in m1, fill up the inner_array
            # we'd require to do this computation to find value of cells of the resultant matrix
                # resultant_matrix[0][0] = m1[0][0] * m2[0][0] + m1[0][1] * m2[1][0] + m1[0][2] * m2[2][0] + m1[0][3] * m2[3][0]
            for j, item_ in enumerate(item): # j -> 0, 4, 7, 9
                sum += item_ * m2[j][k]
            inner_array.append(sum)    
            #print(sum)
            # reset for preparing them for calculating next element of inner_array       
            sum = 0    
            j = 0
            k+=1
            
        resultant_matrix.append(inner_array)            
        print()
    
    print("Result of matrix mulitiplication:")    
    print_resultant_matrix()
    
    
# print resultant_matrix in form of a matric
def print_resultant_matrix():
    for m, item in enumerate(resultant_matrix): # [103, 87, 85, 83]
        for n, item_ in enumerate(resultant_matrix[m]): 
            print(resultant_matrix[m][n], end="\t") 
        print()
        
mat_mult(m1, m2)          