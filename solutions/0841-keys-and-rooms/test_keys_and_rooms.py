from keys_and_rooms import Solution

solution = Solution()


def test_case_1():
    rooms = [[1], [2], [3], []]
    expected = True
    assert solution.canVisitAllRooms(rooms) == expected


def test_case_2():
    rooms = [[1, 3], [3, 0, 1], [2], [0]]
    expected = False
    assert solution.canVisitAllRooms(rooms) == expected
