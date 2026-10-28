class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        l = 0
        r = len(nums)-1
        maxi = 0

        while l<r:
            current_sum = nums[l] + nums[r]

            if current_sum > maxi:
                maxi = current_sum

            l+=1
            r-=1
        return maxi
