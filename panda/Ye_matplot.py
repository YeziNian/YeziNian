import matplotlib.pyplot as plt
import tkinter.messagebox
import numpy as np
import pandas as pd
import tkinter.filedialog
import tkinter
import tkinter.scrolledtext
name = 1
#print("{0} {1}".format(1, 2))
root = tkinter.Tk()
#print(tkinter.NO)
root.geometry("600x600")
ine = tkinter.IntVar(value=3)
def meme():
    yesno = tkinter.messagebox.askyesno(title="Yezi", message="Ok or Not?")
    if yesno:
        file = tkinter.filedialog.askopenfile(title="Open file", filetypes=[("Text files", "*.txt"), ("Python files", "*.py")])
        scor.insert(0.0, "".join(file.readlines()))
    else:
        print("No")
i = 1
def henahsu(event):
    global i
    scor.insert("%d.0" % i, "Hello Jack")
    i += 1
def ok(event):
    print(scor.get(0.0, tkinter.END))
scor = tkinter.scrolledtext.ScrolledText(root, wrap=tkinter.WORD)
scor.pack(fill=tkinter.BOTH, expand=tkinter.YES)
scor.bind("<Button - 1>", henahsu)
scor.bind("<Tab>", ok)
image = tkinter.PhotoImage(file=r"C:\Users\40437\Desktop\QQ浏览器截图20230518163701.png")
butto = tkinter.Button(root, text="Login", command=meme, image=image)
butto.pack()
lae =tkinter.Label(root, textvariable=ine)
lae.pack(expand=tkinter.YES, fill=tkinter.BOTH)
root.mainloop()