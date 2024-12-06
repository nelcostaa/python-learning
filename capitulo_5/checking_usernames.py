current_users = [
    "nelson",
    "rafa",
    "andre",
    "nicholas",
    "john",
]

new_users = [
    "nelson",
    "john",
    "julia",
    "pick",
    "gabi",
]

current_users_lower = [user.lower() for user in current_users]

for user in new_users:
    if user.lower() in current_users_lower:
        print("voce precisara informar um novo nome de usuario.")
    else:
        print("nome disponivel")
