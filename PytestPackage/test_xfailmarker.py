import pytest

@pytest.mark.xfail(reason="unknown bug")
def test_total_calculation():
    assert 100 + 200 == 400

@pytest.mark.xfail(reason="Login button bug not fixed")
def test_login_button():
    assert False
@pytest.mark.xfail(reason="perfect calculation")
def test_calculation():
    assert 100+200==300