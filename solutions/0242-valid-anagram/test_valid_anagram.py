from valid_anagram import Solution

solution = Solution()


def test_case_1():
    s = 'anagram'
    t = 'nagaram'
    expected = True
    assert solution.isAnagram(s, t) == expected


def test_case_2():
    s = 'rat'
    t = 'car'
    expected = False
    assert solution.isAnagram(s, t) == expected


def test_custom_case_1():
    s = 'ac'
    t = 'bb'
    expected = False
    assert solution.isAnagram(s, t) == expected


def test_custom_case_2():
    s = 'agentleman'
    t = 'elegantman'
    expected = True
    assert solution.isAnagram(s, t) == expected
