class Solution:
    def maxProfit(self, nums: list[int], fee: int) -> int:
        min_price = nums[0] + fee
        profit = 0

        for price in nums[1:]:

            if min_price > price + fee:
                min_price = price + fee

            elif price > min_price:
                profit += price - min_price
                min_price = price
        return profit
