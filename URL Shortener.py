from tkinter import *
import pyshorteners 
#creating a new window 
win = Tk()
win.title("URL SHORTENER")
win.geometry("500x500")

def shorten():
    if short.get():
        short.delete(0,END)

    if entry.get():
        #convert to tinyurl
        url = pyshorteners.Shortener().tinyurl.short(entry.get())
        #output to screen 
        short.insert(END, url)

l = Label(win, text="Enter Link to Shorten", font=("Ivy" , 18, "bold"))
l.pack(pady=20)

entry = Entry(win, font=("Ivy" , 18))
entry.pack(pady=20)

button = Button(win, text="Shorten The Link", font=("Ivy" , 18, "bold"), command=shorten)
button.pack(pady=20)

short_l = Label(win, text="Shortened Link", font=("Ivy" , 16))
short_l.pack(pady=50)

short = Entry(win, font=("Ivy" , 20), justify=CENTER, width=25)
short.pack(pady=10)

win.mainloop()
