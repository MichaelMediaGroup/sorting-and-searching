#video = https://youtu.be/SYn8j6873mE

name = ['app'," banana", "car" ,"dog", "egg" ,"michael"]

def binary_search(arr,key):
    start = 0
    end = len(arr) -1
    while start <= end:
        mid = (start + end) //2
        if arr[mid] == key:
            return mid
        if arr[mid] > key:
            end = mid -1
        else:
            start = mid +1
    return -1

print(binary_search(name,"egg"))