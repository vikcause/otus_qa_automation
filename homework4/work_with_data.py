"""
Scripts for distribution books from books.csv to users from users.json
"""
import csv
import json


class DistributeBooks:
    """main class for distributing books to users"""

    def __init__(self):
        self.books = []
        self.users = {}

    def read_books(self):
        """method for reading data from csv"""

        with open('books.csv', 'r', encoding="utf-8") as f:
            reader = csv.DictReader(f)
            self.books = [row for row in reader]

    def read_users(self):
        """method for reading data from json"""

        with open('users.json', 'r', encoding="utf-8") as f:
            self.users = json.load(f)

    def distribute_books(self):
        """method for distributing books to users and writing result
        to new file - result.json"""
        books_per_user = len(self.books) // len(self.users)
        books_dict = {}

        for i, book in enumerate(self.books):
            user_index = i % len(self.users)
            user = self.users[user_index]
            if user['_id'] not in books_dict:
                books_dict[user['_id']] = {'books': []}
            books_dict[user['_id']]['books'].append(book)

        for j, user in enumerate(self.users):
            books_dict[user['_id']] = {'books': []}
            for i in range(books_per_user):
                book_id = i + j * books_per_user
                if book_id < len(self.books):
                    books_dict[user['_id']]['books'].append(self.books[book_id])

        for i in range(len(self.books) - books_per_user * len(self.users)):
            user = self.users[i]
            book_id = books_per_user * len(self.users) + i;
            books_dict[user['_id']]['books'].append(self.books[book_id])

        for user in self.users:
            user['books'] = books_dict[user['_id']]['books']

    def write_result(self):
        """method for write data to results.json"""

        with open('result.json', 'w', encoding="utf-8") as f:
            json.dump(self.users, f)


distribute_books = DistributeBooks()
distribute_books.read_books()
distribute_books.read_users()
distribute_books.distribute_books()
distribute_books.write_result()
