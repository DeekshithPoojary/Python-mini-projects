#DAY 75 | pdf merging exercise

from pypdf import PdfWriter
import os

folder_path = 'C:\CodewithHarry Python'

pdffiles = os.listdir(folder_path)
pdffiles.sort()
merger = PdfWriter()

for file in pdffiles:
    if file.endswith(".pdf"):
        
        print(file)
        
        merger.append(file)
        
        
merger.write("merged_pdf.pdf")      #All the pdf files are merged into this pdf.
merger.close()


        



