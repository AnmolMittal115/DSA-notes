class Solution:
    def minPartitions(self, n: str) -> int:
        maxi = 0

        for ch in n:
            maxi = max(maxi, int(ch))

        return maxi
