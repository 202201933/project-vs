def quick_sort(arr):
    if len(arr) <= 1: #배열길이가 0또는1이면 종료
        return arr
    pivot = arr[len(arr)//2] #중간값
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

arr = [5, 3, 8, 4, 9, 1, 6, 2, 7]
print("정렬 전:", arr)
print("정렬 후:", quick_sort(arr))
