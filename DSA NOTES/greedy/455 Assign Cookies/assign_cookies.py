class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()
        i=j=0

        leng = len(g)
        lens = len(s)

        while i < leng and j < lens:
            if s[j] >= g[i]:
                i += 1
            j += 1
        return i
