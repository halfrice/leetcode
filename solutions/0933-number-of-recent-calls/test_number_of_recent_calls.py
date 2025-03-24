from number_of_recent_calls import Utils

utils = Utils()


def test_case_1():
    calls = ['RecentCounter', 'ping', 'ping', 'ping', 'ping']
    values = [[], [1], [100], [3001], [3002]]
    result = utils.command(list(zip(calls, values)))
    expected = [None, 1, 2, 3, 3]
    assert result == expected
