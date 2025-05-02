from longest_zigzag_path_in_a_binary_tree import Solution, Utils

solution = Solution()
utils = Utils()


def test_case_1():
    root = [1, None, 1, 1, 1, None, None, 1, 1, None, 1, None, None, None, 1]
    root_tree = utils.list_to_tree(root)
    expected = 3
    assert solution.longestZigZag(root_tree) == expected


# HACK: Test case passes leetcode but not pytest (result = 3, expected = 4)
def test_case_2():
    root = [1, 1, 1, None, 1, None, None, 1, 1, None, 1]
    root_tree = utils.list_to_tree(root)
    expected = 4
    assert solution.longestZigZag(root_tree) == expected


def test_case_3():
    root = [1]
    root_tree = utils.list_to_tree(root)
    expected = 0
    assert solution.longestZigZag(root_tree) == expected
