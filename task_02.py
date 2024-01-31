def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    iterations = 0

    while low <= high:
        mid = (low + high) // 2
        iterations += 1

        if arr[mid] == target:
            return iterations, arr[mid]
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    # If the element is not found, return the "upper bound" (the smallest element greater than or equal to the target)
    if high >= 0 and high < len(arr):
        return iterations, arr[high]
    else:
        return iterations, None


# Function for demonstration
def demonstrate_binary_search(sorted_array, target_value):
    result = binary_search(sorted_array, target_value)
    iterations, upper_bound = result

    if upper_bound is not None:
        print(
            f"Element {target_value} found in {iterations} iterations. Upper bound: {upper_bound}"
        )
    else:
        print(f"Element {target_value} not found in the sorted array.")


# Example 1:
sorted_array_1 = [0.1, 0.5, 1.2, 2.0, 3.5, 5.0, 8.1, 13.2]
target_value_1 = 3.0
demonstrate_binary_search(sorted_array_1, target_value_1)

# Example 2:
sorted_array_2 = [-2.3, -1.5, 0.0, 1.8, 4.2, 6.7, 9.2, 11.1]
target_value_2 = 0.5
demonstrate_binary_search(sorted_array_2, target_value_2)

# Example 3:
sorted_array_3 = [1.1, 2.2, 3.3, 4.4, 5.5]
target_value_3 = 2.5
demonstrate_binary_search(sorted_array_3, target_value_3)
