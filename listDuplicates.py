names = ["Meenu", "Sanish", "Sanu", "Meenu"]

duplicates = set([x for x in names if names.count(x) > 1])
print("Duplicates:", duplicates)
