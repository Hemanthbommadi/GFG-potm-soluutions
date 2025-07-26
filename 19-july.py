import math
from collections import Counter

class Solution:
    def vowelCount(self, s: str) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        vowel_counts = Counter()
        for char in s:
            if char in vowels:
                vowel_counts[char] += 1
                
        num_distinct_vowels = len(vowel_counts)

        if num_distinct_vowels == 0:
            return 0

        product_of_counts = 1
        for count in vowel_counts.values():
            product_of_counts *= count
            
        permutations_factor = math.factorial(num_distinct_vowels)
        
        total_distinct_strings = product_of_counts * permutations_factor
        
        return total_distinct_strings