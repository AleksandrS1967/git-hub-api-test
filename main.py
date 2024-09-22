import os
from github import Auth
from github import Github
api_token: str = os.getenv('GIT_TOKEN')


def app():
    auth = Auth.Token(api_token)
    g = Github(auth=auth)
    user = g.get_user()
    print(f"пользователь: {user.name}")
    repos = user.get_repos()
    repos_name_list = []
    print(f"\nСписок репозиториев получен:")
    for rep in repos:
        repos_name_list.append(rep.name)
        print(rep.name)
    if "test_repo" in repos_name_list:
        print("\nВ списке выше уже присутствует репозиторий с именем - test_repo")
        repo = user.get_repo("test_repo")
        repo.delete()
        print("\nПроизведено удаление репозитория - test_repo")
    else:
        repo = user.create_repo("test_repo")
        print(f"\nПроизведено Создание репозитория - {repo.name}")

if __name__ == "__main__":
    app()