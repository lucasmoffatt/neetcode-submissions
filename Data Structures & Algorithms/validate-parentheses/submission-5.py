class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map = {')':'(', '}': '{', ']':'['}

        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            else:
                if stack and map[c] == stack.pop():
                    continue
                else:
                    return False
        if not stack:
            return True
        else:
            return False

