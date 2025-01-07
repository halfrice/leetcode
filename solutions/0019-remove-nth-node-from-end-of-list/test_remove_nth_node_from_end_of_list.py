from remove_nth_node_from_end_of_list import Solution, Utils

solution = Solution()
utils = Utils()


def test_case_1():
    head = [1, 2, 3, 4, 5]
    n = 2
    head = utils.list_to_linked_list(head)
    output = solution.removeNthFromEnd(head, n)
    output = utils.linked_list_to_list(output)
    expected = [1, 2, 3, 5]
    assert output == expected


def test_case_2():
    head = [1]
    n = 1
    head = utils.list_to_linked_list(head)
    output = solution.removeNthFromEnd(head, n)
    output = utils.linked_list_to_list(output)
    expected = []
    assert output == expected


def test_case_3():
    head = [1, 2]
    n = 1
    head = utils.list_to_linked_list(head)
    output = solution.removeNthFromEnd(head, n)
    output = utils.linked_list_to_list(output)
    expected = [1]
    assert output == expected
