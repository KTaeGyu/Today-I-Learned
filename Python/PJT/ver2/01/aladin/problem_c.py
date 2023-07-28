import json
from pprint import pprint


def books_info(books, categories):
    books_info = []
    for book in books:
        new_book_info = {}
        new_book_info['author'] = book.get('author')
        categoryName = []
        for i in book.get('categoryId'):
            for j in categories:
                if i == j.get('id'):
                    categoryName.append(j.get('name'))
        new_book_info['categoryId'] = categoryName
        new_book_info['cover'] = book.get('cover')
        new_book_info['description'] = book.get('description')
        new_book_info['id'] = book.get('id')
        new_book_info['priceSales'] = book.get('priceSales')
        new_book_info['title'] = book.get('title')
        books_info.append(new_book_info)
    return books_info
        



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('./SSAFY/Python/PJT/ver2/01/aladin/data/books.json', encoding='utf-8')
    books = json.load(books_json)

    categories_json = open('./SSAFY/Python/PJT/ver2/01/aladin/data/categories.json', encoding='utf-8')
    categories_list = json.load(categories_json)

    pprint(books_info(books, categories_list))