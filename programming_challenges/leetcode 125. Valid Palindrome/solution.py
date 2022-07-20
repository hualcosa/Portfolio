class Solution:
    def isPalindrome(self, s: str) -> bool:
        lowercase_filtered_chars = [ch.lower() for ch in s if ch.isalnum()]
        reversed_chars_list = lowercase_filtered_chars[::-1]
        
        return lowercase_filtered_chars == reversed_chars_list
        