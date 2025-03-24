from odd_even_linked_list import Solution, Utils

solution = Solution()
utils = Utils()


def test_case_1():
    head = [1, 2, 3, 4, 5]
    linked_list = utils.list_to_linked_list(head)
    result_linked_list = solution.oddEvenList(linked_list)
    result = utils.linked_list_to_list(result_linked_list)
    expected = [1, 3, 5, 2, 4]
    assert result == expected


def test_case_2():
    head = [2, 1, 3, 5, 6, 4, 7]
    linked_list = utils.list_to_linked_list(head)
    result_linked_list = solution.oddEvenList(linked_list)
    result = utils.linked_list_to_list(result_linked_list)
    expected = [2, 3, 6, 7, 1, 5, 4]
    assert result == expected
