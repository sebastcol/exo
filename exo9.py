elements = [float(input(f"Entrez l'élément {i + 1} : ")) for i in range(10)]
carres = [x ** 2 for x in elements]
print("Carrés des éléments :", carres)
