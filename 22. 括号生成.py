def generateParenthesis(n):
    """
    :type n: int
    :rtype: List[str]
    """
    ############################# 1
    # def dfs(S, left, right):
    #     if len(S) == 2 * n:
    #         res.append(''.join(S))
    #         return
    #     if left < n:
    #         S.append('(')
    #         dfs(S, left + 1, right)
    #         S.pop()
    #     if right < left:
    #         S.append(')')
    #         dfs(S, left, right + 1)
    #         S.pop()
    #
    # res = []
    # dfs([], 0, 0)
    # return res
    ############################# 2
    # if n == 0: return ['']
    # ans = []
    # for c in range(n):
    #     for left in generateParenthesis(c):
    #         for right in generateParenthesis(n - c - 1):
    #             # ans.append('({}){}'.format(left, right))
    #             ans.append('({}){}'.format(left, right))
    # return ans

    ############################# 3
    if n == 0: return ['']
    if n == 1: return ['()']
    res = set()
    for i in generateParenthesis(n - 1):
        for j in range(len(i)):
            res.add(i[0:j] + '()' + i[j:])
    return list(res)


print(generateParenthesis(3))
