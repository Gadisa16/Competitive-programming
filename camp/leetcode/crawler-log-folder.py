class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack= []
        for val in logs:
            if val=="./":
                continue
            if val =="../":
                if stack:
                    stack.pop()
            
            else:
                stack.append(val)
        return len(stack)