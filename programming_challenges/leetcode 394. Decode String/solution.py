class Solution:
    def decodeString(self, s: str) -> str:
        # initialize the stack
        stack = []
        # iterate through each character
        for i in range(len(s)):
            # if char is different from "]" append it to the stack
            if s[i] != "]":
                stack.append(s[i])
            else:
                # pop the substring from the stack
                substr = ""
                while stack[-1] != "[":
                    substr = stack.pop() + substr
                stack.pop()
                # pop the digit(s) from the stack
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                # decode the substring and put it back on the stack
                stack.append(int(k) * substr)
    
        return "".join(stack)