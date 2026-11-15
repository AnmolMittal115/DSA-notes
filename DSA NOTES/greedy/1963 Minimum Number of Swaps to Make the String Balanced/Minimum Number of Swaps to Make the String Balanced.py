class Solution:
    def minSwaps(self, s: str) -> int:
        depth = 0
        maxi = 0

        for ch in s:

            if ch == '[':
                depth+=1
            else:
                depth-=1
            maxi = max(maxi, -depth)

        return (maxi+1)//2