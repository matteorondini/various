import PyPDF2

# apertura e lettura dei 2 file PDF
pdf1 = open("test1.pdf", "rb")
pdf2 = open("test2.pdf", "rb")
reader1 = PyPDF2.PdfFileReader(pdf1)
reader2 = PyPDF2.PdfFileReader(pdf2)

# definizione del writer
writer = PyPDF2.PdfFileWriter()

# lettura delle pagine di pfd1 e passaggio al writer
for x in range(reader1.numPages):
    page = reader1.getPage(x)
    writer.addPage(page)

# lettura delle pagine di pfd2 e passaggio al writer
for x in range(reader2.numPages):
    page = reader2.getPage(x)
    writer.addPage(page)

# creazione ed apertura del file unito
pdf_unito = open("combinati.pdf", "wb")

#scrittura del file e chiusura di tutti i 3 file
writer.write(pdf_unito)
pdf_unito.close()
pdf1.close()
pdf2.close()