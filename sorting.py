def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# User input for array elements
arr = list(map(int, input("Enter array elements separated by space: ").split()))
print("Sorted array:", bubble_sort(arr))
