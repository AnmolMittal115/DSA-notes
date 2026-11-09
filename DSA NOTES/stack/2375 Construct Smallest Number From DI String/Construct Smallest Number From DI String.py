class Solution:
    def smallestNumber(self, pattern: str) -> str:
        stack = []
        ans = []
        n = len(pattern) + 1

        for i in range(n):
            if i == n-1 or pattern[i] == 'I':
                stack.append(str(i+1))
                while stack:
                    ans.append(stack.pop())
            else:
                stack.append(str(i+1))
        return "".join(ans)
