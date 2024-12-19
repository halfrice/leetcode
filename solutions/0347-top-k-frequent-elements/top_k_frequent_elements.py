# https://leetcode.com/problems/top-k-frequent-elements/


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        bucket = [[] for _ in range(len(nums) + 1)]
        for n, c in freq.items():
            bucket[c].append(n)

        top = []
        for i in bucket[:0:-1]:
            for n in i:
                top.append(n)
                if len(top) == k:
                    return top
