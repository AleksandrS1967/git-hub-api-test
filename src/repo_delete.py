def repo_delete(user, src):
    repo = user.get_repo(src.repo_name)
    repo.delete()
    print(f"\nПроизведено удаление репозитория - {src.repo_name}")