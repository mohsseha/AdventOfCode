from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        res=strs[0]
        for r in strs[1:]:
            #go over each row and find max match
            mxlen=min(len(res),len(r))
            res=res[0:mxlen]
            for j in range(mxlen):
                if res[j]!=r[j]:
                    res=res[0:j]
                    break
            if not res:
                break
        return res



