class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        res = tmp = 0
        for j in range(len(s)):
            i = dic.get(s[j], -1)
            dic[s[j]] = j
            tmp = tmp + 1 if tmp < j - i else j - 1
            res = max(res, tmp)
        return res


obj = Solution()
print(obj.lengthOfLongestSubstring('abcaddf'))
