# palindrome_number.py


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        # Create array with individual digits
        n = x
        nums = []
        while n > 0:
            digit = n % 10
            nums.append(digit)
            n = n // 10

        # Iterate through nums array and compare front with back until midway
        i = 0
        nums_len = len(nums)
        while i < nums_len // 2:
            if nums[i] != nums[nums_len - 1 - i]:
                return False
            i += 1
        return True
