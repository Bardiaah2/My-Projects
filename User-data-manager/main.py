"""A tkinter app that holds user datas and can check for them
easily add/delete data to ask for at line 105
"""
import tkinter as tk
import csv
from PIL import ImageTk, Image
import time

global num
global user_name
global data_entry
global submit
global error


class Entries:
    def __init__(self, *args, root=None, command=None):
        self.args = list(args)
        self.root = root
        self.command = command
        self.frame = tk.Frame(self.root)
        for i, j in enumerate(self.args):
            tk.Label(self.frame, text=j).grid(row=i, column=0, padx=20, pady=20)
            self.args[i] = tk.Entry(self.frame)
            self.args[i].grid(row=i, column=1, padx=20, pady=20)
            self.args[i].bind("<Return>", lambda event: self.command())
        self.args[0].focus()
        self.btn = tk.Button(self.frame, text="Send", command=self.command)
        self.btn.grid(row=i + 1, column=1)
        self.frame.pack(pady=20, padx=20)


class BackButton:
    def __init__(self, close_root, open_root):
        self.close_root = close_root
        self.open_root = open_root
        self.btn = tk.Button(self.close_root, text="Back")
        self.btn.config(bd=0)
        self.btn.bind("<Button-1>", lambda evnet: self.back())
        self.btn.place(x=0, y=0)

    def back(self):
        self.open_root.deiconify()
        self.close_root.destroy()


def rounds():
    global num
    global data_entry
    global error
    headline = ["Name", "Last Name", "Code"]
    data = {}
    try:
        error.destroy()
    except NameError:
        pass
    for i in range(2):
        if data_entry.args[i].get():
            data.setdefault(headline[i], data_entry.args[i].get())
        else:
            error = tk.Label(data_entry.frame, text=f"Error: fill\n{headline[i]}", foreground="red")
            error.grid(row=3, column=0)
            return None
    try:
        data.setdefault(headline[2], int(data_entry.args[2].get()))
        with open("User_datas.csv") as User_file:
            dic = csv.DictReader(User_file)
            for i in dic:
                if data["Code"] == int(i["Code"]):
                    error = tk.Label(data_entry.frame, text="Error: This code\nalready exists", foreground="red")
                    error.grid(row=3, column=0)
                    for j in range(3):
                        data_entry.args[j].delete(0, "end")
                    return None
        with open("User_datas.csv", "a", newline="\n") as User_file:
            writer = csv.DictWriter(User_file, headline)
            writer.writerow(data)
    except ValueError:
        error = tk.Label(data_entry.frame, text="Error:Code must\nbe a number", foreground="red")
        error.grid(row=3, column=0)
        num += 1
    for i in range(3):
        data_entry.args[i].delete(0, "end")
    num -= 1
    if num == 0:
        submit.destroy()
        window.deiconify()


def enter_user():
    global data_entry
    global num
    global submit

    def write_user():
        global data_entry
        global num
        try:
            num = int(user_entry.args[0].get())
            user_entry.args[0].delete(0, "end")
        except ValueError:
            tk.Label(user_entry.frame, text="Error: Enter a number", foreground="red").grid(row=1, column=0)
            return None
        user_entry.frame.destroy()
        data_entry = Entries("Name", "Last Name", "Code", root=submit, command=rounds)  # add to args for more data

    window.withdraw()
    submit = tk.Toplevel()
    submit.resizable(False, False)
    submit.geometry("850x500")
    submit.title("Submit")
    bg3 = ImageTk.PhotoImage(Image.open("bg3.jpg").resize((850, 500)))
    tk.Label(submit, image=bg3).place(x=0, y=0)
    BackButton(submit, window)
    tk.Label(submit, text="Enter Your User Data", font=("Arial", 20, "bold")).pack(pady=40, padx=40)
    user_entry = Entries("How many users\n"
                         "do you want to add?", root=submit, command=write_user)
    submit.mainloop()


def login():
    global user_name
    name, password = loginEntry.args[0].get(), loginEntry.args[1].get()
    with open("Login.csv") as login_file:
        dic = csv.DictReader(login_file)
        for i in dic:
            if name == i["Username"] and password == i["Password"]:
                user_name = i["Name"]
                loginWindow.destroy()
                return None
        loginEntry.args[0].delete(0, "end")
        loginEntry.args[1].delete(0, "end")
        tk.Label(loginEntry.frame, text="Username or \n "
                                        "password is wrong.", foreground="red").grid(row=2, column=2)


