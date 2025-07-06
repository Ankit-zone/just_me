from tkinter import *
from tkinter import messagebox
import sqlite3 as sql

def add_task():
    task = task_entry.get()
    if len(task) == 0:
        messagebox.showinfo('Error', 'Field is empty.')
    else:
        task_items.append(task)
        db_cursor.execute('INSERT INTO tasks VALUES (?)', (task,))
        refresh_list()
        task_entry.delete(0, 'end')

def refresh_list():
    task_list.delete(0, 'end')
    for item in task_items:
        task_list.insert('end', item)

def delete_task():
    try:
        selected = task_list.get(task_list.curselection())
        if selected in task_items:
            task_items.remove(selected)
            refresh_list()
            db_cursor.execute('DELETE FROM tasks WHERE title = ?', (selected,))
            db_connection.commit()
    except:
        messagebox.showinfo('Error', 'No task selected. Cannot delete.')

def delete_all_tasks():
    confirm = messagebox.askyesno('Delete All', 'Are you sure?')
    if confirm:
        task_items.clear()
        db_cursor.execute('DELETE FROM tasks')
        refresh_list()

def close_app():
    print(task_items)
    app_window.destroy()

def load_from_db():
    task_items.clear()
    for row in db_cursor.execute('SELECT title FROM tasks'):
        task_items.append(row[0])

if __name__ == "__main__":
    app_window = Tk()
    app_window.title("To-Do List")
    app_window.geometry("665x400+550+250")
    app_window.resizable(0, 0)
    app_window.configure(bg="#B5E5CF")

    db_connection = sql.connect('listofTasks.db')
    db_cursor = db_connection.cursor()
    db_cursor.execute('CREATE TABLE IF NOT EXISTS tasks (title TEXT)')

    task_items = []
    main_frame = Frame(app_window, bg="#8EE5EE")
    main_frame.pack(side="top", expand=True, fill="both")

    Label(main_frame, text="TO-DO-LIST\nEnter the Task Title:",
          font=("arial", 14, "bold"),
          bg="#8EE5EE", fg="#FF6103").place(x=20, y=30)

    task_entry = Entry(main_frame, font=("Arial", 14), width=42, fg="black", bg="white")
    task_entry.place(x=180, y=30)

    Button(main_frame, text="ADD", width=15, bg='#04AC0D',
           font=("arial", 14, "bold"), command=add_task).place(x=18, y=80)

    Button(main_frame, text="Remove", width=15, bg='#D4AC0D',
           font=("arial", 14, "bold"), command=delete_task).place(x=240, y=80)

    Button(main_frame, text="Delete All", width=15, bg='#D4AC0D',
           font=("arial", 14, "bold"), command=delete_all_tasks).place(x=460, y=80)

    Button(main_frame, text="Exit/Close", width=52, bg='#D4AC0D',
           font=("arial", 14, "bold"), command=close_app).place(x=17, y=330)

    task_list = Listbox(main_frame, width=70, height=9, font="bold", selectmode='SINGLE',
                        bg="WHITE", fg="BLACK", selectbackground="#FF8C00", selectforeground="BLACK")
    task_list.place(x=17, y=140)

    load_from_db()
    refresh_list()
    app_window.mainloop()

    db_connection.commit()
    db_cursor.close()