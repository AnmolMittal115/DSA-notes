class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []

        for i in range(0, n, 3):

            first = nums[i]
            second = nums[i+1]
            third = nums[i+2]

            if third - first > k:
                return []

            ans.append( [ first, second, third ] )
        return ans
