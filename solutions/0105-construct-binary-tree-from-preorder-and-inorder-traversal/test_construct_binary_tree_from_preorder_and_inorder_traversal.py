from construct_binary_tree_from_preorder_and_inorder_traversal import Solution, Utils


solution = Solution()
utils = Utils()


def test_case_1():
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    result_tree = solution.buildTree(preorder, inorder)
    result = utils.tree_to_list(result_tree)
    expected = [3, 9, 20, None, None, 15, 7]
    assert result == expected


def test_case_2():
    preorder = [-1]
    inorder = [-1]
    result_tree = solution.buildTree(preorder, inorder)
    result = utils.tree_to_list(result_tree)
    expected = [-1]
    assert result == expected
