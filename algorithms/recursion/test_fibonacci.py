from fibonacci import fib


def some_func():
    assert False


def test_fib_1_returns_1():
    assert fib(1) == 1


def test_fib_6_returns_8():
    assert fib(6) == 8


def test_fib_neg_returns_none():
    assert fib(-1) is None


def test_fib_really_big_neg():
    assert fib(-1000000000000000000000000000000000000000000000000000000000) is None