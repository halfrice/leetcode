from delete_the_middle_node_of_a_linked_list import Solution, Utils

solution = Solution()
utils = Utils()


def test_case_1():
    head = [1, 3, 4, 7, 1, 2, 6]
    head = utils.list_to_linked_list(head)
    output = solution.deleteMiddle(head)
    output = utils.linked_list_to_list(output)
    expected = [1, 3, 4, 1, 2, 6]
    assert output == expected


def test_case_2():
    head = [1, 2, 3, 4]
    head = utils.list_to_linked_list(head)
    output = solution.deleteMiddle(head)
    output = utils.linked_list_to_list(output)
    expected = [1, 2, 4]
    assert output == expected


def test_case_3():
    head = [2, 1]
    head = utils.list_to_linked_list(head)
    output = solution.deleteMiddle(head)
    output = utils.linked_list_to_list(output)
    expected = [2]
    assert output == expected


def test_case_4():
    head = [1]
    head = utils.list_to_linked_list(head)
    output = solution.deleteMiddle(head)
    output = utils.linked_list_to_list(output)
    expected = []
    assert output == expected
