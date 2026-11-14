class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        n = len(s)
        hash = {}
        end = 0
        partition = []
        start = 0

        for i in range(n):
            hash[s[i]] = i

        for i in range(n):
            end = max(end, hash[s[i]])

            if i == end:
                partition.append(i - start + 1)
                end = 0
                start = i + 1
        return partition
