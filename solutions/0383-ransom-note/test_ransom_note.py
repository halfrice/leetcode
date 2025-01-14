from ransom_note import Solution

solution = Solution()


def test_case_1():
    ransomNote = 'a'
    magazine = 'b'
    expected = False
    assert solution.canConstruct(ransomNote, magazine) == expected


def test_case_2():
    ransomNote = 'aa'
    magazine = 'ab'
    expected = False
    assert solution.canConstruct(ransomNote, magazine) == expected


def test_case_3():
    ransomNote = 'aa'
    magazine = 'aab'
    expected = True
    assert solution.canConstruct(ransomNote, magazine) == expected


def test_case_4():
    ransomNote = 'bg'
    magazine = 'efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj'
    expected = True
    assert solution.canConstruct(ransomNote, magazine) == expected
