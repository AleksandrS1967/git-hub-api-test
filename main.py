import src


def app():
    user = src.auth(src)
    repos_name_list = src.get_repos_list(user)
    bool_check = src.check_repo_in_list(user, repos_name_list)

    if bool_check:
        src.create_repo(user, src)
    else:
        src.repo_delete(user, src)


if __name__ == "__main__":
    app()