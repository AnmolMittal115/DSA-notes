class Solution:
    def groupThePeople(self, nums: list[int]) -> list[list[int]]:
        ans = []
        n = len(nums)
        hash = {}

        for i in range(n):

            if nums[i] not in hash:
                hash[nums[i]] = hash.get(nums[i], [])
            hash[nums[i]].append(i)
            if len(hash[nums[i]]) == nums[i]:
                ans.append(hash[nums[i]])
                hash[nums[i]] = []
        return ans
