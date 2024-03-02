datatosort = [3, 6, 8, 10, 1, 2, 1,42,2,15,57]

def quick_sort(arr):
    if len(arr) <2:
        return arr
    else:
        pivot = arr[0]
        less = []
        greater = []
        for i in arr[1:]:
            if i <= pivot:
                less.append(i)
            else:
                greater.append(i)
        return quick_sort(less) + [pivot] + quick_sort(greater)
    
print(quick_sort(datatosort))