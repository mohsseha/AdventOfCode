class Solution:
    def countAsterisks(self, s: str) -> int:
        res=0
        count=True
        for c in s:
            if c=="|":
                count=not count
            else:
                if count and c=="*":
                    res+=1
        return res




s=Solution()
assert s.countAsterisks("y|xxx|23jfeldkffds")==0
assert s.countAsterisks("y|***|23jfeldkffds")==0
assert s.countAsterisks("*|***|23jfeldkffds")==1
assert s.countAsterisks("*|***|23jfel||ffds")==1
assert s.countAsterisks("*|***|23jfel|*|*ffds")==2
assert s.countAsterisks("*|***|23jfel|*******|*ffds")==2
assert s.countAsterisks(5*"|||||||")==0
assert s.countAsterisks("l|*e*et|c**o|*de|")==2
assert s.countAsterisks("iamprogrammer")==0
assert s.countAsterisks("yo|uar|e**|b|e***au|tifu|l")==5
