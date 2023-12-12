i = 0
word = ""
taille_word = 0

def count_word(word, taille_word):
    taille_word = len(word)
    return taille_word



print("Pour arrêter vos saisies entrez: STOP")

while word != "STOP":
    word = input("Entrer vos mots: ")
    i += count_word(word, taille_word)

    if word == "STOP":
        i -= 4


print(f"Le nombre total de lettres contenues dans chacun de vos mots est de: {i}")