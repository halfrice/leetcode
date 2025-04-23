from diameter_of_binary_tree import Solution, Utils

solution = Solution()
utils = Utils()


def test_case_1():
    root = [1, 2, 3, 4, 5]
    root_tree = utils.list_to_tree(root)
    result = solution.diameterOfBinaryTree(root_tree)
    expected = 3
    assert result == expected


def test_case_2():
    root = [1, 2]
    root_tree = utils.list_to_tree(root)
    result = solution.diameterOfBinaryTree(root_tree)
    expected = 1
    assert result == expected
