from bank import value


def test_value():
    assert value("hello") == 0
    assert value("HELLO") == 0
    assert value("hiii") == 20
    assert value("woo") == 100

