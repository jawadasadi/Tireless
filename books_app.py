# V 3.2.0
import books_operations as bk

#--------------------main--------------

while True :
    bk.clear()
    print("==========================")
    print("Press A to add a book")
    print("Press L to list a book")
    print("Press F to find a book")
    print("Press D to delete a book")
    print("Press S to save all book")
    print("Press Q to quit application")
    print("==========================")
    choice = input("Enter Your Choice : ").upper()
    if choice == "A":
        bk.add_book()
    elif choice == "L":
        bk.list_books()
    elif choice == "F":
        bk.find_book()
    elif choice == "D":
        bk.delete_book()
    elif choice == "S":
        bk.save_books()
    elif choice == "Q":
        break
    else: input("\nWrong Choice !  Press any key ......")
    continue


