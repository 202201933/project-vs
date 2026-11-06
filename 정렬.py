def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

arr = [4,2,3,5,1]
sorted_arr = insertion_sort(arr)
print(sorted_arr)


def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

arr = [6,8,10,7,9]
sorted_arr = selection_sort(arr)
print(sorted_arr)


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

arr = [14,11,15,13,12]
sorted_arr = bubble_sort(arr)
print(sorted_arr)


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


def percolateDown(A, k, n): # A:배열/k:현재노드인덱스/n:힙크기
    child = 2 * k + 1
    right = 2 * k + 2

    if child <= n - 1: #힙의 유효범위 이내라면
        if right <= n - 1 and A[child] < A[right]: #오른쪽자식이 더 크면
            child = right #더 큰값으로 변경
        if A[k] < A[child]: #루트보다 크면
            A[k], A[child] =A[child], A[k] #위치변경
            percolateDown(A, child, n) #성질유지

def buildHeap(A, n):
    for i in range((n - 2) // 2, -1, -1):
        percolateDown(A, i, n)

def heapSort(A):
    n = len(A)
    buildHeap(A, n)

    for i in range(n - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        percolateDown(A, 0, i)
    return A

array = [4, 10, 3, 5, 1, 8]
sorted_array = heapSort(array)
print(sorted_array)

def merge(A, p, q, r):
    tmp = [0] * len(A)
    i = p
    j = q + 1
    t = 0

    while i<=q and j<=r:
        if A[i] <= A[j]:
            tmp[t] = A[i]
            t += 1
            i += 1
        else:
            tmp[t] = A[j]
            t += 1
            j += 1
    while i <= q:
        tmp[t] = A[i]
        t += 1
        j += 1
    i = p
    t = 0
    while i <= r:
        A[i] = tmp[t]
        i += 1
        t += 1

def mergeSort(A, p, r):
    if p < r:
        q = (p + r) // 2
        mergeSort(A, p , q)
        mergeSort(A, q+1, r)
        merge(A, p, q, r)

array = [5,15,10,23,1,10,7]
sorted_array = mergeSort(array, 0, len(array) - 1)
print(sorted_array)