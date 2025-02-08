# https://leetcode.com/problems/can-place-flowers/


class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        flowerbed = [0] + flowerbed + [0]

        i = 1
        while i < len(flowerbed) - 1:
            if not n:
                return not n

            prev = flowerbed[i - 1]
            cur = flowerbed[i]
            next = flowerbed[i + 1]

            if not prev and not cur and not next:
                n -= 1
                i += 1

            i += 1

        return not n
