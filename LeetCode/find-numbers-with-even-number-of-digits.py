from typing import List


class Solution:
    def num_dig(self, n: int) -> int:
        assert n > -1
        if n == 0:
            return 1
        count = 0
        while n:
            count += 1
            n = n // 10
        return count

    def findNumbers(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            if not self.num_dig(n) % 2:  # even
                res += 1
        return res


s = Solution()
assert s.findNumbers([1, 1, 1, 1, 1]) == 0
assert s.findNumbers(400 * [12]) == 400
assert s.findNumbers([12, 345, 2, 6, 7896]) == 2
assert s.findNumbers([555, 901, 482, 1771]) == 1
assert s.findNumbers([555, 901, 482, 1771]) == 1
