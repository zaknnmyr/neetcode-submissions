# size of window - most frequent character = numReplacement <= k

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        maxSubstring = 0
        l = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r],0)
            while r - l + 1 - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            maxSubstring = max(r-l+1, maxSubstring)

        return maxSubstring
        