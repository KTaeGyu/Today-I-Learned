import json
from pprint import pprint



def book_info(book):
    new_book_info = {}
    new_book_info['author'] = book.get('author')
    new_book_info['categoryId'] = book.get('categoryId')
    new_book_info['cover'] = book.get('cover')
    new_book_info['description'] = book.get('description')
    new_book_info['id'] = book.get('id')
    new_book_info['priceSales'] = book.get('priceSales')
    new_book_info['title'] = book.get('title')
    return new_book_info
      

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    book_json = open('./SSAFY/Python/PJT/ver2/01/aladin/data/book.json', encoding='utf-8')
    book = json.load(book_json)
    
    pprint(book_info(book))
