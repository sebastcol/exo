notes = {"Mia.K": 15, "Vladimir.P": 18, "Emily.R": 12} 
meilleur_eleve = max(notes, key=notes.get)
print("Meilleure note :", meilleur_eleve, notes[meilleur_eleve])
