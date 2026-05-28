class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0
        for t in tokens:
            if t not in ["+","-","*","/"]:
                stack.append(int(t))
            else:
                n1 = stack.pop()
                n2 = stack.pop()
                if t == "+":
                    res = n1 + n2
                elif t == "-":
                    res = n2 - n1
                elif t == "*":
                    res = n1 * n2
                else:
                    res = int(n2/n1)
                stack.append(res)
        return stack[-1]
