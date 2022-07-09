class Solution:
    def checkString(self, s: str) -> bool:
        assert s
        last_a = -1
        first_b = len(s)
        for i, c in enumerate(s):
            assert c == "a" or c == "b"
            if c == "a":
                last_a = i
            elif c == "b":
                first_b = min(first_b, i)
                if first_b < last_a:
                    return False
        return last_a < first_b


s = Solution()
assert s.checkString("ab")
assert not s.checkString("baa")
assert not s.checkString("aba")
assert s.checkString("aab")
assert not s.checkString(20 * "ab")
assert s.checkString(20 * "aa" + "b")
assert s.checkString("aaabbb")
assert not s.checkString("abab")
assert not s.checkString("babab")
assert not s.checkString("bbbbbbbbab")
assert s.checkString("aaaaaaaaab")
assert s.checkString("aaaaaaaaa")
assert s.checkString("bbb")
assert not s.checkString(99 * "b" + "a")
