import os
from github import Auth
from github import Github

from src.auth import auth
from src.get_repos_list import get_repos_list
from src.check_repo_in_list import check_repo_in_list
from src.create_repo import create_repo
from src.repo_delete import repo_delete

repo_name = "test_repo"
Auth = Auth
git = Github
api_token: str = os.getenv('GIT_TOKEN')