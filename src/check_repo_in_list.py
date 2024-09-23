def check_repo_in_list(src, repos_name_list):
    if "test_repo" in repos_name_list:
        print(f"\nВ списке выше уже присутствует репозиторий с именем - {src.repo_name}")
        return False
    else:
        return True
