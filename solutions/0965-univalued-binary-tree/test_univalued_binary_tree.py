from univalued_binary_tree import Solution, Utils

solution = Solution()
utils = Utils()


def test_case_1():
    root = [1, 1, 1, 1, 1, None, 1]
    root_tree = utils.list_to_tree(root)
    expected = True
    assert solution.isUnivalTree(root_tree) == expected


def test_case_2():
    root = [2, 2, 2, 5, 2]
    root_tree = utils.list_to_tree(root)
    expected = False
    assert solution.isUnivalTree(root_tree) == expected
