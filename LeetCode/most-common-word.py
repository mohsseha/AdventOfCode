# naive implementation  https://leetcode.com/problems/most-common-word/


from typing import List


class Solution:
    SPLIT_CHARS=set(" !?',;.") #set is minor optimization

    def par_to_word_list(self,paragraph:str)-> List[str]:
        res=[]
        word=""
        for i,c in enumerate(paragraph):
            if c in self.SPLIT_CHARS or i==len(paragraph)-1:
                if i==len(paragraph)-1 and c not in self.SPLIT_CHARS:
                    word+=c
                if word:
                    res.append(word)
                word=""
                continue
            word+=c
        return res


    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph=paragraph.lower()
        banned=set(b.lower() for b in banned)
        word_list=self.par_to_word_list(paragraph)
        hist={}
        for w in word_list:
            if w in banned:
                continue
            if w in hist:
                hist[w]=hist[w]+1
            else:
                hist[w]=1
        mx_word=list(hist.keys())[0]
        for w in hist.keys():
            if hist[w]>hist[mx_word]:
                mx_word=w
        return mx_word
        
        



s = Solution()
assert s.mostCommonWord(paragraph="Bob hit a ball, the hit BALL flew far after it was hit.", banned=["hit"]) == "ball"
assert s.mostCommonWord(paragraph="a.", banned=[]) == "a"
