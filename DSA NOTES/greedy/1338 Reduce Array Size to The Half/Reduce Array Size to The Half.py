from collections import Counter

class Solution:
    def minSetSize(self, nums: list[int]) -> int:
        Count = sorted(Counter(nums).values(), reverse = True)
        n = len(nums)//2


        for i in range(len(Count)):

            n -= Count[i]
            if n <=0:
                return i + 1
