import glob
import img2pdf
from PyPDF2 import PdfFileReader, PdfFileWriter


def convert_all(regex="*.jpg"):
    images = glob.glob(regex)
    images.sort()
    convert_list(images)


def convert_list(images):
    for image in images:
        with open(image.split('.')[0] + '.pdf', 'wb') as target, open(image, 'rb') as source:
            target.write(img2pdf.convert(source))


def concatenate_all(target, regex="*.pdf"):
    pdfs = glob.glob(regex)
    pdfs.sort()
    with open(target, 'wb') as output:
        concatenate_list(pdfs, output)


def concatenate_list(pdfs, target):
    input_streams = []
    try:
        for pdf in pdfs:
            input_streams.append(open(pdf, 'rb'))
        writer = PdfFileWriter()
        for reader in map(PdfFileReader, input_streams):
            for n in range(reader.getNumPages()):
                writer.addPage(reader.getPage(n))
        writer.write(target)
    finally:
        for f in input_streams:
            f.close()

if __name__ == '__main__':
    convert_all()
    concatenate_all('Termo de Compromisso.pdf', 'tc*.pdf')
