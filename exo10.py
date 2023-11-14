def tri_insertion(liste):
    for i in range(1, len(liste)):
        cle = liste[i]
        j = i - 1
        while j >= 0 and cle < liste[j]:
            liste[j + 1] = liste[j]
            j -= 1
        liste[j + 1] = cle
    return liste

numbers = [float(input(f"Entrez le nombre {i + 1} : ")) for i in range(10)]
tri_insertion(numbers)
print("Liste triée :", numbers)
