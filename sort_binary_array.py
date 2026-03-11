from merge_sort import merge_sort

# problem: sort a binary array containing only [0..'s, 1..'s]

# approach 1
#  just use the merge_sort recently implemented
#  o(nlogn) running time, o(n) space

def sort_array_1(array):
    return merge_sort(array)
    
sorted_array = sort_array_1([1,0,1,0,1,0,0,0,0,0,1,1,1,1])
print(f"sorted_list using approach 1 ->  {sorted_array}")

#################################################

# approach 2
#  filter out the 0's from original list and put them in a separate result array
#  find how many 1's need to follow the 0's in the result array -> len(original_array) - len(result_array)
#  just append those many 1's to result array
#  o(n) running time [2 linear iterations, while filtering for 0's and while adding the 1's], o(n) space [extra space for the result_array]

def sort_array_2(array):
    result_array = list(filter(lambda x: x == 0, array)) # with this step result_array contain's all 0's of original list
    count_of_ones_required = len(array) - len(result_array)
    result_array.extend(1 for _ in range(count_of_ones_required))
    return result_array

sorted_array = sort_array_1([1,0,1,0,1,0,0,0,0,0,1,1,1,1])
print(f"sorted_list using approach 2 ->  {sorted_array}")


#################################################

# approach 3
#  using in-place swap on the original array, this does not incur space complexity
#  the idea is to maintain a pointer 'k' on the oldest occurance of position 1
#  when we encounter a 0, we swap array[current_position] with array[k] and move k by 1 (the aim being to point 'k' to earliest occurance in the array)
#  time complexity - o(n), space - o(1)

def sort_array_3(array):
    seen_one = False
    k = 0
    for i, item in enumerate(array):
       if array[i] == 1 and not seen_one : # lock pointer at earliest occurance of 1
          k = i
          seen_one = True          
       elif array[i] == 0:
          # swap arr[k], arr[i]
          temp = array[k]
          array[k] = array[i]
          array[i] = temp
          k = k + 1 # 'k' will always have to point to the earliest occrance 1
    return array      
    
sorted_array = sort_array_3([1,0,1,0,1,0,0,0,0,0,1,1,1,1])
print(f"sorted_list using approach 3 ->  {sorted_array}")
   
   
#################################################

# approach 4
#  again using in-place swap on the original array
#  two pointers: one to the leftmost position and other on the rightmost
#  if array[left] -> 0 advance left and if array[right] -> 1, decrement right
#  if array[left] -> 1 and array[right] -> 0, swap and left+, right-
#  time complexity - o(n), space - o(1)   

def sort_array_4(array):
    i = 0
    j = len(array) - 1
    while i <= j:
        if array[i] == 0:
            i+=1
        elif array[j] == 1:
            j-=1
        elif array[i] == 1 and array[j] == 0:
            # swap
            temp = array[i]
            array[i] = array[j]
            array[j] = temp
            i+=1
            j-=1
    return array 

sorted_array = sort_array_4([1,0,1,0,1,0,0,0,0,0,1,1,1,1])
print(f"sorted_list using approach 4 ->  {sorted_array}")