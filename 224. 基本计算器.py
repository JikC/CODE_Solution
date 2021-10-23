class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        ops = [1]
        sign = 1
        res = 0
        n = len(s)
        i = 0
        while i < n:
            if s[i] == ' ':
                i += 1
            elif s[i] == '+' or s[i] == '-':
                sign = ops[-1] if s[i] == '+' else -ops[-1]
                i += 1
            elif s[i] == '(':
                ops.append(sign)
                i += 1
            elif s[i] == ')':
                ops.pop()
                i += 1
            else:
                num = 0
                while i < n and s[i].isdigit():
                    num = num * 10 + (ord(s[i]) - ord('0'))
                    i += 1
                res += num * sign
        return res


obj = Solution()
print(obj.calculate("1+2+(3-(4+5))"))
