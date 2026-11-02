class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        charset = {}
        seen = {}
        for char in s1:
            charset[char] = 1 + charset.get(char, 0)

        l = 0

        for r in range(len(s2)):
            seen[s2[r]] = 1 + seen.get(s2[r],0)

            if (r - l + 1 > len(s1)):
                seen[s2[l]] = seen.get(s2[l], 0) - 1
                if seen[s2[l]] == 0:
                    del seen[s2[l]]
                l += 1
            
            if charset == seen:
                return True
        
        return False