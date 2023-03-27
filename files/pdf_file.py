import os

from fpdf import FPDF
from domain_models.book import Book


class PdfFile:
    OUTPUT_FOLDER = "reports"

    @staticmethod
    def _next_file_name():
        files = os.listdir(PdfFile.OUTPUT_FOLDER)
        max_file = 0
        for file in files:
            current_file_number = int(file.title().upper().replace("REPORT-(", "").replace(").PDF", ""))
            max_file = max(max_file, current_file_number)
        max_file = max_file + 1
        return 'Report-(%s).pdf' % max_file

    @staticmethod
    def save(results):
        if not os.path.exists(PdfFile.OUTPUT_FOLDER):
            os.mkdir(PdfFile.OUTPUT_FOLDER)
        key = 1
        pdf = FPDF('P', 'mm', 'A4')
        filename = PdfFile.OUTPUT_FOLDER + "/" + PdfFile._next_file_name()

        pdf.add_font("Roboto Regular", "", "Roboto-Regular.ttf", uni=True)
        pdf.set_font('Roboto Regular', '', 14)
        pdf.add_page()
        pdf.write(8, 'Все книги'.upper())
        pdf.ln(8)
        pdf.add_font("Roboto Thin", "", "Roboto-Thin.ttf", uni=True)
        pdf.set_font('Roboto Thin', '', 12)
        for result in results:
            (book_id, book) = result
            formatted_book = "%s. %s. \"%s\". %s г. (%s стр.)" % (key, book.author, book.title, book.year, book.count_pages)
            key = key + 1
            pdf.write(8, formatted_book)
            pdf.ln(8)
        pdf.output(filename, 'F')
        pdf.close()
        os.system("start %s" % filename)

    @staticmethod
    def save_one(result):
        PdfFile.save([result])




