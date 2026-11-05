class Solution:
    def maxProfit(self, nums: list[int]) -> int:
        n = len(nums)
        total_profit = 0

        for i in range(1,n):
            buy = nums[i-1]
            sell = nums[i]

            if sell > buy:
                total_profit += sell - buy
        return total_profit
