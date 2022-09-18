import pdfplumber as pdftools

def Fetch_Text(file_path):
    with pdftools.open(file_path) as tool:
        for page_num, page in enumerate(tool.pages, 1):
            print(f"page number is {page_num}")
            data = page.extract_text()
            print(data)
        
pdf_path = "C:\\Users\\Administrator\\Desktop\\My code\\simple project\\fetch pdf text\\pdf file\\EnglishELLBILHowUseDialoguesFreeBookpdf.pdf"

Fetch_Text(pdf_path)