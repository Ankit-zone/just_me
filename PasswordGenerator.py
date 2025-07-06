import string
import random
from tkinter import *
from tkinter import messagebox
import sqlite3

with sqlite3.connect("users.db") as db:
    cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users(Username TEXT NOT NULL, GeneratedPassword TEXT NOT NULL);")
cursor.execute("SELECT * FROM users")
db.commit()
db.close()


class PasswordApp:
    def __init__(self, window):
        self.window = window
        self.user_name_var = StringVar()
        self.password_len_var = IntVar()
        self.generated_password_var = StringVar()

        window.title('Password Generator')
        window.geometry('660x500')
        window.config(bg='#FF8000')
        window.resizable(False, False)

        Label(text=":PASSWORD GENERATOR:", anchor=N, fg='darkblue', bg='#FF8000',
              font='arial 20 bold underline').grid(row=0, column=1)

        Label(text="").grid(row=1, column=0, columnspan=2)

        Label(text="Enter User Name: ", font='times 15 bold', bg='#FF8000', fg='darkblue').grid(row=2, column=0)
        self.username_entry = Entry(textvariable=self.user_name_var, font='times 15', bd=6, relief='ridge')
        self.username_entry.grid(row=2, column=1)
        self.username_entry.focus_set()

        Label(text="").grid(row=3, column=0)

        Label(text="Enter Password Length: ", font='times 15 bold', bg='#FF8000', fg='darkblue').grid(row=4, column=0)
        self.length_entry = Entry(textvariable=self.password_len_var, font='times 15', bd=6, relief='ridge')
        self.length_entry.grid(row=4, column=1)

        Label(text="").grid(row=5, column=0)

        Label(text="Generated Password: ", font='times 15 bold', bg='#FF8000', fg='darkblue').grid(row=6, column=0)
        self.password_entry = Entry(textvariable=self.generated_password_var, font='times 15', bd=6,
                                    relief='ridge', fg='#DC143C')
        self.password_entry.grid(row=6, column=1)

        Label(text="").grid(row=7, column=0)

        Button(text="GENERATE PASSWORD", bd=3, relief='solid', padx=1, pady=1,
               font='Verdana 15 bold', fg='#68228B', bg='#BCEE68',
               command=self.generate_password).grid(row=8, column=1)

        Label(text="").grid(row=9, column=0)

        Button(text="ACCEPT", bd=3, relief='solid', padx=1, pady=1,
               font='Helvetica 15 bold italic', fg='#458B00', bg='#FFFAF0',
               command=self.accept_entry).grid(row=10, column=1)

        Label(text="").grid(row=11, column=0)

        Button(text="RESET", bd=3, relief='solid', padx=1, pady=1,
               font='Helvetica 15 bold italic', fg='#458B00', bg='#FFFAF0',
               command=self.reset_fields).grid(row=12, column=1)

    def generate_password(self):
        upper = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        lower = list("abcdefghijklmnopqrstuvwxyz")
        symbols = list("@#%&()\"?!")
        digits = list("1234567890")

        username = self.username_entry.get()
        length_input = self.length_entry.get()

        if username == "":
            messagebox.showerror("Error", "Name cannot be empty")
            return
        if not username.isalpha():
            messagebox.showerror("Error", "Name must be a string")
            self.username_entry.delete(0, 25)
            return

        try:
            length = int(length_input)
            if length < 6:
                messagebox.showerror("Error", "Password must be at least 6 characters long")
                return
        except ValueError:
            messagebox.showerror("Error", "Password length must be a number")
            return

        self.password_entry.delete(0, length)

        num_upper = random.randint(1, length - 3)
        num_lower = random.randint(1, length - 2 - num_upper)
        num_sym = random.randint(1, length - 1 - num_upper - num_lower)
        num_digit = length - num_upper - num_lower - num_sym

        password_parts = (
            random.sample(upper, num_upper) +
            random.sample(lower, num_lower) +
            random.sample(symbols, num_sym) +
            random.sample(digits, num_digit)
        )
        random.shuffle(password_parts)
        final_password = "".join(password_parts)
        self.password_entry.insert(0, final_password)

    def accept_entry(self):
        with sqlite3.connect("users.db") as db:
            cursor = db.cursor()
            cursor.execute("SELECT * FROM users WHERE Username = ?", [self.user_name_var.get()])

            if cursor.fetchall():
                messagebox.showerror("This username already exists!", "Please use another username")
            else:
                cursor.execute("INSERT INTO users(Username, GeneratedPassword) VALUES(?, ?)",
                               (self.user_name_var.get(), self.generated_password_var.get()))
                db.commit()
                messagebox.showinfo("Success!", "Password generated successfully")

    def reset_fields(self):
        self.username_entry.delete(0, 25)
        self.length_entry.delete(0, 25)
        self.password_entry.delete(0, 25)


if __name__ == '__main__':
    root = Tk()
    PasswordApp(root)
    root.mainloop()