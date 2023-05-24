
def selection_sort(arr):
    """
    Sorts an array using selection sort algorithm.

    :param arr: Array to be sorted.
    :return: Sorted array.
    """
    n = len(arr)

    for i in range(n):
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

        # Print intermediate steps of sorting process
        print(f"Step {i+1}: {arr}")

    return arr

# Get array from user
arr = input("Enter comma-separated values to sort: ").split(',')
arr = [int(x.strip()) for x in arr]

# Sort array using selection sort and print intermediate steps
print("Original array:", arr)
sorted_arr = selection_sort(arr)
print("Sorted array:",sorted_arr)
