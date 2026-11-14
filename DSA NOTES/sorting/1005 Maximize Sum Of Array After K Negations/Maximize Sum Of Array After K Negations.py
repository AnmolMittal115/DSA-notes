def largestSumAfterKNegations(self, nums: list[int], k: int) -> int:
    nums.sort()
    n = len(nums)
    print(nums)
    i = 0

    while k:
      if i < n:
        if nums[i] < 0:
            nums[i] = - nums[i]
            k-=1
            if i < n-1:
                if abs(nums[i]) < nums[i+1]:
                    continue
                i+=1


        else:
                nums[i] *= (-1)**k
                break

    return sum(nums)
