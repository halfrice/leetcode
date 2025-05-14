# https://leetcode.com/problems/letter-combinations-of-a-phone-number/


class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []

        # Since digits[i] is gauranteed to be 2-9, offset by 2
        charmap = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        combos = ['']

        for d in digits:
            # Get the letters corresponding to the digit
            chars = charmap[int(d) - 2]

            # # Construct combinations by appending each possible letter to each existing
            # temp = []
            # for p in combos:
            #     for c in chars:
            #         temp.append(p + c)
            # combos = temp
            # # Or the more pythonic way using list comprehension
            combos = [p + c for p in combos for c in chars]

        return combos
