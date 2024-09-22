def check_repo_in_list(user, repos_name_list):
    if "test_repo" in repos_name_list:
        print("\nВ списке выше уже присутствует репозиторий с именем - test_repo")
        return False
    else:
        return True
