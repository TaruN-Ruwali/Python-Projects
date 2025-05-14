# Library Management System with GUI in Python
# Tech Stack: Python, Tkinter (GUI), SQLite (Database)

import tkinter as tk
from tkinter import messagebox, simpledialog
import sqlite3

# Database Setup
conn = sqlite3.connect('library.db')
cursor = conn.cursor()

# cursor.execute("DROP TABLE IF EXISTS books")  # Temporary for fixing structure
# cursor.execute("DROP TABLE IF EXISTS issues")  # Temporary for fixing structure

cursor.execute('''CREATE TABLE IF NOT EXISTS books (
                    id INTEGER PRIMARY KEY,
                    title TEXT,
                    author TEXT,
                    year INTEGER,
                    isbn TEXT,
                    total_copies INTEGER,
                    available_copies INTEGER)
            ''')

cursor.execute('''CREATE TABLE IF NOT EXISTS issues (
                    issue_id INTEGER PRIMARY KEY,
                    book_id INTEGER,
                    student_name TEXT,
                    issue_date TEXT,
                    FOREIGN KEY(book_id) REFERENCES books(id))
            ''')
conn.commit()

# Backend Functions
def add_book(title, author, year, isbn, copies):
    cursor.execute("INSERT INTO books (title, author, year, isbn, total_copies, available_copies) VALUES (?, ?, ?, ?, ?, ?)",
                   (title, author, year, isbn, copies, copies))
    conn.commit()

def view_books():
    cursor.execute("SELECT * FROM books")
    return cursor.fetchall()

