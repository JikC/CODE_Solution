from collections import deque


class Solution:
    def minimumJumps(self, forbidden, a, b, x):
        forbidden = set(forbidden)
        Q = deque()
        Q.append((0, 0, False))
        while Q:
            cur, cnt, used = Q.popleft()
            if cur == x:
                # 第一次到x即最小步数，因为队列后序元素cnt都是大于等于当前cnt的
                return cnt
            if cur + a < 6000 and cur + a not in forbidden:
                # 6000是往右探索的最大值，x最大为2000
                forbidden.add(cur + a)
                Q.append((cur + a, cnt + 1, False))
            if not used and cur - b > 0 and cur - b not in forbidden:
                # 这里不能forbidden，因为后退回cur-b处时，无法覆盖前进到cur-b再后退到cur-2b的情况。
                Q.append((cur - b, cnt + 1, True))
        return -1


obj = Solution()
print(obj.minimumJumps([1, 6, 2, 14, 5, 17, 4], 16, 9, 7))
