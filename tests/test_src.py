import src
import pytest


@pytest.fixture
def auth_user():
    auth_ = src.Auth.Token(src.api_token)
    g = src.git(auth=auth_)
    user = g.get_user()
    return user


@pytest.fixture
def auth_g():
    auth_ = src.Auth.Token(src.api_token)
    g = src.git(auth=auth_)
    return g


def test_auth():
    user = src.auth(src)
    assert user != 0


def test_get_repos_list(auth_user):
    list_repos = src.get_repos_list(auth_user)
    assert type(list_repos) == list


def test_check_repo_in_list_false():
    test_list_repo = [src.repo_name, 'work_repo']
    bool_ = src.check_repo_in_list(src, test_list_repo)
    assert not bool_


def test_check_repo_in_list_true():
    test_list_repo = ['repo_name', 'work_repo']
    bool_ = src.check_repo_in_list(src, test_list_repo)
    assert bool_


def test_create_repo(auth_user):
    name_repo = src.create_repo(auth_user, src)
    assert name_repo == src.repo_name


def test_delete_repo(auth_user):
    repo = src.repo_delete(auth_user, src)
    assert repo == src.repo_name


def test_auth_error():
    src.api_token = "345645dfghdfgh"
    user = src.auth(src)
    assert user == 0