def check_user():
    def search():
        headline = ["Name", "Last Name", "Code"]
        searched_data = {}
        matched_data = [set(), set(), set()]
        for i in range(3):
            if search_entry.args[i].get():
                searched_data.setdefault(headline[i], search_entry.args[i].get())
                search_entry.args[i].delete(0, "end")
        with open("User_datas.csv") as User_file:
            dic = csv.DictReader(User_file)
            for row in dic:
                for i, (key, val) in enumerate(list(searched_data.items())):
                    if val == row[key].lower():
                        matched_data[i].add(f"{row}")
        search_result = tk.Tk()
        search_result.geometry("500x300")
        search_result.title("Search result")
        if i:
            if i == 1:
                matched_data[2] = matched_data[1]
            result = list(matched_data[0].intersection(matched_data[1]).intersection(matched_data[2]))
            if result:
                for i in range(len(result)):
                    tk.Label(search_result, text=result[i]).grid(row=i, column=0, padx=10, pady=10)
            else:
                tk.Label(search_result, text="No User Found.").pack(pady=20)
        else:
            result = list(matched_data[0])
            if result:
                for i in range(len(result)):
                    tk.Label(search_result, text=result[i]).grid(row=i, column=0, padx=10, pady=10)
            else:
                tk.Label(search_result, text="No User Found.").pack(pady=20)

    window.withdraw()
    check_window = tk.Toplevel()
    check_window.title("Search Users")
    check_window.resizable(False, False)
    check_window.geometry("850x500")
    bg4 = ImageTk.PhotoImage(Image.open("bg4.jpg").resize((850, 500)))
    tk.Label(check_window, image=bg4).place(x=0, y=0)
    BackButton(check_window, window)
    tk.Label(check_window, text="Search for Users.", font=("comic", 20, "bold")).pack(pady=40, padx=40)
    tk.Label(check_window, text="Search by code, name or both").pack(pady=20)
    search_entry = Entries("Name", "Last Name", "code", root=check_window, command=search)
    check_window.mainloop()


def signin():
    global loginEntry
    global signin_button

    def add_user():
        global loginEntry
        headline = ["Username", "Password", "Name"]
        data = {}
        for i in range(3):
            if signin_entry.args[i].get():
                data.setdefault(headline[i], signin_entry.args[i].get())
            else:
                tk.Label(signin_entry.frame, text=f"Error: fill\n{headline[i]}", foreground="red").grid(row=3, column=0)
                for j in range(3):
                    signin_entry.args[j].delete(0, "end")
                return None
        with open("Login.csv") as login_file:
            dic = csv.DictReader(login_file)
            for i in dic:
                if data["Username"].lower() == i["Username"].lower():
                    for j in range(3):
                        signin_entry.args[j].delete(0, "end")
                    tk.Label(signin_entry.frame,
                             text="Error:This username\nalready exists.",
                             foreground="red").grid(row=3,
                                                    column=0)
                    return None
        with open("Login.csv", "a", newline="\n") as login_file:
            writer = csv.DictWriter(login_file, headline)
            writer.writerow(data)
        signin_entry.frame.destroy()
        loginEntry = Entries("Username", "Password", root=loginWindow, command=login)
        signin_button = tk.Button(loginWindow, text="Signin", command=signin)
        signin_button.pack(pady=20)

    signin_button.destroy()
    loginEntry.frame.destroy()
    signin_entry = Entries("Username", "Password", "Name", root=loginWindow, command=add_user)


loginWindow = tk.Tk()
loginWindow.title("Login page")
loginWindow.geometry("800x500")
loginWindow.resizable(False, False)
bg1 = ImageTk.PhotoImage(Image.open("bg1.jpg").resize((800, 500)))
tk.Label(loginWindow, image=bg1).place(x=0, y=0)
tk.Label(loginWindow, text="Login", font=("Arial", 20, "bold")).pack()
loginEntry = Entries("Username", "Password", root=loginWindow, command=login)
signin_button = tk.Button(loginWindow, text="Signin", command=signin)
signin_button.pack(pady=20)
loginWindow.mainloop()

window = tk.Tk()
window.resizable(False, False)
window.geometry("850x500")
window.title("Main Window")
bg2 = ImageTk.PhotoImage(Image.open("bg2.jpg").resize((850, 500)))
tk.Label(window, image=bg2).place(x=0, y=0)
tk.Label(window, text=f"Hello {user_name}.", font=("Comic", 24), background="#8E7B8D").pack(pady=40)
tk.Label(window, text=f"Entered at {time.strftime('%a, %d %b %Y %H:%M:%S', time.localtime())}",
         background="#8E7B8D").pack(pady=10)
tk.Label(window, text="What do you want to do?", background="#8E7B8D").pack(pady=20)
EnterUser = tk.Label(window, text="Enter User", font=("Arial", 16), background="gray", height=2, width=20)
EnterUser.bind("<Button-1>", lambda event: enter_user())
EnterUser.pack(pady=20)
SearchUser = tk.Label(window, text="Search User", font=("Arial", 16), background="gray", height=2, width=20)
SearchUser.bind("<Button-1>", lambda event: check_user())
SearchUser.pack(pady=20)
window.mainloop()
