book = input()

checked_books = 0
is_book_found = False
current_book = input()


while current_book != "No More Books":
    if current_book == book:
        is_book_found = True
        break


    checked_books += 1
    current_book = input()

if is_book_found == False:
    print(f"The book you search is not here!")
    print(f"You checked {checked_books} books.")
else:
    print(f"You checked {checked_books} books and found it.")





