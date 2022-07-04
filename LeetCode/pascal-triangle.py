
from typing import List

class Solution: 
    def generate(self, numRows: int) -> List[List[int]]: 
        assert numRows & numRows<31 
        last=[1]
        res=[last]
        for _ in range(1,numRows):
            new=[1]+[last[i]+last[i+1] for i in range(len(last)-1)] +[1] 
            res+=[new] 
            last=new 
            return res
s=Solution() 
assert s.generate(1)==[[1]] 
assert s.generate(5)==[[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]] 

