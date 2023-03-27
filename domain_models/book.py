class Book:
    def __init__(self, title: str, year: int, author: str, count_pages: int):
        self.title = title
        self.year = year
        self.author = author
        self.count_pages = count_pages

    def __str__(self):
        return f'{self.author}. "{self.title}\". {self.year} г. ({self.count_pages} стр.)'

    def __repr__(self):
        return f'{self.title}, {self.year}, {self.author}, {self.count_pages}'

