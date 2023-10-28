def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

def count_smaller_elements(first_array, second_array):
    result = []
    for num in second_array:
        count = binary_search(first_array, num)
        result.append(count)
    return result

# Read input
n, m = map(int, input().split())
first_array = list(map(int, input().split()))
second_array = list(map(int, input().split()))

# Count smaller elements
output = count_smaller_elements(first_array, second_array)

# Print the result
print(' '.join(map(str, output)))
