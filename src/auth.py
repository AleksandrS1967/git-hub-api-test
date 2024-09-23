def auth(src):
    try:
        auth_ = src.Auth.Token(src.api_token)
        g = src.git(auth=auth_)
        user = g.get_user()
        print(f"пользователь: {user.name}")
        return user
    except src.github.GithubException:
        return 0