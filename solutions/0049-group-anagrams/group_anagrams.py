# https://leetcode.com/problems/group-anagrams/


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hashmap = {}
        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s not in hashmap:
                hashmap[sorted_s] = []
            hashmap[sorted_s].append(s)

        groups = []
        for v in hashmap.values():
            v.sort()
            groups.append(v)

        groups.sort(key=len)
        return groups
