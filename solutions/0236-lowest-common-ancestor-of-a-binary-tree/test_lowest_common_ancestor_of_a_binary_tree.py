from lowest_common_ancestor_of_a_binary_tree import Solution, Utils

solution = Solution()
utils = Utils()


def test_case_1():
    root = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    root_tree = utils.list_to_tree(root)
    p = 5
    p_node = utils.get_node_with_val(root_tree, p)
    q = 1
    q_node = utils.get_node_with_val(root_tree, q)
    result_node = solution.lowestCommonAncestor(root_tree, p_node, q_node)
    expected = 3
    expected_node = utils.get_node_with_val(root_tree, expected)
    assert result_node == expected_node


def test_case_2():
    root = root = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    root_tree = utils.list_to_tree(root)
    p = 5
    p_node = utils.get_node_with_val(root_tree, p)
    q = 4
    q_node = utils.get_node_with_val(root_tree, q)
    result_node = solution.lowestCommonAncestor(root_tree, p_node, q_node)
    expected = 5
    expected_node = utils.get_node_with_val(root_tree, expected)
    assert result_node == expected_node


def test_case_3():
    root = root = [1, 2]
    root_tree = utils.list_to_tree(root)
    p = 1
    p_node = utils.get_node_with_val(root_tree, p)
    q = 2
    q_node = utils.get_node_with_val(root_tree, q)
    result_node = solution.lowestCommonAncestor(root_tree, p_node, q_node)
    expected = 1
    expected_node = utils.get_node_with_val(root_tree, expected)
    assert result_node == expected_node
