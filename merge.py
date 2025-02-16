
import os
from PyPDF2 import PdfMerger

x = [a for a in os.listdir("pdfs") if a.endswith(".pdf")]
print(x)
merger = PdfMerger()

for pdf in x:
    merger.append(open("pdfs/" + pdf, 'rb'))

with open("result.pdf", "wb") as fout:
    merger.write(fout)