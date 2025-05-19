# https://leetcode.com/problems/substring-with-concatenation-of-all-words/

from collections import Counter


class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        word_len = len(words[0])
        word_count = Counter(words)
        res = []

        # Iterate through all indices of possible substrings
        for i in range(word_len):
            left = i
            sub_count = Counter()
            matches = 0

            # Iterate through s with a step of word_len
            for j in range(i, len(s) - word_len + 1, word_len):
                # Get the current word for this iteration
                word = s[j : j + word_len]

                if word in word_count:
                    sub_count[word] += 1
                    matches += 1

                    # Handle case where the substring contains an extra occurence
                    # of the current word
                    while sub_count[word] > word_count[word]:
                        matches -= 1
                        sub_count[s[left : left + word_len]] -= 1
                        left += word_len

                    # If all words are in the current substring, add the index to result
                    if matches == len(words):
                        res.append(left)

                # If word is not in sub_count
                else:
                    # Move left forwad by a step of word_len
                    left = j + word_len
                    # Reset sub_count and matches
                    sub_count.clear()
                    matches = 0

        return res
