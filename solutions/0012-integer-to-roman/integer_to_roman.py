# https://leetcode.com/problems/integer-to-roman/


class Solution:
    def intToRoman(self, num: int) -> str:
        roman = [
            ['I', 1],
            ['IV', 4],
            ['V', 5],
            ['IX', 9],
            ['X', 10],
            ['XL', 40],
            ['L', 50],
            ['XC', 90],
            ['C', 100],
            ['CD', 400],
            ['D', 500],
            ['CM', 900],
            ['M', 1000],
        ]

        res = ''
        for s, v in reversed(roman):
            if num // v:
                count = num // v
                res += s * count
                num = num % v

        return res
