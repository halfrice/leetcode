from linked_list_cycle import Solution, Utils

solution = Solution()
utils = Utils()


def test_case_1():
    head = [3, 2, 0, -4]
    pos = 1
    head_linked_list = utils.list_to_linked_list(head, pos)
    expected = True
    assert solution.hasCycle(head_linked_list) == expected


def test_case_2():
    head = [1, 2]
    pos = 0
    head_linked_list = utils.list_to_linked_list(head, pos)
    expected = True
    assert solution.hasCycle(head_linked_list) == expected


def test_case_3():
    head = [1]
    pos = -1
    head_linked_list = utils.list_to_linked_list(head, pos)
    expected = False
    assert solution.hasCycle(head_linked_list) == expected
