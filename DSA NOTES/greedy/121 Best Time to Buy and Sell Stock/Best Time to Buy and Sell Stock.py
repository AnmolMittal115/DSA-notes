class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        min_price = nums[0]
        max_profit = 0

        for num in nums:
            if num < min_price:
                min_price = num
            profit = num - min_price
            if max_profit < profit:
                max_profit = profit

        return max_profit
