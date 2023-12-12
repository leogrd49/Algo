password = str(input("Entrer un mdp: "))

def str_to_star(password):
    count_password = len(password)
    hide_password = "*" * count_password
    return hide_password

print(str_to_star(password))