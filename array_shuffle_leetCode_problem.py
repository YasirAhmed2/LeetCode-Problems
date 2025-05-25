import random

class Solution:

    def __init__(self, nums):
        self.original = nums[:]
        self.current = nums[:]

    def reset(self):
        self.current = self.original[:]
        return self.current

    def shuffle(self):
        # Fisher-Yates shuffle algorithm
        n = len(self.current)
        for i in range(n - 1, 0, -1):
            j = random.randint(0, i)
            self.current[i], self.current[j] = self.current[j], self.current[i]
        return self.current