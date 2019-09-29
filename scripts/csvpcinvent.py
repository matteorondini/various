import csv

originale = {}  # Dichiarazione liste
finale = []

print("Converte CSV in PCINVENT\nAutore: Matteo Rondini")

with open("ean.csv", "r") as file:  # Lettura del file PCINVENT
    reader = csv.DictReader(file, delimiter=";")
    for row in reader:
        conta_ean = str.count(row["EAN"], "") - 1
        conta_qt = str.count(row["QT"][0:-3], "") - 1
        row = ("0"*(13 - conta_ean)) + \
            row["EAN"] + ("0"*(7 - conta_qt) + row["QT"]
                          [0:-3]) + row["QT"][-2:]
        finale.append(row)
    print(f"{len(finale)} elementi convertiti correttamente")

with open("PCINVENT", "w") as file2:
    for elemento in finale:
        file2.write(f"{elemento}\n")
