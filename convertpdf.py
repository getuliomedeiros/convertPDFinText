import PyPDF2

filename = './texto.pdf'

reader = PyPDF2.PdfFileReader(filename)

numPages = reader.getNumPages()

arquivo = open('arq01.txt','w')

for i in range(numPages):
  page = reader.getPage(i)
  text = page.extractText()
  arquivo.write(text)
arquivo.close()
