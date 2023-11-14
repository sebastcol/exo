def factorielle(n):
    if n == 0:
        return 1
    else:
        return n * factorielle(n - 1)

num = int(input("Entrez un nombre pour calculer le factoriel : "))
print("Factoriel :", factorielle(num))
