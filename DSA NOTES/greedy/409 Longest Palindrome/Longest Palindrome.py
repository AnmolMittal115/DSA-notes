class Solution:
    def longestPalindrome(self, s: str) -> int:
        hash = {}
        longest = 0
        odd_found = False

        for ch in s:
            hash[ch] = hash.get(ch, 0) + 1

        for value in hash.values():
            puhh = value%2
            longest += value - (puhh)
            if puhh:
                odd_found = True

        return longest + odd_found
