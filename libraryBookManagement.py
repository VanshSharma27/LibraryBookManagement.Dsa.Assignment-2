# -----------------------------
# Node Class for Book (Linked List)
# -----------------------------
class Book:
    def _init_(self, book_id, title, author, status="Available"):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.status = status
        self.next = None


# -----------------------------
# Stack Node for Transactions
# -----------------------------
class Transaction:
    def _init_(self, action, book_id):
        self.action = action  # "Issue" or "Return"
        self.book_id = book_id
        self.next = None


# -----------------------------
# Stack Class for Undo Functionality
# -----------------------------
class TransactionStack:
    def _init_(self):
        self.top = None

    def push(self, action, book_id):
        new_trans = Transaction(action, book_id)
        new_trans.next = self.top
        self.top = new_trans

    def pop(self):
        if self.top is None:
            return None
        popped = self.top
        self.top = self.top.next
        return popped

    def is_empty(self):
        return self.top is None

    def view_transactions(self):
        if self.top is None:
            print("No recent transactions.")
            return
        print("\nRecent Transactions:")
        temp = self.top
        while temp:
            print(f"{temp.action} Book ID: {temp.book_id}")
            temp = temp.next
        print()


# -----------------------------
# BookList Class (Linked List)
# -----------------------------
class BookList:
    def _init_(self):
        self.head = None

    def insert_book(self, book_id, title, author):
        new_book = Book(book_id, title, author)
        if self.head is None:
            self.head = new_book
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_book
        print("Book inserted successfully!")

    def delete_book(self, book_id):
        if self.head is None:
            print("No books available.")
            return

        if self.head.book_id == book_id:
            self.head = self.head.next
            print("Book deleted successfully!")
            return

        prev = None
        curr = self.head
        while curr and curr.book_id != book_id:
            prev = curr
            curr = curr.next

        if curr is None:
            print("Book not found.")
            return

        prev.next = curr.next
        print("Book deleted successfully!")

    def search_book(self, book_id):
        temp = self.head
        while temp:
            if temp.book_id == book_id:
                return temp
            temp = temp.next
        return None

    def display_books(self):
        if self.head is None:
            print("No books in the library.")
            return

        print("\nCurrent Book List:")
        temp = self.head
        while temp:
            print(
                f"Book ID: {temp.book_id} | Title: {temp.title} | "
                f"Author: {temp.author} | Status: {temp.status}"
            )
            temp = temp.next
        print()

    # -----------------------------
    # Transaction Functions
    # -----------------------------
    def issue_book(self, book_id, stack):
        book = self.search_book(book_id)
        if not book:
            print("Book not found!")
            return
        if book.status == "Issued":
            print("Book already issued.")
            return
        book.status = "Issued"
        stack.push("Issue", book_id)
        print("Book issued successfully!")

    def return_book(self, book_id, stack):
        book = self.search_book(book_id)
        if not book:
            print("Book not found!")
            return
        if book.status == "Available":
            print("Book is already available.")
            return
        book.status = "Available"
        stack.push("Return", book_id)
        print("Book returned successfully!")

    def undo_transaction(self, stack):
        if stack.is_empty():
            print("No transactions to undo.")
            return

        last = stack.pop()
        book = self.search_book(last.book_id)
        if not book:
            print("Book not found for undo operation.")
            return

        if last.action == "Issue":
            book.status = "Available"
            print("Undo successful: Book returned to library.")
        elif last.action == "Return":
            book.status = "Issued"
            print("Undo successful: Book re-issued.")


# -----------------------------
# Menu Driven Program
# -----------------------------
def main():
    library = BookList()
    transactions = TransactionStack()

    while True:
        print("\n========== Library Management System ==========")
        print("1. Insert Book")
        print("2. Delete Book")
        print("3. Search Book")
        print("4. Display Books")
        print("5. Issue Book")
        print("6. Return Book")
        print("7. Undo Last Transaction")
        print("8. View Transactions")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                book_id = int(input("Enter Book ID: "))
                title = input("Enter Book Title: ")
                author = input("Enter Author Name: ")
                library.insert_book(book_id, title, author)
            except ValueError:
                print("Invalid input. Book ID must be an integer.")

        elif choice == "2":
            try:
                book_id = int(input("Enter Book ID to delete: "))
                library.delete_book(book_id)
            except ValueError:
                print("Invalid input. Book ID must be an integer.")

        elif choice == "3":
            try:
                book_id = int(input("Enter Book ID to search: "))
                book = library.search_book(book_id)
                if book:
                    print(
                        f"Book Found: {book.title} by {book.author} | Status: {book.status}"
                    )
                else:
                    print("Book not found.")
            except ValueError:
                print("Invalid input. Book ID must be an integer.")

        elif choice == "4":
            library.display_books()

        elif choice == "5":
            try:
                book_id = int(input("Enter Book ID to issue: "))
                library.issue_book(book_id, transactions)
            except ValueError:
                print("Invalid input. Book ID must be an integer.")

        elif choice == "6":
            try:
                book_id = int(input("Enter Book ID to return: "))
                library.return_book(book_id, transactions)
            except ValueError:
                print("Invalid input. Book ID must be an integer.")

        elif choice == "7":
            library.undo_transaction(transactions)

        elif choice == "8":
            transactions.view_transactions()

        elif choice == "9":
            print("Exiting program...")
            break

        else:
            print("Invalid choice! Try again.")


# -----------------------------
# Run the Program
# -----------------------------
if _name_ == "_main_":
    main()
