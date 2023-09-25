"""convert pdf to docx
"""
from pdf2docx import Converter

def convertir():
    cv = Converter('n.pdf')
    cv.convert('nuevo.docx', start=0, end=None)
    cv.close()