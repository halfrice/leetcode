from middle_of_the_linked_list import Solution, Utils

solution = Solution()
utils = Utils()


def test_case_1():
    head = [1, 2, 3, 4, 5]
    head_linked_list = utils.list_to_linked_list(head)
    result = solution.middleNode(head_linked_list)
    result_list = utils.linked_list_to_list(result)
    expected = [3, 4, 5]
    assert result_list == expected


def test_case_2():
    head = [1, 2, 3, 4, 5, 6]
    head_linked_list = utils.list_to_linked_list(head)
    result = solution.middleNode(head_linked_list)
    result_list = utils.linked_list_to_list(result)
    expected = [4, 5, 6]
    assert result_list == expected
