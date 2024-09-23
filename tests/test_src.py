import src
import pytest


@pytest.fixture
def auth_init():
    auth_ = src.Auth.Token(src.api_token)
    g = src.git(auth=auth_)
    user = g.get_user()
    return user, g


def test_auth():
    user = src.auth(src)
    assert user != 0


def test_auth_error():
    src.api_token = "345645dfghdfgh"
    user = src.auth(src)
    assert user == 0