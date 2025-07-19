texte = input("Entrez une chaîne : ")
inverse = ""

for char in texte:
    inverse = char + inverse  # Ajout devant pour inverser

print(f"Chaîne inversée : {inverse}")