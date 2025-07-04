# https://leetcode.com/problems/text-justification/


class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        total_words = len(words)
        res = []
        i = 0

        while i < total_words:
            # Hardcode the first word
            line = [words[i]]
            # Update the width with the length of the first word
            width = len(words[i])
            # Move to the next word
            i += 1

            # Because the first word was hardcoded, the strategy to create the rest of
            # the line is to simulate adding a space (the +1) before, or to the left,
            # of every next word that will fill the line
            while i < total_words and width + 1 + len(words[i]) <= maxWidth:
                # Update the width with a space followed by the length of the next word
                width += 1 + len(words[i])
                line.append(words[i])
                i += 1

            # Check if it's the last line or the line has only 1 word
            if i == total_words or len(line) == 1:
                # Put a space between multiple words or none if it's 1 word
                left_line = ' '.join(line)
                # Fill the rest of the line with spaces
                right_spaces = ' ' * (maxWidth - len(left_line))
                res.append(left_line + right_spaces)
            # Handle multiple words on the line except the last line
            else:
                # Get the number of spaces already added to the current line
                edges = len(line) - 1
                # Get the total number of spaces that will fill the line
                total_spaces = maxWidth - (width - edges)
                equal_spaces, extra_spaces = divmod(total_spaces, edges)
                line_with_spaces = []

                # Leave the last word out because no spaces will be added to the right
                for j, word in enumerate(line[:-1]):
                    line_with_spaces.append(word)
                    extra_space = 1 if j < extra_spaces else 0
                    line_with_spaces.append(' ' * (equal_spaces + extra_space))

                # Hardcode the last word
                line_with_spaces.append(line[-1])
                res.append(''.join(line_with_spaces))

        return res
