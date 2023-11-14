numbers = [float(input(f"Entrez le nombre {i + 1} : ")) for i in range(10)]
print("Maximum :", max(numbers))
print("Minimum :", min(numbers))
print("Moyenne :", sum(numbers) / len(numbers))
