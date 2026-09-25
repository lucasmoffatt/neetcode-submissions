class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {'(': ')', '{': '}', '[': ']'}

        for c in s:
            if c in brackets:
                stack.append(c)
            elif stack and brackets[stack[-1]] == c:
                stack.pop()
            else:
                return False
        
        return len(stack) == 0
