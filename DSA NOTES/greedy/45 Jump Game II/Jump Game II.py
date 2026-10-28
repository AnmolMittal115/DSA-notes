class Solution:
    def jump(self, nums: list[int]) -> int:
        mini_jumps = 0
        farthest = 0
        current_reach = 0
        n = len(nums)

        for i in range(n):

            if i > current_reach:
                mini_jumps+=1
                current_reach = farthest

            farthest = max( farthest, i + nums[i] )

            if current_reach>= n-1:
                return mini_jumps
        return mini_jumps
