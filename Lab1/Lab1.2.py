import random


def get_next_gap(gap):
    gap = (gap * 10) // 13
    if gap < 1:
        return 1
    return gap


def comb_sort(arr):
    n = len(arr)
    gap = n
    count_of_swaps = 0
    count_of_comparisons = 0
    swapped = True
    while gap > 1 or swapped:
        gap = get_next_gap(gap)
        swapped = False
        for i in range(0, n - gap):
            count_of_comparisons += 1
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                count_of_swaps += 1
                swapped = True
    print("Length of list: ", n)
    print("Count of swaps: ", count_of_swaps)
    print("Count of comparisons: ", count_of_comparisons)


A = list(range(50000))
random.shuffle(A)
# print(A)
comb_sort(A)
# print(A)
