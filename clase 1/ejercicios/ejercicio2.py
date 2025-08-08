# Find All Occurrences of an Element in an Array

def find_all_occurrences(arr, element):
    n = len(arr) 
    positions = []
    for i in range(n) : 
        if arr[i] == element :
            positions.append(i)
    return positions


# Test Cases
def test_find_all_occurrences():
    test_cases = [
        (["apple", "banana", "apple", "cherry"], "apple", [0, 2]),
        (["dog", "cat", "dog", "bird"], "dog", [0, 2]),
        (["red", "blue", "green", "red", "blue"], "blue", [1, 4]),
        (["one", "two", "three"], "four", []),
        ([], "anything", []),
        (["a", "b", "a", "c", "a"], "a", [0, 2, 4]),
    ]
    
    for i, (input_array, element, expected) in enumerate(test_cases):
        result = find_all_occurrences(input_array, element)
        assert result == expected, f"FAILED on case {i + 1}: expected {expected}, but got {result}"
    print("All tests PASSED.")

# Run Tests
if __name__ == "__main__":
    test_find_all_occurrences()
