# https://leetcode.com/problems/contains-duplicate-ii/


class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        # Sliding window solution
        window = set()
        i = 0

        for j in range(len(nums)):
            if j - i > k:
                window.remove(nums[i])
                i += 1

            if nums[j] in window:
                return True

            window.add(nums[j])

        return False
