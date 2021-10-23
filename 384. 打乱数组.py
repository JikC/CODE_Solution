import random


class Solution:

    def __init__(self, nums):
        self.array = nums
        self.original = list(nums)

    def reset(self):
        self.array = self.original
        self.original = list(self.original)
        return self.array

    def shuffle(self):
        ##### 1.
        # aux = list(self.array)
        # for idx in range(len(self.array)):
        #     removeidx = random.randrange(len(aux))
        #     self.array = aux.pop(removeidx)
        ##### 2.
        for i in range(len(self.array)):
            swapidx = random.randrange(i, len(self.array))
            self.array[i], self.array[swapidx] = self.array[swapidx], self.array[i]
        return self.array




# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
