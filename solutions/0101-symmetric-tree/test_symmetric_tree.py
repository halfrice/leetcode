from symmetric_tree import Solution, Utils

solution = Solution()
utils = Utils()


def test_case_1():
    root = [1, 2, 2, 3, 4, 4, 3]
    root_tree = utils.list_to_tree(root)
    expected = True
    assert solution.isSymmetric(root_tree) == expected


def test_case_2():
    root = [1, 2, 2, None, 3, None, 3]
    root_tree = utils.list_to_tree(root)
    expected = False
    assert solution.isSymmetric(root_tree) == expected
