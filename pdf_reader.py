import PyPDF2
import os

# @author brandon
# Merges all the pdfs and extracts all the text from the /pdf directory

filenames = []

for filename in os.listdir('./pdf'):
    if filename.endswith('.pdf'):
        filenames.append(filename)

def write_pdf_to_text(filenames_list):

    note_results = ""

    for filename in filenames_list:
        with open("./pdf/{}".format(filename), "rb") as pdf:
            file_reader = PyPDF2.PdfFileReader(pdf)
            print("Currently writing pdf:", filename)
            for page_num in range(file_reader.numPages):
                page = file_reader.getPage(page_num)
                note_results += page.extractText()

    with open("EXTRACTED_TEXT.txt", "w", encoding="utf-8") as file_to_save:
        file_to_save.write(note_results)

    print("Sucessfully written all notes into .txt file!")

def merge_all_pdf(filenames_list):
    merger = PyPDF2.PdfFileMerger()

    for filename in filenames_list:
        with open("./pdf/{}".format(filename), "rb") as pdf:
            print("Currently merging pdf:", filename)
            merger.append(PyPDF2.PdfFileReader(pdf))

    with open('MERGED_PDF.pdf', 'wb') as output:
        merger.write(output)

    merger.close()

    print("Succesfully merged all slides into one pdf file!")

print("Begin writing all slides into text")
write_pdf_to_text(filenames)

print("Begin merging all slides into one PDF")
merge_all_pdf(filenames)
