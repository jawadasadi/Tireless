from os import system 
clear = lambda :system("cls")

from pickle import load

with open("books.info", "rb") as books_info:
    books = load(books_info)


def add_to_excel():
    import xlsxwriter as xl
    pass


def add_book():
    clear()
    global books   #global list of all books (optional code)
    book = {}
    book["title"] = input("Enter title of the book : ")
    book["author"] = input("Enter author of the book : ")
    book["pages"] = int(input("Enter pages of the book : "))
    book["price"] = float(input("Enter price of the book : "))
    book["isbn"] = input("Enter ISBN of the book : ")
    books.append(book)
    input("Press any key .....")



def list_books():
    clear()
    for book in books :
        
        print(f"Title : {book['title']}")
        print(f"Author : {book['author']}")
        print(f"Pages : {book['pages']}")
        print(f"Price : {book['price']}")
        print(f"ISBN : {book['isbn']}")
        print("-------------------------------")
        # print(books.__sizeof__())
    input("Press any key .....")

def find_book():
    clear()
    isbn = input("Enter ISBN to find your book : ")
    for book in books :
        if book["isbn"] == isbn :
            print("------------------------------")
            print(f"Title : {book['title']}")
            print(f"Author : {book['author']}")
            print(f"Pages : {book['pages']}")
            print(f"Price : {book['price']}")
            print(f"ISBN : {book['isbn']}")
            print("-------------------------------")
            input("Press any key .....")

            break
    else:
        input("This book IS NOT in books database !")


def delete_book():
    clear()
    isbn = input("Enter ISBN to find your book : ")
    for book in books :
        if book["isbn"] == isbn :
            books.remove(book)
            input("Book has been deleted successfully.")

            break
    else:
         input("This book IS NOT in books database !")

def save_books():
       clear()
       from pickle import dump
       with open("Books.info","wb") as books_info :
           dump(books,books_info)
           input("Books has been saved successfully")
