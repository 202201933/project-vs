def quick_sort(arr):
    if len(arr) <= 1: #배열길이가 0또는1이면 종료
        return arr
    pivot = arr[len(arr)//2] #중간값
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

arr = [4, 7, 3, 5, 1, 2, 4]
print("정렬 전:", arr)
print("정렬 후:", quick_sort(arr))
