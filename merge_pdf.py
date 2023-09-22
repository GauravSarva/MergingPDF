from PyPDF2 import PdfWriter
import os


merging = PdfWriter()
pdf_files = [file for file in os.listdir() if file.endswith(".pdf")]
for pdf in pdf_files:
  merging.append(pdf)

merging.write("MERGED_PDFs.pdf")
merging.close()
