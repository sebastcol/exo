with open('text.txt', 'r') as file:
    contenu = file.read()
    mots = contenu.split()
    nombre_mots = len(mots)

with open('output.txt', 'w') as file_out:
    file_out.write(f"Nombre de mots dans le fichier : {nombre_mots}")
