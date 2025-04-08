from search_in_a_binary_search_tree import Solution, Utils

solution = Solution()
utils = Utils()


def test_case_1():
    root = [4, 2, 7, 1, 3]
    val = 2
    root_tree = utils.list_to_tree(root)
    result_tree = solution.searchBST(root_tree, val)
    result = utils.tree_to_list(result_tree)
    expected = [2, 1, 3]
    assert result == expected


def test_case_2():
    root = [4, 2, 7, 1, 3]
    val = 5
    root_tree = utils.list_to_tree(root)
    result_tree = solution.searchBST(root_tree, val)
    result = utils.tree_to_list(result_tree)
    expected = []
    assert result == expected
