import tkinter as tk
from tkinter import Label, messagebox

root = tk.Tk()
root.title("WhatsApp History")
root.iconbitmap("assets/youtubedownloader.ico")
root.geometry("200x400+840+100")
root.resizable(0,0)
try:
    with open("pywhatkit_txtfile.txt", "r") as f:
        Label(root, text=f.read()).pack()
except FileNotFoundError:
	messagebox.showinfo("WhatsApp History.",
                     "No History found.")

root.mainloop()
