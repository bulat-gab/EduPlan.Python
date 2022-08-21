# You have 2 sorted list. arr_1=[1, 4, 6, 7, 8, 9] arr_2=[6, 9]
# Find an intersection and evaluate O complexity.

"""
You have 2 sorted list. arr_1=[1, 4, 6, 7, 8, 9] arr_2=[6, 9, 10]
Find an intersection and evaluate O complexity.
"""


def get_intersection(arr1: list[int], arr2: list[int]) -> list[int]:
    # return list(set(arr1) & set(arr2)) # O(min(n, m))
    i = 0
    j = 0

    result = []
    while True:
        if i >= len(arr1) or j >= len(arr2):
            break

        if arr1[i] < arr2[j]:
            i += 1
        elif arr1[i] > arr2[j]:
            j += 1
        else:
            result.append(arr1[i])
            i += 1
            j += 1

    return result

if __name__ == "__main__":
    arr_1 = [1, 4, 6, 7, 8, 9]
    arr_2 = [6, 9, 10]

    # assert get_intersection(arr_1, arr_2) == [6, 9]
    print(get_intersection(arr_1, arr_2))
