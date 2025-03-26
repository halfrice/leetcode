from reverse_linked_list_ii import Solution, Utils

solution = Solution()
utils = Utils()


def test_case_1():
    head = [1, 2, 3, 4, 5]
    left = 2
    right = 4
    linked_list = utils.list_to_linked_list(head)
    result_linked_list = solution.reverseBetween(linked_list, left, right)
    result = utils.linked_list_to_list(result_linked_list)
    expected = [1, 4, 3, 2, 5]
    assert result == expected


def test_case_2():
    head = [5]
    left = 1
    right = 1
    linked_list = utils.list_to_linked_list(head)
    result_linked_list = solution.reverseBetween(linked_list, left, right)
    result = utils.linked_list_to_list(result_linked_list)
    expected = [5]
    assert result == expected


def test_case_3():
    head = [3, 5]
    left = 1
    right = 2
    linked_list = utils.list_to_linked_list(head)
    result_linked_list = solution.reverseBetween(linked_list, left, right)
    result = utils.linked_list_to_list(result_linked_list)
    expected = [5, 3]
    assert result == expected


def test_case_3():
    head = [3, 5, 7]
    left = 1
    right = 3
    linked_list = utils.list_to_linked_list(head)
    result_linked_list = solution.reverseBetween(linked_list, left, right)
    result = utils.linked_list_to_list(result_linked_list)
    expected = [7, 5, 3]
    assert result == expected
