from PyPDF2 import PdfFileWriter, PdfFileReader
import getpass
pdfwriter = PdfFileWriter()
pdf = PdfFileReader("/content/Deitel C How to Program 8th Edition.pdf")

for page_num in range(pdf.numPages):
  pdfwriter.addPage(pdf.getPage(page_num))

password = getpass.getpass(prompt = 'Enter password : ')
pdfwriter.encrypt(password)

with open("/content/Deitel C How to Program 8th Edition.pdf", "wb") as f:
  pdfwriter.write(f)
print("DONE")