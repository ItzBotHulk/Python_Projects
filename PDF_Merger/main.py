import PyPDF2

pdfFiles = ["sample_1.pdf", "sample_2.pdf"]
merger = PyPDF2.PdfMerger()
for filename in pdfFiles:
    pdfFile = open(filename, 'rb')
    pdfReader = PyPDF2.PdfReader(pdfFile)
    merger.append(pdfReader)
pdfFile.close()
merger.write('merged.pdf')