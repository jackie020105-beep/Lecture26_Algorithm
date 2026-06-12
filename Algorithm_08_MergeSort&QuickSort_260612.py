# 병합 정렬 (Merge Sort) ==========================================================
def merge_sort(A, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort (A, left, mid)
        merge_sort (A, mid+1, right)
        merge(A, left, mid, right)

# 병합 정렬 (Merge Sort) : merge
sorted_A = [0] * 100
def merge(A, left, mid, right):
    k = i = left
    j = mid + 1
    while i <= mid and j <= right:
        if A[i] <= A[j]:
            sorted_A[k] = A[i]
            k, i = k+1, i+1
        else:
            sorted_A[k] = A[j]
            k, j = k+1, j+1

    if i > mid:
        sorted_A[k:k+right-j+1] = A[j:right+1]
    else:
        sorted_A[k:k+mid-i+1] = A[i:mid+1]
    A[left:right+1] = sorted_A[left:right+1]


# 퀵 정렬(Quick Sort) ==========================================================
def quick_sort(A, left, right):
    if left < right:
        p = partition(A, left, right)
        quick_sort(A, left, p-1)
        quick_sort(A, p+1, right)

# 퀵 정렬(Quick Sort) : Partition
def partition(A, left, right):
    pivot = A[left]
    low = left + 1
    high = right

    while low <= high:
        while low <= right and A[low] < pivot: 
            low += 1
        while high >= left + 1 and A[high] > pivot: 
            high -= 1
        if low < high:
            A[low], A[high] = A[high], A[low]
    A[left], A[high] = A[high], A[left]
    return high


# 파이썬 정렬 함수 : key 매개변수 ==========================================================

# 내장 함수 활용
words = ["apple", "kiwi", "banana", "cherry"]
sorted(words, key =len)
sorted(words, key =str.lower)
# ambda 함수 (익명 함수) 활용
users = [("Alice",30),("Bob",20),("Charlie",25)]
users.sort(key=lambda x: x[1])

# ======================================== 

if __name__ == "__main__":
    # 병합 정렬 (Merge Sort) : merge ==================
    arr1 = [38, 27, 43, 3, 9, 82, 10]
    print("정렬 전:", arr1)
    merge_sort(arr1, 0, len(arr1) - 1)
    print("정렬 후:", arr1)

    # 퀵 정렬(Quick Sort) ==================
    arr2 = [50, 23, 9, 18, 61, 32]
    print("정렬 전:", arr2)
    quick_sort(arr2, 0, len(arr2) - 1)
    print("정렬 후:", arr2)

    # sorted() key 테스트 ==================
    
    # 길이 기준 정렬
    result1 = sorted(words, key=len)
    print("길이 기준 정렬:", result1)

    # 알파벳 소문자 기준 정렬
    result2 = sorted(words, key=str.lower)
    print("소문자 기준 정렬:", result2)

    # lambda key 테스트 ==================
    users = [("Alice", 30), ("Bob", 20), ("Charlie", 25)]
    print("정렬 전:", users)
    # 나이 기준 정렬
    users.sort(key=lambda x: x[1])
    print("정렬 후:", users)


