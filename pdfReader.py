import PyPDF2

a = PyPDF2.PdfFileReader('sample.pdf')
print(a.documentInfo)
print(a.getNumPages())
print("Content of PDF is : ")
for page in range(a.getNumPages()):
    print(a.getPage(page).extractText())