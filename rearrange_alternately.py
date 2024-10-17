def rearrange_alternately(arr):
    """
    Rearrange a sorted array in an alternating order of largest and smallest elements.

    Parameters:
    arr (list): A sorted list of integers.

    Returns:
    list: A list rearranged in alternate high-low order.
    """
    n = len(arr)
    result = [0] * n  # Resultant array to hold the rearranged elements

    # Pointers for largest and smallest elements
    left, right = 0, n - 1

    # Fill the result array alternately with largest and smallest
    for i in range(n):
        if i % 2 == 0:
            result[i] = arr[right]
            right -= 1
        else:
            result[i] = arr[left]
            left += 1

    return result

# Example usage:
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    print("Original Array:", arr)
    print("Rearranged Array:", rearrange_alternately(arr))
