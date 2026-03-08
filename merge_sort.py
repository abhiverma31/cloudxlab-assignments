# merge two sorted lists
# space - o(n), time - o(n)
def merge_lists(list1, list2):
    i = 0
    j = 0
    merged_list = []
    while (i < len(list1) and j < len(list2)):
        if list1[i] > list2[j]:
            merged_list.append(list2[j])
            j+=1
        elif list1[i] < list2[j]:
            merged_list.append(list1[i])
            i+=1
        else:
            merged_list.append(list1[i])
            i+=1
            
     # we need to populate merged_array with the remaining elements of the
     # partially processed array        
    if i == len(list1):
        merged_list.extend(list2[j:])
    else:
        merged_list.extend(list1[i:])
    return merged_list    

# overall time complexity of merge sort - o(nlogn) and space complexity - o(n)
# why nlog(n) time complexity: log(n) levels and within each level n operations 
# are happening for the merge process which amounts to n * log(n) running time
def merge_sort(array):
    if len(array) == 1:
        return array
    else:
        mid = len(array) // 2
        left = merge_sort(array[:mid])
        right = merge_sort(array[mid:])
        return merge_lists(left, right)

if __name__ ==  "__main__":
    sorted_list = merge_sort([6, 5, 7, 10, 1, -1, 10, 11, -4, 13, -90])    
    print(sorted_list)