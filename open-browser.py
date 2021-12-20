import webbrowser
from tkinter import *


def google():
    webbrowser.open('www.google.com')


root = Tk()
root.title('Open Browser')
root.geometry('300x200')

mywebsite = Button(root, text='Open site', command=google).pack(pady=20)

root.mainloop()
