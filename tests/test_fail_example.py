import pytest

@pytest.mark.xfail(reason="This is intended failure for demo purpose")
def test_x_fail():
    assert False

@pytest.mark.skip(reason="This is intended SKIP for demo purpose")
def test_x_skip():
    pass    