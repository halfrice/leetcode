from reverse_nodes_in_k_group import Solution, Utils

solution = Solution()
utils = Utils()


def test_case_1():
    head = [1, 2, 3, 4, 5]
    k = 2
    linked_list = utils.list_to_linked_list(head)
    result_linked_list = solution.reverseKGroup(linked_list, k)
    result = utils.linked_list_to_list(result_linked_list)
    expected = [2, 1, 4, 3, 5]
    assert result == expected


def test_case_2():
    head = [1, 2, 3, 4, 5]
    k = 3
    linked_list = utils.list_to_linked_list(head)
    result_linked_list = solution.reverseKGroup(linked_list, k)
    result = utils.linked_list_to_list(result_linked_list)
    expected = [3, 2, 1, 4, 5]
    assert result == expected
