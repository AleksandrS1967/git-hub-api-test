def get_repos_list(user):
    repos = user.get_repos()
    repos_name_list = []
    print(f"\nСписок репозиториев получен:")
    for rep in repos:
        repos_name_list.append(rep.name)
        print(rep.name)
    return repos_name_list