# NOT DONE! WILL BE CONTINUED IN NEXT CLASS: https://leetcode.com/problems/most-common-word/


from typing import List


class Solution:
    SPLIT_CHARS="!?',;."
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph=paragraph.lower()
        banned=[b.lower() for b in banned]
        




s = Solution()
assert s.mostCommonWord(paragraph="Bob hit a ball, the hit BALL flew far after it was hit.", banned=["hit"]) == "ball"
assert s.mostCommonWord(paragraph="a.", banned=[]) == "a"
