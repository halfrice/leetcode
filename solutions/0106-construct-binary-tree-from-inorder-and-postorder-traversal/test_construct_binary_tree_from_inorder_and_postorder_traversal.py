from construct_binary_tree_from_inorder_and_postorder_traversal import Solution, Utils


solution = Solution()
utils = Utils()


def test_case_1():
    inorder = [9, 3, 15, 20, 7]
    postorder = [9, 15, 7, 20, 3]
    result_tree = solution.buildTree(inorder, postorder)
    result = utils.tree_to_list(result_tree)
    expected = [3, 9, 20, None, None, 15, 7]
    assert result == expected


def test_case_2():
    inorder = [-1]
    postorder = [-1]
    result_tree = solution.buildTree(inorder, postorder)
    result = utils.tree_to_list(result_tree)
    expected = [-1]
    assert result == expected
