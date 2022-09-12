import os

def isBinod(fileName):
    with open(fileName) as f:
        content = f.read().lower()
    if "binod" in content:
        return f"File {fileName} has Found Word Binod !!!!!!\n"
    else: 
        return f"File {fileName} has not Found Word Binod !!\n"

if __name__ == "__main__":
    filesList = os.listdir()

    for item in filesList:
        if item.endswith("txt"):
            print(f"Finding Binod in file {item}")
            hasBinod = isBinod(item)
            print(hasBinod)
