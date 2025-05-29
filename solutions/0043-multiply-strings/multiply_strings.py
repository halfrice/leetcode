# https://leetcode.com/problems/multiply-strings/


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'

        num1_len, num2_len = len(num1), len(num2)

        # Create a list with zeroes and a length of num1_len + num2_len to store digits
        res = [0] * (num1_len + num2_len)

        # Process digits from right to left
        for i in range(num1_len - 1, -1, -1):
            num1_digit = int(num1[i])
            for j in range(num2_len - 1, -1, -1):
                num2_digit = int(num2[j])
                res[i + j + 1] += num1_digit * num2_digit

        # Process the carries
        for i in range(num1_len + num2_len - 1, 0, -1):
            # Get the carry and add it to the next place value (ones -> tens -> hundreds)
            res[i - 1] += res[i] // 10
            # Process the value at res[i] and keep just the last digit (23 = 3, 98 = 8)
            res[i] %= 10

        i = 0 if res[0] != 0 else 1
        return ''.join(str(d) for d in res[i:])
