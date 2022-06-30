from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        assert nums 
        dups=set()
        for i in nums: 
            if i in dups: 
                dups.remove(i)
            else:
                dups.add(i)
        return dups.pop()


s=Solution()
nums = [2,2,1]
assert s.singleNumber(nums)==1
nums = [4,1,2,1,2]
assert s.singleNumber(nums)==4
nums=[1]
assert s.singleNumber(nums)==1


