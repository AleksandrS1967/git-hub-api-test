def create_repo(user, src):
    repo = user.create_repo(src.repo_name)
    print(f"\nПроизведено Создание репозитория - {src.repo_name}")
    return repo.name