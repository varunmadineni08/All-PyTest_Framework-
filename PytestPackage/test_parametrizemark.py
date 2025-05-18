import pytest

@pytest.mark.parametrize("username, password", [
    ("admin", "admin123"),
    ("user1", "pass1"),
    ("guest", "guest123")
])
def test_login(username, password):
    print(f"Testing login with {username}/{password}")
    assert username != "" and password != ""


@pytest.mark.parametrize("browser", ["chrome", "firefox", "safari"])
def test_browser_support(browser):
    print(f"Running test on: {browser}")
    assert browser in ["chrome", "firefox", "safari"]


@pytest.mark.parametrize("input, expected", [
    (2 + 2, 4),
    (3 * 3, 9),
    (5 - 1, 4)
])
def test_math(input, expected):
    assert input == expected
