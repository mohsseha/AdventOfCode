#this algorithm is O(m*n), is there something faster?
class Solution:
    def strStr(self, heystack: str,needle: str):
        if not needle:
            return 0
        found = False
        for i in range(len(heystack)):
            for j in range(len(needle)):
                if i+j>=len(heystack) or needle[j] != heystack[i + j]:
                    break
                if j == len(needle) - 1:
                    found = True
            if found:
                return i
        return -1



