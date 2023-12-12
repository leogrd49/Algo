i = 0
word = ""
taille_word = 0
word_stock = []

def count_word(word):
    taille_word = len(word)
    return taille_word

print("Pour arrêter vos saisies entrez: STOP")

while word != "STOP":
    word = input("Entrer vos mots: ")
    
    if word != "STOP":
        taille = count_word(word)
        word_stock.append(taille)
        i += taille


print(word_stock)
print("Le total est de: ", i)
