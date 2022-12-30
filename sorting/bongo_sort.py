import random

to_sort = [5,1,12]

def bogo_sort(arr):
    def is_sorted(arr):
        for i in range(0,len(arr)-1):
            if arr[i] > arr[i+1]:
                return False
        return True

    while not is_sorted(arr):
        random.shuffle(arr)
    return arr

print(bogo_sort(to_sort))
