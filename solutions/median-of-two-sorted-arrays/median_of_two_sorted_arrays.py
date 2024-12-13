# median_of_two_sorted_arrays.py


class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        x = nums1 if len(nums1) <= len(nums2) else nums2
        y = nums2 if len(nums2) >= len(nums1) else nums1
        xy_len = len(x) + len(y)

        head = len(x) - 1
        tail = 0
        while True:
            x_cut = (head + tail) // 2
            y_cut = (xy_len // 2) - x_cut - 2

            if x_cut >= 0:
                x_left = x[x_cut]
            else:
                x_left = float('-inf')
            if x_cut + 1 < len(x):
                x_right = x[x_cut + 1]
            else:
                x_right = float('inf')
            if y_cut >= 0:
                y_left = y[y_cut]
            else:
                y_left = float('-inf')
            if y_cut + 1 < len(y):
                y_right = y[y_cut + 1]
            else:
                y_right = float('inf')

            if x_left <= y_right and y_left <= x_right:
                if xy_len % 2 == 0:
                    return (max(x_left, y_left) + min(x_right, y_right)) / 2
                else:
                    return min(x_right, y_right)
            elif x_left > y_right:
                head = x_cut - 1
            else:
                tail = x_cut + 1
