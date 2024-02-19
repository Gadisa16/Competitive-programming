class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack= []

        for val in tokens:
            if val not in "+-*/":
                stack.append(int(val))

            else:
                vr, vl= stack.pop(), stack.pop()
                if val== "+":
                    stack.append(vl + vr)
                elif val== "*":
                    stack.append(vl * vr)
                elif val== "-":
                    stack.append(vl - vr)
                else:
                    stack.append(int(vl/vr))

        return stack[0] 


        