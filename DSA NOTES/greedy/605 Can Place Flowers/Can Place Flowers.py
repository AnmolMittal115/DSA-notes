class Solution:
    def canPlaceFlowers(self, nums: list[int], p: int) -> bool:
        if not p:
            return True

        n = len(nums)
        i = 0

        while i < n:
            if nums[i] == 0:
                left_empty = i == 0 or nums[i - 1] == 0
                right_empty = i == n - 1 or nums[i + 1] == 0

                if left_empty and right_empty:
                    nums[i] = 1
                    p -= 1
                    i += 1

                    if p == 0:
                        return True
            i += 1

        return p <= 0
