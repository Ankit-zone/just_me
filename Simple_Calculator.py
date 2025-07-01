import tkinter as tk

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(screen.get()))
            screen_var.set(result)
        except Exception:
            screen_var.set("Error")
    elif text == "C":
        screen_var.set("")
    else:
        screen_var.set(screen_var.get() + text)

root = tk.Tk()
root.geometry("300x400")
root.title("Simple Calculator")

screen_var = tk.StringVar()
screen = tk.Entry(root, textvar=screen_var, font="Arial 20")
screen.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

btn_frame = tk.Frame(root)
btn_frame.pack()

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-" ],
    ["C", "0", "=", "+"]
]

for row in buttons:
    frame = tk.Frame(btn_frame)
    frame.pack(expand=True, fill='both')
    for btn_text in row:
        btn = tk.Button(frame, text=btn_text, font="Arial 15", height=2, width=4)
        btn.pack(side='left', expand=True, fill='both', padx=2, pady=2)
        btn.bind("<Button-1>", click)

root.mainloop()
