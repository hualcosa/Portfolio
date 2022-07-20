class Solution:
    def isValid(self, s: str) -> bool:
        # stack to keep track of opening brackets
        stack = []
        
        # hash map for keeping track of mappings
        mapping = {')':'(', '}':'{', ']':'['}
        
        for char in s:
            # if the character is a closing bracket
            if char in mapping:
                # assign a dummy variable to top_element in case the stack is empty
                top_element = stack.pop() if stack else '#'
                
                if mapping[char] != top_element:
                    return False
            else: # add it to the stack
                stack.append(char)
            
        # if the stack is empty, return true, else return false
        return not stack