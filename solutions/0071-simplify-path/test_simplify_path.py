from simplify_path import Solution

solution = Solution()


def test_case_1():
    path = '/home/'
    expected = '/home'
    assert solution.simplifyPath(path) == expected


def test_case_2():
    path = '/home/'
    expected = '/home'
    assert solution.simplifyPath(path) == expected


def test_case_3():
    path = '/home/user/Documents/../Pictures'
    expected = '/home/user/Pictures'
    assert solution.simplifyPath(path) == expected


def test_case_4():
    path = '/../'
    expected = '/'
    assert solution.simplifyPath(path) == expected


def test_case_5():
    path = path = '/.../a/../b/c/../d/./'
    expected = '/.../b/d'
    assert solution.simplifyPath(path) == expected
