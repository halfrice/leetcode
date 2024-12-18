from add_two_numbers import Solution, Utils

s = Solution()
u = Utils()


def test_case_1():
    l1 = [2, 4, 3]
    ll1 = u.list_to_linked_list(l1)
    l2 = [5, 6, 4]
    ll2 = u.list_to_linked_list(l2)
    ll_output = s.addTwoNumbers(ll1, ll2)
    output = u.linked_list_to_list(ll_output)
    expected = [7, 0, 8]
    assert output == expected


def test_case_2():
    l1 = [0]
    ll1 = u.list_to_linked_list(l1)
    l2 = [0]
    ll2 = u.list_to_linked_list(l2)
    ll_output = s.addTwoNumbers(ll1, ll2)
    output = u.linked_list_to_list(ll_output)
    expected = [0]
    assert output == expected


def test_case_3():
    l1 = [9, 9, 9, 9, 9, 9, 9]
    ll1 = u.list_to_linked_list(l1)
    l2 = [9, 9, 9, 9]
    ll2 = u.list_to_linked_list(l2)
    ll_output = s.addTwoNumbers(ll1, ll2)
    output = u.linked_list_to_list(ll_output)
    expected = [8, 9, 9, 9, 0, 0, 0, 1]
    assert output == expected
