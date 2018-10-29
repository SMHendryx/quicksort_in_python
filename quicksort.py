# Ported from Cracking the Coding Interview book by Gayle Laakman McDowell

from typing import List


def quicksort(A: List[float], left: int, right: int) -> None:
    """
    Sorts array A by making all values less than  are  recursively partitioning subarrays of A.
    """
    index = partition(A, left, right)
    if (left < index - 1): # Sort left half:
        quicksort(A, left, index - 1)
    if (index < right): # sort right half
        quicksort(A, index, right)

def partition(A: List[float], left: int, right: int) -> int:
    """
    Swaps values such that all values on the left are less than or equal to the returned index and all values on the right are greater than the returned index.
    :param A: list/array to partition
    :param left: left index of the subarray to partition.
    :param right: right index of the subarray to partition.
    :return: integer index splitting the partitioned array
    """
    # Choose pivot value:
    pivot = A[int((left + right) / 2)]
    while left <= right:
        # Find elements to swap:
        while A[left] < pivot:
            left += 1
        while A[right] > pivot:
            right -= 1

        # Swap elements. Move left and right indices:
        if left <= right:
            tmp = A[left]
            A[left] = A[right]
            A[right] = tmp
            left += 1
            right -= 1
    return left

def gen_n_rand_ints(n:int=100, low:int=0, high:int=1000):
    # wrapper to yeild random.randint
    import random
    for _ in range(n):
        yield random.randint(low, high)


def main():

    #A = [1,2,3,4,5,6]
    #quicksort(A, 0, len(A)-1)
    #A

    #A = [7,2,3,4,5,6]
    #quicksort(A, 0, len(A)-1)
    #A

    gen = gen_n_rand_ints()
    A = [g for g in gen]
    print('List before quicksort:')
    print(A)
    quicksort(A, 0, len(A)-1)
    print('List after quicksort:')
    print(A)


if __name__ == '__main__':
    main()