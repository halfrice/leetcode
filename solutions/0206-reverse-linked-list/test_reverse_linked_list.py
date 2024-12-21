from reverse_linked_list import Solution, Utils

solution = Solution()
utils = Utils()


def test_case_1():
    head = [1, 2, 3, 4, 5]
    linked_list = utils.list_to_linked_list(head)
    output_linked_list = solution.reverseList(linked_list)
    output = utils.linked_list_to_list(output_linked_list)
    expected = [5, 4, 3, 2, 1]
    assert output == expected


def test_case_2():
    head = [1, 2]
    linked_list = utils.list_to_linked_list(head)
    output_linked_list = solution.reverseList(linked_list)
    output = utils.linked_list_to_list(output_linked_list)
    expected = [2, 1]
    assert output == expected


def test_case_3():
    head = []
    linked_list = utils.list_to_linked_list(head)
    output_linked_list = solution.reverseList(linked_list)
    output = utils.linked_list_to_list(output_linked_list)
    expected = []
    assert output == expected
