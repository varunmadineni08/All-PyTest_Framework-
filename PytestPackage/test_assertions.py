import pytest
def test_sample_one():# ==,!=
    a=10
    b=5
    assert a==b

def test_sample_two(): #comparison asserts <,>,<=,>=
    a=10
    b=1
    assert a>b

def test_sample_three():
    a="varun"
    b="madineni"
    assert a.__eq__(b)

#not in,in
def test_type4():
    a="varun madineni"
    #assert "varun" in a
    assert "arun" not in a
#length of list
def test_type5():
    a=[1,2,3,4,5,6,7,8,9,0]
    assert len(a)==10

#identity asserts (is, is not)
def test_type6():
    a=[1,2,3]
    b=a
    assert a is b
    #assert a is not b

#Exception assertion
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        a = 10 / 0

#Type assertions
def test_types():
    a="varun"
    assert isinstance(a,str)

#Boolean assertions
def test_bool():
    page_loaded = True
    assert page_loaded is True
    # button_disabled = False
    # assert button_disabled is False