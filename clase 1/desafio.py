# Anagram Checker
def sort_string_array(arr) : 
    n = len(arr)
    for i in range(n) : 
        for j in range(n-1): 
            if arr[j] > arr[j+1]: 
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
def are_anagram(word1, word2):
    word1 = word1.lower()
    word2 = word2.lower()
    word1 = list(word1)
    word2 = list(word2)
    word1 = sort_string_array(word1)
    word2 = sort_string_array(word2)
    if word1 == word2: 
        return True 
    else: 
        return False
    

    pass

# Test Cases
def test_are_anagram():
    test_cases = [
        ("roma", "amor", True),
        ("python", "typhon", True),
        ("hola", "halo", True),
        ("listen", "silent", True),
        ("rat", "tar", True),
        ("hello", "world", False),
        ("night", "thing", True),
        ("abc", "def", False),
        ("aabbcc", "abcabc", True),
        ("", "", True),  # Two empty strings are anagrams
        ("a", "a", True),
        ("a", "b", False),
        ("abcd", "abc", False),  # Different lengths
    ]
    
    for i, (word1, word2, expected) in enumerate(test_cases):
        result = are_anagram(word1, word2)
        assert result == expected, f"FAILED on case {i + 1}: expected {expected}, but got {result}"
    print("All tests PASSED.")

# Run Tests
if __name__ == "__main__":
    test_are_anagram()
