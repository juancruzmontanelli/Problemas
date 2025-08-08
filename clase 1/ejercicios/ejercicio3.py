# Find the First Occurrence of an Element in an Array

## Problem Description

def find_first_occurrence(arr, element):
    for i, value in enumerate(arr):
        if value == element: 
            return i 
    return -1

# Test Cases
def test_find_first_occurrence():
    test_cases = [
        (["apple", "banana", "cherry"], "banana", 1),
        (["dog", "cat", "dog", "bird"], "dog", 0),
        (["red", "blue", "green", "blue"], "blue", 1),
        (["one", "two", "three"], "four", -1),
        ([], "anything", -1),
        (["a", "b", "c"], "c", 2),
    ]
    
    for i, (input_array, element, expected) in enumerate(test_cases):
        result = find_first_occurrence(input_array, element)
        assert result == expected, f"FAILED on case {i + 1}: expected {expected}, but got {result}"
    print("All tests PASSED.")

# Run Tests
if __name__ == "__main__":
    test_find_first_occurrence()
