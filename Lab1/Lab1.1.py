import random


def bubble_sort(arr):
    n = len(arr)
    count_of_swaps = 0
    count_of_comparisons = 0
    for i in range(n - 1):
        swapped = False
        for j in range(0, n - i - 1):
            count_of_comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                count_of_swaps += 1
                swapped = True
        if not swapped:
            break
    print("Length of list: ", n)
    print("Count of swaps: ", count_of_swaps)
    print("Count of comparisons: ", count_of_comparisons)


A = list(range(10000))
# random.shuffle(A)
# print(A)
bubble_sort(A)
# print(A)
