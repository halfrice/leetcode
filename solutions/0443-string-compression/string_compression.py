# https://leetcode.com/problems/string-compression/


class Solution:
    def compress(self, chars: list[str]) -> int:
        cur, res = 0, 0  # cur = current pointer, res = result

        while cur < len(chars):
            # Find the next char that does not match cur
            next = cur + 1  # next = next char pointer
            while next < len(chars) and chars[cur] == chars[next]:
                next += 1

            # Update result pointer with current char
            chars[res] = chars[cur]
            res += 1

            # Handle sequence of chars longer than 1
            if next - cur > 1:
                count = str(next - cur)
                for c in count:
                    chars[res] = c
                    res += 1

            # Update cur to next different char
            cur = next

        return res
