# 给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。
# 输入：s = "ADOBECODEBANC", t = "ABC"
# 输出："BANC"
import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = collections.defaultdict(int)
        for c in t: need[c] += 1
        needCount = len(t)
        i = 0
        res = [0, float("inf")]
        for j, c in enumerate(s):
            if need[c] > 0: needCount -= 1
            need[c] -= 1
            if needCount == 0:
                while True:
                    if need[s[i]] == 0: break
                    need[s[i]] += 1
                    i += 1
                if j - i < res[1] - res[0]:
                    res = (i, j)
                need[s[i]] += 1
                needCount += 1
                i += 1
        return '' if res[1] > len(s) else s[res[0]:res[1]+1]


obj = Solution()
print(obj.minWindow("DADOBECODEBANC", "ABC"))
