import os

percorso = input(f"Lists all filenames and sizes inside the selected path, including folders\nCurrent dir: {os.getcwd()}\nPath to scan: ")
totalsize = 0
misura = ""

for dirpath, dirnames, filenames in os.walk(percorso):
    print(f"Scanned path: {dirpath}")
    for file in filenames:
        print(f"{dirpath}/{file}: {(os.path.getsize(os.path.join(dirpath, file))/1024)} KB")
        totalsize += (os.path.getsize(os.path.join(dirpath, file)))

if totalsize >= 1024 and totalsize < (1024*1024):
    totalsize = (totalsize / 1024)
    misura = "KB"
elif totalsize >= (1024*1024):
    totalsize = (totalsize / (1024*1024))
    misura = "MB"
else:
    misura = "B"

print(f"\n\nTotal size: {totalsize} {misura}")