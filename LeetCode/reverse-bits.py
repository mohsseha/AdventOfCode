# https://leetcode.com/problems/reverse-bits/submissions/

#Runtime: 36 ms, faster than 87.81% of Python3 online submissions for Reverse Bits.
#Memory Usage: 13.9 MB, less than 49.26% of Python3 online submissions for Reverse Bits.

# how can you simplify this? 
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        mask = 1
        for i in range(32):
            if (mask << i) & n:
                res = (mask << (31 - i)) | res
        return res

