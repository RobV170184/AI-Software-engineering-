import sqlite3


def create_connection():
    """Create and return a connection to the ebookstore database."""
    return sqlite3.connect('ebookstore.db')


def create_tables(conn):
    """Create the book and author tables if they do not already exist."""
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS author (
            id      INTEGER PRIMARY KEY,
            name    TEXT NOT NULL,
            country TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS book (
            id       INTEGER PRIMARY KEY,
            title    TEXT NOT NULL,
            authorID INTEGER,
            qty      INTEGER,
            FOREIGN KEY (authorID) REFERENCES author(id)
        )
    ''')
    conn.commit()


def populate_initial_data(conn):
    """Populate the book and author tables with the initial dataset."""
    cursor = conn.cursor()

    authors = [
        (1290, 'Charles Dickens', 'England'),
        (8937, 'J.K. Rowling',    'England'),
        (2356, 'C.S. Lewis',      'Ireland'),
        (6380, 'J.R.R. Tolkien',  'South Africa'),
        (5620, 'Lewis Carroll',   'England'),
    ]
    cursor.executemany(
        'INSERT OR IGNORE INTO author (id, name, country) VALUES (?, ?, ?)',
        authors
    )

    books = [
        (3001, 'A Tale of Two Cities',                     1290, 30),
        (3002, "Harry Potter and the Philosopher's Stone",  8937, 40),
        (3003, 'The Lion, the Witch and the Wardrobe',     2356, 25),
        (3004, 'The Lord of the Rings',                    6380, 37),
        (3005, "Alice's Adventures in Wonderland",         5620, 12),
    ]
    cursor.executemany(
        'INSERT OR IGNORE INTO book (id, title, authorID, qty) VALUES (?, ?, ?, ?)',
        books
    )
    conn.commit()


def validate_id(prompt):
    """Prompt for and validate a 4-digit integer ID. Returns int or None."""
    value = input(prompt).strip()
    if not value.isdigit() or len(value) != 4:
        print("Error: ID must be exactly 4 digits.")
        return None
    return int(value)


def enter_book(conn):
    """Add a new book to the database."""
    cursor = conn.cursor()

    book_id = validate_id("Enter book ID (4 digits): ")
    if book_id is None:
        return

    title = input("Enter book title: ").strip()
    if not title:
        print("Error: Title cannot be empty.")
        return

    author_id = validate_id("Enter author ID (4 digits): ")
    if author_id is None:
        return

    cursor.execute('SELECT id FROM author WHERE id = ?', (author_id,))
    if not cursor.fetchone():
        print(f"Error: Author ID {author_id} not found.")
        return

    try:
        qty = int(input("Enter quantity: ").strip())
    except ValueError:
        print("Error: Quantity must be a whole number.")
        return

    try:
        cursor.execute(
            'INSERT INTO book (id, title, authorID, qty) VALUES (?, ?, ?, ?)',
            (book_id, title, author_id, qty)
        )
        conn.commit()
        print("Book added successfully.")
    except sqlite3.IntegrityError:
        print("Error: A book with that ID already exists.")


def update_book(conn):
    """Update a book's quantity (default), title, or authorID;
    or update the linked author's name and/or country."""
    cursor = conn.cursor()

    book_id = validate_id("Enter the book ID to update: ")
    if book_id is None:
        return

    cursor.execute('''
        SELECT book.id, book.title, book.qty,
               author.id, author.name, author.country
        FROM book
        INNER JOIN author ON book.authorID = author.id
        WHERE book.id = ?
    ''', (book_id,))
    row = cursor.fetchone()
    if not row:
        print("Book not found.")
        return

    _, title, qty, auth_id, auth_name, auth_country = row
    print(f"\nCurrent details:")
    print(f"  Title:           {title}")
    print(f"  Quantity:        {qty}")
    print(f"  Author Name:     {auth_name}")
    print(f"  Author Country:  {auth_country}")

    print("\nWhat would you like to update?")
    print("1. Quantity (default)")
    print("2. Title")
    print("3. Author ID")
    print("4. Author name and/or country")
    choice = input("Enter choice (1-4): ").strip()

    if choice in ('1', ''):
        try:
            new_qty = int(input("Enter new quantity: ").strip())
            cursor.execute('UPDATE book SET qty = ? WHERE id = ?', (new_qty, book_id))
            conn.commit()
            print("Quantity updated.")
        except ValueError:
            print("Error: Quantity must be a whole number.")

    elif choice == '2':
        new_title = input("Enter new title: ").strip()
        if not new_title:
            print("Error: Title cannot be empty.")
            return
        cursor.execute('UPDATE book SET title = ? WHERE id = ?', (new_title, book_id))
        conn.commit()
        print("Title updated.")

    elif choice == '3':
        new_auth_id = validate_id("Enter new author ID (4 digits): ")
        if new_auth_id is None:
            return
        cursor.execute('SELECT id FROM author WHERE id = ?', (new_auth_id,))
        if not cursor.fetchone():
            print(f"Error: Author ID {new_auth_id} not found.")
            return
        cursor.execute('UPDATE book SET authorID = ? WHERE id = ?', (new_auth_id, book_id))
        conn.commit()
        print("Author ID updated.")

    elif choice == '4':
        new_name = input(
            f"New author name (press Enter to keep '{auth_name}'): "
        ).strip()
        new_country = input(
            f"New author country (press Enter to keep '{auth_country}'): "
        ).strip()
        if new_name:
            cursor.execute(
                'UPDATE author SET name = ? WHERE id = ?', (new_name, auth_id)
            )
        if new_country:
            cursor.execute(
                'UPDATE author SET country = ? WHERE id = ?', (new_country, auth_id)
            )
        conn.commit()
        print("Author details updated.")

    else:
        print("Invalid choice.")


def delete_book(conn):
    """Delete a book from the database after confirmation."""
    cursor = conn.cursor()

    book_id = validate_id("Enter book ID to delete: ")
    if book_id is None:
        return

    cursor.execute('SELECT title FROM book WHERE id = ?', (book_id,))
    row = cursor.fetchone()
    if not row:
        print("Book not found.")
        return

    confirm = input(f"Delete '{row[0]}'? (yes/no): ").strip().lower()
    if confirm == 'yes':
        cursor.execute('DELETE FROM book WHERE id = ?', (book_id,))
        conn.commit()
        print("Book deleted.")
    else:
        print("Deletion cancelled.")


def search_books(conn):
    """Search for books by ID, title keyword, or author name keyword."""
    cursor = conn.cursor()

    print("\nSearch by:")
    print("1. Book ID")
    print("2. Title")
    print("3. Author name")
    choice = input("Enter choice (1-3): ").strip()

    if choice == '1':
        book_id = input("Enter book ID: ").strip()
        cursor.execute('''
            SELECT book.id, book.title, author.name, author.country, book.qty
            FROM book INNER JOIN author ON book.authorID = author.id
            WHERE book.id = ?
        ''', (book_id,))
    elif choice == '2':
        keyword = input("Enter title keyword: ").strip()
        cursor.execute('''
            SELECT book.id, book.title, author.name, author.country, book.qty
            FROM book INNER JOIN author ON book.authorID = author.id
            WHERE book.title LIKE ?
        ''', (f'%{keyword}%',))
    elif choice == '3':
        keyword = input("Enter author name keyword: ").strip()
        cursor.execute('''
            SELECT book.id, book.title, author.name, author.country, book.qty
            FROM book INNER JOIN author ON book.authorID = author.id
            WHERE author.name LIKE ?
        ''', (f'%{keyword}%',))
    else:
        print("Invalid choice.")
        return

    rows = cursor.fetchall()
    if not rows:
        print("No books found.")
        return

    print(f"\n{'─' * 60}")
    for row in rows:
        print(f"ID:       {row[0]}")
        print(f"Title:    {row[1]}")
        print(f"Author:   {row[2]} ({row[3]})")
        print(f"Quantity: {row[4]}")
        print(f"{'─' * 60}")


def view_all_books(conn):
    """Display title, author name, and country for every book using zip()."""
    cursor = conn.cursor()

    cursor.execute('SELECT title FROM book')
    titles = [row[0] for row in cursor.fetchall()]

    cursor.execute('''
        SELECT author.name, author.country
        FROM book INNER JOIN author ON book.authorID = author.id
    ''')
    author_rows = cursor.fetchall()
    names     = [row[0] for row in author_rows]
    countries = [row[1] for row in author_rows]

    print("\nDetails")
    print('-' * 50)
    for title, name, country in zip(titles, names, countries):
        print(f"Title: {title}")
        print(f"Author's Name: {name}")
        print(f"Author's Country: {country}")
        print('-' * 50)


def main():
    """Main program loop — presents the menu and dispatches to functions."""
    with create_connection() as conn:
        create_tables(conn)
        populate_initial_data(conn)

        while True:
            print("\n" + "=" * 50)
            print("      BOOKSTORE MANAGEMENT SYSTEM")
            print("=" * 50)
            print("1. Enter book")
            print("2. Update book")
            print("3. Delete book")
            print("4. Search books")
            print("5. View details of all books")
            print("0. Exit")

            choice = input("\nEnter your choice: ").strip()

            if choice == '1':
                enter_book(conn)
            elif choice == '2':
                update_book(conn)
            elif choice == '3':
                delete_book(conn)
            elif choice == '4':
                search_books(conn)
            elif choice == '5':
                view_all_books(conn)
            elif choice == '0':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()
