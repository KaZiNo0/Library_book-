import datetime
import os

from peewee import MySQLDatabase, InternalError as PeeweeInternalError
from domain_models.book import Book
from repository.library import Library
from files.pdf_file import PdfFile


def print_main_menu():
    input("Нажмите \"Enter\" для выхода в главное меню")


class ConsoleLibrary:

    def _input_year(self):
        string_input = input("Введите год книги: ")
        year = int(float(string_input)) if '.' in string_input else int(string_input)
        while year <= 0 or year > int(datetime.date.today().year):
            string_input = input("Попробуйте ввести год еще раз:")
            year = int(float(string_input)) if '.' in string_input else int(string_input)
        return year

    def add_book(self):
        os.system("cls")
        title = input("Введите название книги: ")
        author = input("Введите автора книги: ")
        year = self._input_year()
        count_pages = int(input("Введите число страниц: "))
        book = Book(title, year, author, count_pages)
        change_option = input("Вы хотите создать книгу %s? 1-Да, 2-Нет: " % book)

        if change_option == '1':
            self.library.add(book=book)

        print_main_menu()

    def delete_book(self):
        os.system("cls")
        book_number = input("Введите номер книги для удаления:")
        book = self.library.get_at(book_number)
        if not book:
            input("Книга не найдена. Нажмите Enter, чтобы перейти в главное меню...")
            return

        change_option = input("Вы действительно хотите удалить книгу %s? 1-Да, 2-Нет: " % book)

        if change_option == '1':
            self.library.remove_at(book_number)
            print("Книга удалена ", book)

        print_main_menu()

    def change_title(self, book_number, book):
        os.system("cls")
        title = input("Введите название книги (Пусто, чтобы сохранить без изменений): ")
        if title == "" or book.title == title:
            input("Пустое название или не изменилось. Нажмите Enter, чтобы перейти в главное меню...")
            return
        book.title = title
        change_option = input("Вы хотите обновить книгу %s? 1-Да, 2-Нет: " % book)

        if change_option == '1':
            self.library.update_at(book_number, book)
            print("Книга обновлена ", book)

    def change_author(self, book_number, book):
        os.system("cls")
        author = input("Введите автора книги (Пусто, чтобы сохранить без изменений): ")
        if author == "" or book.author == author:
            input("Автор не введен или не изменилось. Нажмите Enter, чтобы перейти в главное меню...")
            return
        book.author = author
        change_option = input("Вы хотите обновить книгу %s? 1-Да, 2-Нет: " % book)

        if change_option == '1':
            self.library.update_at(book_number, book)
            print("Книга обновлена ", book)

    def change_year(self, book_number, book):
        os.system("cls")

        year = self._input_year()

        if book.year == year:
            input("Год не изменен. Нажмите Enter, чтобы перейти в главное меню...")
            return
        book.year = year

        change_option = input("Вы хотите обновить книгу %s? 1-Да, 2-Нет: " % book)

        if change_option == '1':
            self.library.update_at(book_number, book)
            print("Книга обновлена ", book)

    def change_count_pages(self, book_number, book):
        os.system("cls")

        count_pages = int(input("Введите количество страниц: "))

        if book.count_pages == count_pages:
            input("Количество страниц не изменено. Нажмите Enter, чтобы перейти в главное меню...")
            return
        book.count_pages = count_pages

        change_option = input("Вы хотите обновить книгу %s? 1-Да, 2-Нет: " % book)

        if change_option == '1':
            self.library.update_at(book_number, book)
            print("Книга обновлена ", book)

    def update_book(self):
        os.system("cls")
        book_id = input("Введите номер книги для обновления: ")
        book = self.library.get_at(book_id)

        if not book:
            input("Книга не найдена. Нажмите Enter, чтобы перейти в главное меню...")
            return

        print("Обновление книги ", book)
        change_option = input("Что вы хотите изменить?\n"
                              "1-Название\n"
                              "2-Автор\n"
                              "3-Год\n"
                              "4-Количество страниц\n"
                              "5-Отменить ввод, вернуться в главное меню\n"
                              "Enter: ")

        if change_option == "1":
            self.change_title(book_id, book)
        elif change_option == "2":
            self.change_author(book_id, book)
        elif change_option == "3":
            self.change_year(book_id, book)
        elif change_option == "4":
            self.change_count_pages(book_id, book)

        print_main_menu()

    def count_books(self):
        os.system("cls")
        books = self.library.get_all_books()
        print("Всего книг: ", len(books))
        print_main_menu()

    def list_books(self):
        os.system("cls")
        books = self.library.get_all_books()
        for book in books:
            print(book)
        print_main_menu()

    def find_books_year(self):
        os.system("cls")
        year = self._input_year()
        book = self.library.find_by_year(year)
        print("Найдено: ", book)
        return book

    def find_books_author(self):
        os.system("cls")
        author = input("Введите автора для поиска: ")
        book = self.library.find_by_author(author)
        print("Найдено: ", book)
        return book

    def find_books_title(self):
        os.system("cls")
        title = input("Введите название для поиска: ")
        book = self.library.find_by_title(title)
        print("Найдено: ", book)
        return book

    def find_books(self):
        os.system("cls")
        search = input("Поиск книги по: \n 1 - Году \n 2 - Автору \n 3 - Названию \n Enter:")
        result = None
        if search == "1":
            result = self.find_books_year()
        elif search == "2":
            result = self.find_books_author()
        elif search == "3":
            result = self.find_books_title()
        print_main_menu()
        return result

    def print_all_books(self):
        os.system("cls")
        pdf = PdfFile()
        books = self.library.get_all_books()
        pdf.save(books)
        print_main_menu()

    def __init__(self):
        self.library = Library(data_base=MySQLDatabase('3456', user='root1', password='',
                                               host='localhost', port=3306))

        self.library.connect()

    def run(self):
        try:
            while True:
                os.system("cls")
                command = input(
                    'Опции:\n'
                    '1 - Добавить запись\n'
                    '2 - Найти запись по параметру\n'
                    '3 - Изменить запись\n'
                    '4 - Удалить запись\n'
                    '5 - Вывод количества записей\n'
                    '6 - Вывод всех записей в справочнике\n'
                    '7 - Экспорт в PDF файл\n'
                    '8 - Выход\n'
                    'Введите опцию:')
                if command == "8":
                    break
                elif command == "1":
                    self.add_book()
                elif command == "2":
                    self.find_books()
                elif command == "3":
                    self.update_book()
                elif command == "4":
                    self.delete_book()
                elif command == "5":
                    self.count_books()
                elif command == "6":
                    self.list_books()
                elif command == "7":
                    self.print_all_books()

            self.library.close()
        except PeeweeInternalError as px:
            print(str(px))

        print("Вы завершили работу со справочником")
