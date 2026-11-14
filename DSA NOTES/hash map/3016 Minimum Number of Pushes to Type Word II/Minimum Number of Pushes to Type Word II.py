from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        counts = sorted(Counter(word).values(), reverse = True)
        level = 1
        min_push = 0
        available = 8

        for count in counts:
            min_push+=level*count
            available-=1
            if available == 0:
                level+=1
                available = 8
        return min_push
