from min_stack import Runner

runner = Runner()


def test_case_1():
    ops = ['MinStack', 'push', 'push', 'push', 'getMin', 'pop', 'top', 'getMin']
    vals = [[], [-2], [0], [-3], [], [], [], []]
    expected = [None, None, None, None, -3, None, 0, -2]
    assert runner.run(ops, vals) == expected
