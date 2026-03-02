from collections import deque

# ---------------- Data Structures ----------------
books = []       # List for all books
issued_books = deque()  # Queue for issued books (first come, first served)
removed_books = []      # Stack for removed books

# ---------------- Core Functions ----------------
def add_book():
    book_name = input("Enter book name to add: ").strip()
    if book_name:
        books.append(book_name)
        print(f"✅ '{book_name}' added to library.\n")
    else:
        print("Book name cannot be empty.\n")

def remove_book():
    if not books:
        print("Library is empty. No books to remove.\n")
        return
    book = books.pop()  # Stack behavior
    removed_books.append(book)
    print(f"❌ '{book}' removed from library.\n")

def issue_book():
    if not books:
        print("Library is empty. No books to issue.\n")
        return
    book = books.pop(0)  # Queue behavior (first added book issued first)
    issued_books.append(book)
    print(f"📚 '{book}' has been issued.\n")

def search_book():
    name = input("Enter book name to search: ").strip()
    found = [b for b in books if name.lower() in b.lower()]
    if found:
        print(f"Found books: {', '.join(found)}\n")
    else:
        print("No book found with that name.\n")

def display_books():
    if not books:
        print("Library is empty.\n")
        return
    print("📖 Books in Library:")
    for idx, book in enumerate(books, 1):
        print(f"{idx}. {book}")
    print()

# ---------------- Menu ----------------
def show_menu():
    print("==== Library Management System ====")
    print("1. Add Book")
    print("2. Remove Last Book (Stack)")
    print("3. Issue Book to Student (Queue)")
    print("4. Search Book")
    print("5. Display All Books")
    print("6. Exit")

def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            add_book()
        elif choice == "2":
            remove_book()
        elif choice == "3":
            issue_book()
        elif choice == "4":
            search_book()
        elif choice == "5":
            display_books()
        elif choice == "6":
            print("Goodbye! 👋")
            break
        else:
            print("❌ Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()