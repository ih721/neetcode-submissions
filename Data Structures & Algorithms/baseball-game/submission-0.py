class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []
        for op in operations:
            if op == 'C':
                res.pop()
            elif op == 'D':
                d = res[-1] * 2
                res.append(d)
            elif op == '+':
                sum1 = res[-2] + res[-1]
                res.append(sum1)
            else:
                res.append(int(op))
        return sum(res)
        
            


