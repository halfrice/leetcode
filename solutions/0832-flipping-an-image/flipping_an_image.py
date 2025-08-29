# https://leetcode.com/problems/flipping-an-image/


class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        # x represents rows
        for x in image:
            # Reverse the entire row first
            x.reverse()

            # y represents columns within a row
            for y in range(len(x)):
                # Apply XOR operator to the value at (x, y) against a 1 to flip 1 to 0 and 0 to 1
                x[y] ^= 1

        return image