def search_books(title="", author="", year="", isbn=""):
    cursor.execute("SELECT * FROM books WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
    return cursor.fetchall()

def delete_book(book_id):
    cursor.execute("DELETE FROM books WHERE id=?", (book_id,))
    cursor.execute("DELETE FROM issues WHERE book_id=?", (book_id,))
    conn.commit()

def update_book(book_id, title, author, year, isbn, copies):
    cursor.execute("UPDATE books SET title=?, author=?, year=?, isbn=?, total_copies=?, available_copies=? WHERE id=?",
                   (title, author, year, isbn, copies, copies, book_id))
    conn.commit()

def issue_book(book_id, student_name, issue_date):
    cursor.execute("SELECT available_copies FROM books WHERE id=?", (book_id,))
    available = cursor.fetchone()[0]
    if available > 0:
        cursor.execute("INSERT INTO issues (book_id, student_name, issue_date) VALUES (?, ?, ?)",
                       (book_id, student_name, issue_date))
        cursor.execute("UPDATE books SET available_copies = available_copies - 1 WHERE id=?", (book_id,))
        conn.commit()
        return True
    else:
        return False

def return_book(book_id, student_name):
    cursor.execute("DELETE FROM issues WHERE issue_id IN (SELECT issue_id FROM issues WHERE book_id=? AND student_name=? LIMIT 1)", (book_id, student_name))
    cursor.execute("UPDATE books SET available_copies = available_copies + 1 WHERE id=?", (book_id,))
    conn.commit()

def get_issued_students(book_id):
    cursor.execute("SELECT student_name FROM issues WHERE book_id=?", (book_id,))
    return [row[0] for row in cursor.fetchall()]

# GUI Setup
class LibraryGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")

        # Labels and Entries
        tk.Label(root, text="Title").grid(row=0, column=0)
        tk.Label(root, text="Author").grid(row=0, column=2)
        tk.Label(root, text="Year").grid(row=1, column=0)
        tk.Label(root, text="ISBN").grid(row=1, column=2)
        tk.Label(root, text="Copies").grid(row=2, column=0)

        self.title_text = tk.StringVar()
        self.author_text = tk.StringVar()
        self.year_text = tk.StringVar()
        self.isbn_text = tk.StringVar()
        self.copies_text = tk.StringVar()

        self.e1 = tk.Entry(root, textvariable=self.title_text)
        self.e2 = tk.Entry(root, textvariable=self.author_text)
        self.e3 = tk.Entry(root, textvariable=self.year_text)
        self.e4 = tk.Entry(root, textvariable=self.isbn_text)
        self.e5 = tk.Entry(root, textvariable=self.copies_text)

        self.e1.grid(row=0, column=1)
        self.e2.grid(row=0, column=3)
        self.e3.grid(row=1, column=1)
        self.e4.grid(row=1, column=3)
        self.e5.grid(row=2, column=1)

        # Listbox and Scrollbar
        self.listbox = tk.Listbox(root, height=10, width=80)
        self.listbox.grid(row=3, column=0, rowspan=6, columnspan=4)

        self.sb = tk.Scrollbar(root)
        self.sb.grid(row=3, column=4, rowspan=6)

        self.listbox.configure(yscrollcommand=self.sb.set)
        self.sb.configure(command=self.listbox.yview)

        self.listbox.bind('<<ListboxSelect>>', self.get_selected_row)

        # Buttons
        tk.Button(root, text="View All", width=12, command=self.view_command).grid(row=3, column=5)
        tk.Button(root, text="Search Book", width=12, command=self.search_command).grid(row=4, column=5)
        tk.Button(root, text="Add Book", width=12, command=self.add_command).grid(row=5, column=5)
        tk.Button(root, text="Update", width=12, command=self.update_command).grid(row=6, column=5)
        tk.Button(root, text="Delete", width=12, command=self.delete_command).grid(row=7, column=5)
        tk.Button(root, text="Issue Book", width=12, command=self.issue_command).grid(row=8, column=5)
        tk.Button(root, text="Return Book", width=12, command=self.return_command).grid(row=9, column=5)
        tk.Button(root, text="Close", width=12, command=root.quit).grid(row=10, column=5)

    def get_selected_row(self, event):
        index = self.listbox.curselection()[0]
        self.selected_tuple = self.listbox.get(index)
        self.e1.delete(0, tk.END)
        self.e1.insert(tk.END, self.selected_tuple[1])
        self.e2.delete(0, tk.END)
        self.e2.insert(tk.END, self.selected_tuple[2])
        self.e3.delete(0, tk.END)
        self.e3.insert(tk.END, self.selected_tuple[3])
        self.e4.delete(0, tk.END)
        self.e4.insert(tk.END, self.selected_tuple[4])
        self.e5.delete(0, tk.END)
        self.e5.insert(tk.END, self.selected_tuple[5])

    def view_command(self):
        self.listbox.delete(0, tk.END)
        for row in view_books():
            students = get_issued_students(row[0])
            display_info = f"Issued to: {', '.join(students)}" if students else f"Available ({row[6]} copies left)"
            self.listbox.insert(tk.END, row[:7] + (display_info,))

    def search_command(self):
        self.listbox.delete(0, tk.END)
        for row in search_books(self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get()):
            students = get_issued_students(row[0])
            display_info = f"Issued to: {', '.join(students)}" if students else f"Available ({row[6]} copies left)"
            self.listbox.insert(tk.END, row[:7] + (display_info,))

    def add_command(self):
        add_book(self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get(), int(self.copies_text.get()))
        self.view_command()

    def delete_command(self):
        delete_book(self.selected_tuple[0])
        self.view_command()

    def update_command(self):
        update_book(self.selected_tuple[0], self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get(), int(self.copies_text.get()))
        self.view_command()

    def issue_command(self):
        student_name = simpledialog.askstring("Issue Book", "Enter student name:")
        if student_name:
            from datetime import date
            success = issue_book(self.selected_tuple[0], student_name, date.today().isoformat())
            if success:
                messagebox.showinfo("Success", "Book issued successfully!")
            else:
                messagebox.showwarning("Unavailable", "No copies available!")
            self.view_command()

    def return_command(self):
        student_name = simpledialog.askstring("Return Book", "Enter student name:")
        if student_name:
            return_book(self.selected_tuple[0], student_name)
            messagebox.showinfo("Returned", "Book returned successfully!")
            self.view_command()

if __name__ == '__main__':
    root = tk.Tk()
    app = LibraryGUI(root)
    root.mainloop()
    conn.close()
