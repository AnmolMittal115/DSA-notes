class Solution:
    def partitionString(self, s: str) -> int:
        sett = set()
        count = 1

        for ch in s:
            if ch in sett:
                count+=1
                sett.clear()

            sett.add(ch)
        return count
