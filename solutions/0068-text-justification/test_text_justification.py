from text_justification import Solution

solution = Solution()


def test_case_1():
    words = ['This', 'is', 'an', 'example', 'of', 'text', 'justification.']
    maxWidth = 16
    expected = [  # fmt: skip
        'This    is    an',
        'example  of text',
        'justification.  ',
    ]
    assert solution.fullJustify(words, maxWidth) == expected


def test_case_2():
    words = ['What', 'must', 'be', 'acknowledgment', 'shall', 'be']
    maxWidth = 16
    expected = [  # fmt: skip
        'What   must   be',
        'acknowledgment  ',
        'shall be        ',
    ]
    assert solution.fullJustify(words, maxWidth) == expected


def test_case_3():
    words = [
        'Science',
        'is',
        'what',
        'we',
        'understand',
        'well',
        'enough',
        'to',
        'explain',
        'to',
        'a',
        'computer.',
        'Art',
        'is',
        'everything',
        'else',
        'we',
        'do',
    ]
    maxWidth = 20
    expected = [  # fmt: skip
        'Science  is  what we',
        'understand      well',
        'enough to explain to',
        'a  computer.  Art is',
        'everything  else  we',
        'do                  ',
    ]
    assert solution.fullJustify(words, maxWidth) == expected
