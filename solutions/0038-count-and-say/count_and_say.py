# https://leetcode.com/problems/count-and-say/


class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'

        res = ''
        count = 1
        c = self.countAndSay(n - 1)
        c_len = len(c)

        for i in range(c_len):
            if i + 1 < c_len and c[i] == c[i + 1]:
                count += 1
            else:
                res += str(count) + c[i]
                count = 1

        return res
