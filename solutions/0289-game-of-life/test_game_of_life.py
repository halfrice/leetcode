from game_of_life import Solution

solution = Solution()


def test_case_1():
    board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
    solution.gameOfLife(board)
    expected = [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]
    assert board == expected


def test_case_2():
    board = [[1, 1], [1, 0]]
    solution.gameOfLife(board)
    expected = [[1, 1], [1, 1]]
    assert board == expected
