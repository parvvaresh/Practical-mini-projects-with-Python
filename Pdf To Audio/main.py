import PyPDF2
import pyttsx3
import time

path_pdf = "C:\\Users\\Administrator\\Desktop\\My code\\PYTHON\\simple project\\Pdf To Audio\\Pdf\\test.pdf"

path = open(path_pdf, "rb")

pdf_reader = PyPDF2.PdfFileReader(path)

speak = pyttsx3.init()


for pages in range(pdf_reader.numPages):
    text = pdf_reader.getPage(pages).extractText()
    speak.say(text)
    speak.runAndWait()
    time.sleep(2)

speak.stop()