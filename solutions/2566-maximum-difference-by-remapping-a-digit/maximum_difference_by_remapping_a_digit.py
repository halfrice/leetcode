# https://leetcode.com/problems/maximum-difference-by-remapping-a-digit/


class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = str(num)
        min_num = int(s.replace(s[0], '0'))

        for d in s:
            if d != '9':
                max_num = int(s.replace(d, '9'))

                return max_num - min_num

        return num - min_num
