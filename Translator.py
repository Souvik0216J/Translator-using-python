from tkinter import *
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
from googletrans import Translator
import googletrans # pip install googletrans==3.1.0a0
import urllib.request

# Window Configuration
root = Tk()
root.title("Translator By Souvik Ghosh")
root.geometry("1080x400")
root.resizable(0, 0)
root.configure(bg="white")

# Current Using Language Swap Each Other
def Swap_language():
    lan1 = combo1.get()
    lan2 = combo2.get()
    if lan2 == "Select Language":
        pass
    else:
        combo2.set(f'{lan1}')
        combo1.set(f'{lan2}')

# To Change Language Name
def label_change():
    c = combo1.get()
    c1 = combo2.get()
    l1.configure(text=c)
    l2.configure(text=c1)
    root.after(500, label_change)

# To Translate Input
def Translate():
    try:
        text_ = text1.get(1.0, END)
        t1 = Translator()
        trans_text = t1.translate(text_, src=combo1.get(), dest=combo2.get())
        trans_text = trans_text.text

        text2.delete(1.0, END)
        text2.insert(END, trans_text)
    except:    
        def connect(host='http://google.com'):
            try:
                urllib.request.urlopen(host)  
                return True
            except:
                return False
        if (connect() == False):
            messagebox.showinfo("No Internet", "Cheak Your Internet Connection.")
        else:
            messagebox.showerror("Error", "Something Went Wrong! Try Again.")

# Press Enter To Active Function
def Enter(event):
    Translate()

# Icon
icon_img = PhotoImage(file="assets\\logo.png")
root.iconphoto(0, icon_img)

# Arrow Image
arrow_img =Image.open("assets\\Arrow.png")
resize_image = arrow_img.resize((150, 70))
final_img = ImageTk.PhotoImage(resize_image)
#img_l1 = Label(root, image=final_img)
swap_button = Button(image=final_img, font="Roboto 15 italic bold", activebackground="grey", command=Swap_language)
swap_button.place(x=457, y=75)
#img_l1.place(x=460, y=75)

# Create Combo Box List
language = googletrans.LANGUAGES
language_list = list(language.values())
lang1 = language.keys()

# Input Box
combo1 = ttk.Combobox(root, values=language_list, font="Roboto 14", state="r")
combo1.place(x=110, y=20)
combo1.set("English")

l1 = Label(root, text="ENGLISH", font="segoe 30 bold", width=18, bd=5, relief=GROOVE)
l1.place(x=10, y=50)

f1 = Frame(root, bg="Black", bd=5)
f1.place(x=10, y=118, width=440, height=210)

text1 = Text(f1, font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=430, height=200)

scrool_b1 = Scrollbar(f1)
scrool_b1.pack(side=RIGHT, fill="y")
scrool_b1.config(command=text1.yview)
text1.configure(yscrollcommand=scrool_b1.set)

# Output Box
combo2 = ttk.Combobox(root, values=language_list, font="Roboto 14", state="r")
combo2.place(x=730, y=20)
combo2.set("Select Language")

l2 = Label(root, text="ENGLISH", font="segoe 30 bold", width=18, bd=5, relief=GROOVE)
l2.place(x=620, y=50)

f2 = Frame(root, bg="Black", bd=5)
f2.place(x=620, y=118, width=440, height=210)

text2 = Text(f2, font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD)
text2.place(x=0, y=0, width=430, height=200)

scrool_b2 = Scrollbar(f2)
scrool_b2.pack(side=RIGHT, fill="y")
scrool_b2.config(command=text1.yview)
text2.configure(yscrollcommand=scrool_b2.set)

# Translate Button
b1 = Button(root, text="Translate", font="Roboto 15 italic bold", activebackground="blue", cursor="hand2", bd=5, bg="red", fg="white", command=Translate)
b1.place(x=480, y=250)
root.bind('<Return>', Enter)

label_change()

root.mainloop()