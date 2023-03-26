#video https://youtu.be/qIbuVhwRNpg

listtest = [2,6,4,12,89,3,69]

def Insertion_Sort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i -1
        while j >=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -=1
        arr[j+1] = key
    return arr

print(Insertion_Sort(listtest))