from tkinter import *
from tkinter import messagebox

# Function to handle login
def Login():
    username = entry1.get()
    password = entry2.get()

    if username == '' or password == '':
        messagebox.showerror('Login Error', 'Fields cannot be empty!')
    elif username == 'madanrajsagar' and password == '11111111':
        messagebox.showinfo('Login Success', 'Login Successful!')
        root.destroy()  # Close the login window
        welcome_screen()
    else:
        messagebox.showerror('Login Error', 'Incorrect Username or Password!')

# Function to open the welcome screen
def welcome_screen():
    win = Tk()
    win.title("Welcome")
    win.geometry("800x500")
    win.configure(bg="#f0f0f0")

    Label(win, text="WELCOME TO MSBTE NAVIGATOR!", font=("Arial", 24, "bold"), bg="#f0f0f0", fg="green").pack(pady=50)
    
    win.mainloop()

# Function to toggle password visibility
def toggle_password():
    if entry2.cget('show') == '*':
        entry2.config(show='')
        toggle_btn.config(text="🙈 Hide")
    else:
        entry2.config(show='*')
        toggle_btn.config(text="👁 Show")

# Main login window
root = Tk()
root.title("Login Page")
root.geometry("500x400")
root.configure(bg="#2c3e50")

# Styling
title = Label(root, text="Login Page", font=("Arial", 24, "bold"), bg="#2c3e50", fg="#ecf0f1")
title.pack(pady=20)

frame = Frame(root, bg="#34495e", padx=20, pady=20)
frame.pack(pady=10)

Label(frame, text="Username", font=("Arial", 14), bg="#34495e", fg="white").grid(row=0, column=0, pady=10, padx=10)
entry1 = Entry(frame, font=("Arial", 14))
entry1.grid(row=0, column=1, pady=10, padx=10)

Label(frame, text="Password", font=("Arial", 14), bg="#34495e", fg="white").grid(row=1, column=0, pady=10, padx=10)
entry2 = Entry(frame, font=("Arial", 14), show="*")
entry2.grid(row=1, column=1, pady=10, padx=10)

# Toggle password visibility button
toggle_btn = Button(frame, text="👁 Show", font=("Arial", 10), command=toggle_password, bg="#16a085", fg="white", bd=0)
toggle_btn.grid(row=1, column=2, padx=5)

# Login Button with Hover Effect
def on_enter(e):
    login_btn.config(bg="#1abc9c")

def on_leave(e):
    login_btn.config(bg="#16a085")

login_btn = Button(root, text="Login", font=("Arial", 16, "bold"), bg="#16a085", fg="white", bd=0, padx=20, pady=5, command=Login)
login_btn.pack(pady=20)

login_btn.bind("<Enter>", on_enter)
login_btn.bind("<Leave>", on_leave)

root.mainloop()
