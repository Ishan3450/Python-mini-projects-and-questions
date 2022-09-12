import os

def createFolder(folderName):
    if not os.path.exists(folderName):
        os.makedirs(folderName)

def moveFiles(folderName,fileListName):
    for file in fileListName:
        os.replace(file,f"{folderName}/{file}")

createFolder('Microsoft Word')
createFolder('Microsoft Excel')
createFolder('Microsoft Powerpoint')

fileList = os.listdir()
fileList.remove("ClutterFolder.py")

# for file in fileList:
#     print(file)

# For Word Documents
word = [file for file in fileList if os.path.splitext(file)[1].lower() == ".docx"]

# to print the Word List
print('\nWord Files :\n')
for wordFile in word:
    print(wordFile)

# For Excel Documents
excel = [file for file in fileList if os.path.splitext(file)[1].lower() == ".xlsx"]

# to print Excel Documents
print("\nExcel Documents : \n")
for excelFiles in excel:
    print(excelFiles)

# For Powerpoint Presentations
powerpoint = [file for file in fileList if os.path.splitext(file)[1].lower() == ".pptx"]

# to print PowerPoint Presentation
print('\nPowerPoint Presentations : \n')
for ppFile in powerpoint:
    print(ppFile)

# Replacing the files according to their Extesions
moveFiles("Microsoft Powerpoint",powerpoint)
moveFiles("Microsoft Excel",excel)
moveFiles("Microsoft Word",word)
print('File Cluttered !!')
print('\n')
