from reorder_list import Solution, Utils

solution = Solution()
utils = Utils()


def test_case_1():
    head = [1, 2, 3, 4]
    head = utils.list_to_linked_list(head)
    solution.reorderList(head)
    output = utils.linked_list_to_list(head)
    expected = [1, 4, 2, 3]
    assert output == expected


def test_case_2():
    head = [1, 2, 3, 4, 5]
    head = utils.list_to_linked_list(head)
    solution.reorderList(head)
    output = utils.linked_list_to_list(head)
    expected = [1, 5, 2, 4, 3]
    assert output == expected
