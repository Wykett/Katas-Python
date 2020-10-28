def find_even_index(arr):
    for pivot in range(len(arr)):
        left_total = sum(arr[:pivot])
        right_total = sum(arr[pivot+1:])
        print (left_total)
        print (right_total)
        if left_total == right_total:
            return pivot
    return -1 