import pytest
import sys

@pytest.mark.smoke
def test_sample_one():
    print("smoke test is verified")

@pytest.mark.regression
def test_sample_two():
    print("regression is tested")

@pytest.mark.sanity
def test_sample_three():
    print("sanity is tested")

@pytest.mark.smoke
def test_sample_four():
    print("smoke test is verified")



