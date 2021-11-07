# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
# 注意：若 s 和 t 中每个字符出现的次数都相同，则称 s 和 t 互为字母异位词。
# 示例 1:
# 输入: s = "anagram", t = "nagaram"
# 输出: true
# 示例 2:
# 输入: s = "rat", t = "car"
# 输出: false
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        record = [0] * 26
        for i in range(len(s)): record[ord(s[i]) - ord("a")] += 1
        for i in range(len(t)): record[ord(t[i]) - ord("a")] -= 1
        for i in record:
            if i != 0: return False
        return True


obj = Solution()
print(obj.isAnagram("anagram", "nagaram"))
print(obj.isAnagram("rat", "car"))