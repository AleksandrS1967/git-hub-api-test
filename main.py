import src


def app():
    user = src.auth(src)
    if user == 0:
        print("Ошибка аутентификации (файла auth.py) - возможно не верно указан токен... или его срок истек...")
    else:
        repos_name_list = src.get_repos_list(user)
        bool_check = src.check_repo_in_list(src, repos_name_list)

        if bool_check:
            src.create_repo(user, src)
        else:
            src.repo_delete(user, src)


if __name__ == "__main__":
    app()