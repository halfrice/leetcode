from lru_cache import Utils

utils = Utils()


def test_case_1():
    cmds = ['LRUCache', 'put', 'put', 'get', 'put', 'get', 'put', 'get', 'get', 'get']
    vals = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
    utils = Utils()
    expected = [None, None, None, 1, None, -1, None, -1, 3, 4]
    result = utils.command(tuple(zip(cmds, vals)))
    assert result == expected


def test_case_2():
    cmds = ['LRUCache', 'put', 'get']
    vals = [[1], [2, 1], [2]]
    utils = Utils()
    expected = [None, None, 1]
    result = utils.command(tuple(zip(cmds, vals)))
    assert result == expected


def test_case_3():
    cmds = ['LRUCache', 'put', 'put', 'get', 'put', 'put', 'get']
    vals = [[2], [2, 1], [2, 2], [2], [1, 1], [4, 1], [2]]
    utils = Utils()
    expected = [None, None, None, 2, None, None, -1]
    result = utils.command(tuple(zip(cmds, vals)))
    assert result == expected
