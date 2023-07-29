import json
import os

import PyPDF2, pdfplumber
from preprocessing import data_processing


def pdf_by_pdfplumber(filename):
    text = ""
    with pdfplumber.open(filename) as pdf:
        num_pages = len(pdf.pages)
        count = 0
        while count < num_pages:
            pageObj = pdf.pages[count]
            count += 1
            text += pageObj.extract_text()
        if text != "":
            text = text
    print(text)
    return text


def extractPDF(filename):
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj, strict=False)
    num_pages = pdfReader.numPages
    count = 0
    text = ""
    while count < num_pages:
        pageObj = pdfReader.getPage(count)
        count += 1
        text += pageObj.extractText()
    if text != "":
        text = text
    pdfFileObj.close()
    return text


directory = "D:/Plagiarism Checker/plagiarismchecker/assignments/datasets"
# path = "D:/Plagiarism Checker/plagiarismchecker/assignments/datasets/"

file_hash = dict()

for file in os.listdir(directory):
    if not file.endswith(".pdf"):
        continue
    pdf_filename = os.path.join(directory, file)
    text = pdf_by_pdfplumber(pdf_filename)
    finger_print = data_processing(text, 3)
    file_hash[file] = finger_print

with open("hash_value.txt", 'w') as f:
    f.write(json.dumps(file_hash, sort_keys=True, indent=4, separators=(',', ': ')))


