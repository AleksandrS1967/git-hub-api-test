def create_repo(user, src):
    user.create_repo(src.repo_name)
    print(f"\nПроизведено Создание репозитория - {src.repo_name}")