class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        nums.sort(reverse = True)
        n = len(nums)
        total = 0

        for i in range(1,n-n//3,2):
            total += nums[i]
        return total
