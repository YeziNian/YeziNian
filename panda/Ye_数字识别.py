import tkinter
import tkinter.filedialog
import tkinter.messagebox
from datetime import datetime
from tkinter import scrolledtext
import sys
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import time
from ttkthemes import ThemedStyle
from ttkbootstrap import Style
from tkinter import ttk
import threading
import ttkbootstrap
def GUI():
    #窗口属性
    root = tkinter.Tk()
    heitht = root.winfo_screenheight()
    width = root.winfo_screenwidth()
    root.geometry("800x600+{0}+{1}".format((width - 800) // 2, (heitht - 600) // 2))
    root.title("Yezi Rec")
    #对象构建
    style = ThemedStyle(root)
    print(style.get_themes())
    style.set_theme('smog')
    strvar = tkinter.StringVar(value="")
    label_file = tkinter.Label(root, text="文件地址:")
    label_file.place(x=20, y=20, height=40, width=60)
    entry_file = tkinter.Entry(root, textvariable=strvar)
    entry_file.place(x=80, y=30, height=20, width=300)
    def Open():
        name = tkinter.filedialog.askopenfilename(title="Yezi", filetypes=[("Photo types", "* .gif * .png")])
        strvar.set(name)
        entry_file["fg"] = "red"
    button_file = tkinter.Button(root, text="Open", command=Open)
    button_file.place(x=400, y=30, height=20, width=50)
    image = tkinter.PhotoImage()
    canva = tkinter.Canvas(root)
    canva.create_image(200, 200, image=image)
    canva.place(x=20, y=100, width=700, height=400)
    button = tkinter.Button(root, text="nihao")
    button.pack()
    root.mainloop()

def UI():
    style = Style(theme="darkly")
    name = style.theme_names()
    root = style.master
    root.geometry("200x200+700+200")
    root.title("ttkbootstrap widget demo")
    def chre(event):
        what = a.get()
        if what:
            style.theme_use(themename=what)
        else:
            pass
    de = tkinter.StringVar(value="")
    def change():
        while True:
            data = datetime.now()
            str1 = ""
            str1 += str(data.year)
            str1 += str(data.month)
            str1 += str(data.second)
            de.set(str1)
            time.sleep(0.3)
    mm = threading.Thread(target=change)
    mm.daemon = True
    mm.start()
    def tanchu():
        tkinter.messagebox.showinfo(title="Yezi", message=a.get())
    a = ttk.Combobox(root, values=tuple(name), width=30, height=30)

    ttk.Separator(root).pack()
    a.set("darkly")
    a.pack()
    a.bind("<<ComboboxSelected>>", chre)
    ok = ttk.Label(root, textvariable=de)
    ok.pack()
    frame = ttk.Frame(root)
    label = ttk.Label(frame, text="City")
    label1 = ttk.Label(frame, text="Rank")
    label.place(x=0, y=0, width=40, height=10)
    label1.place(x=70, y=0, width=40, height=10)
    frame.place(x=10, y=50, width=100, height=20)
    b = ttk.Label(root, text="你好撒旦")
    b.pack()
    p = tkinter.IntVar(value=0)
    c = ttk.Checkbutton(root, text="ok", variable=p, onvalue=1, offvalue=0)
    c.pack()
    d = ttk.Menubutton(root)
    d.pack()
    t = threading.Thread(target=chre)
    t.daemon = True
    ttk.Button(root, text="Submit", style="success.TButton", command=tanchu).pack(side="left", padx=5, pady=10)
    root.mainloop()

def hhe():
    root = tkinter.Tk()
    button = ttk.Button(root, text="ttk")
    button.pack()
    button1 = tkinter.Button(root, text="tkingter")
    button1.pack()
    root.mainloop()

def hehe():
    style = Style(theme="darkly")
    root = style.master
    root.geometry("200x200+600+300")
    root.title("hehe")
    frame = ttk.Frame(root, width=200, height=140, relief="sunken")
    label1 = ttk.Label(frame, text="City")
    label2 = ttk.Label(frame, text="Rank")
    label1.place(x=0, y=0, width=40, height=30)
    label2.place(x=160, y=0, width=40, height=30)
    listbox = tkinter.Listbox(frame)
    listbox.place(x=0, y=30, width=200, height=130)
    def add():
        top = tkinter.Toplevel(root, width=200, height=200)
        var = tkinter.StringVar(value="")
        var1 = tkinter.StringVar(value="")
        entry = ttk.Entry(top, textvariable=var)
        entry.pack()
        entry1 = ttk.Entry(top, textvariable=var1)
        entry1.pack()
        top.overrideredirect(True)
        def gai(event):
            if var and var1:
                listbox.insert(0, var.get()+"\t\t"+var1.get())
        top.bind("<KeyPress-w>", gai)
    button = ttk.Button(root, text="添加", command=add)
    button.place(x=80, y=170, width=50, height=30)
    listbox.insert(0, "South west 1")
    frame.pack()
    frame.pack_forget()
    print(frame.clipboard_get())
    root.mainloop()

def cizhi():
    style = Style(theme="litera")
    root = style.master
    root.title("Cizhi")
    root.geometry("300x300+550+260")
    frame1 = ttk.Frame(root, width=300, height=300)
    frame2 = ttk.Frame(root, width=300, height=300)
    label = ttk.Label(frame1, text="\tI w", justify=tkinter.LEFT, wraplength=100)
    label.pack()
    def button_1():
        sys.exit()
    def button_2():
        frame1.pack_forget()
    def thred(event):
        x = event.widget.winfo_pointerx()-root.winfo_x()
        y = event.widget.winfo_pointery()-root.winfo_y()-35
        print(x, y)
        if 190<=x<=240 and 180<=y<=220:
            button2.place(x=190, y=100, width=50, height=40)
        else:
            button2.place(x=190, y=180, width=50, height=40)
    def ixnashi(event):
        obje = event.widget
        print(obje)
    root.bind("<Motion>", ixnashi)
    button1 = ttk.Button(frame1, text="同意", command=button_1)
    button1.place(x=20, y=180, width=50, height=40)
    button2 = ttk.Button(frame1, text="反对", command=button_2)
    button2.place(x=190, y=180, width=50, height=40)
    button2.bind("<Motion>", thred)
    frame1.pack(fill=tkinter.BOTH, expand=tkinter.YES)
    #frame1.place(x=0, y=0, width=300, height=300)
    """    frame1.pack_forget()
    dd = scrolledtext.ScrolledText(root)
    dd.pack(fill=tkinter.BOTH, expand=True)
    dd.insert(0.0, "hehe")
    dd.delete(0.0, tkinter.END)"""
    root.mainloop()
"""root = tkinter.Tk()
bt = ttk.Button(root, text="he", underline=1)
bt.pack()
root.geometry("330x330")
ttk.Label(root, text="wode", image="0.jpg", compound="top").pack()
ttk.Scrollbar(root).pack(fill=ttkbootstrap.BOTH)
root.mainloop()"""
def mo():
    style = Style(theme="litera")
    root = style.master
    root.geometry("300x300")
    def jiance(event):
        try:
            widget = event.widget
            #print(widget)
            widget["padding"] = 20
            objc = widget.identify(event.x, event.y)
            print(widget.instate("NORMAL"))
            print(objc)
        except Exception:
            pass
    a = ttk.Button(root, text="OK")
    a.pack()
    #root.bind("<Motion>", jiance)
    com = ttk.Combobox(root, values=tuple(["1", "2", "3"]), state="readonly") #不能编辑
    com.pack()
    de = ttk.Spinbox(root, from_=0, to=100, increment=10, wrap=True, format="%4.2f", command=lambda: print(de.get()))
    de.pack()
    dee = ttk.Spinbox(root, values=["asd", "2", "3"])
    dee.pack()
    """
    虚拟事件
    用户若按下 <Up> ，则控件会生成 <<Increment>> 虚拟事件，若按下 <Down> 则会生成 <<Decrement>> 事件。
    command 是无论按下增加或减少都会调用"""

    note = ttk.Notebook(root, height=40, width=40, padding=[10, 10, 10, 10])
    note.enable_traversal()
    note.add(ttk.Button(note, text="Click"), text="__eew", underline=1)
    note.add(ttk.Button(note), text="eew")
    for tab in note.tabs():
        note.tab(tab, text="_ehew2")
        break
        #note.tab(tab, background="pink")
    note.bind("<Button-1>", lambda event: print(note.index("end")))
    note.bind("<Button-1>", lambda event: note.insert("end", ttk.Button(note, text="Hello")))
    note.bind("<Button-3>", lambda event: note.select(1))
    #note.option_add('*Notebook*Background', 'pink')
    note.pack()

    #进度条
    ine = tkinter.IntVar(value=0)
    progrss = ttk.Progressbar(root, orient="horizontal", maximum=100, variable=ine, mode="determinate", phase=1)
    #progrss.step(50)
    #progrss.start(10)
    def chc():
        for i in range(100):
            ine.set(i)
            time.sleep(0.3)
    kekek = threading.Thread(target=chc)
    kekek.daemon = True
    kekek.start()
    #progrss.stop()
    progrss.place(x=90, y=230)
    #lae = ttk.Label(root, textvariable=ine)
    #lae.place(x=90, y=230, width=40, height=20)
    #ttk.Separator(orient="horizontal")
    jj = ttk.Sizegrip(root)
    jj.pack()
    newtop = tkinter.Toplevel(root)

    tree = ttk.Treeview(newtop, selectmode="browse")
    # 添加列标题
    tree["columns"] = ("Name", "Age", "Gender")

    # 定义列的显示样式
    tree.column("#0", width=0, stretch="yes")
    tree.column("Name", width=100)
    tree.column("Age", width=100)
    tree.column("Gender", width=100)

    # 设置头部的标题
    tree.heading("#0", text="", anchor="w")
    tree.heading("Name", text="Name", anchor="center")
    tree.heading("Age", text="Age", anchor="center")
    tree.heading("Gender", text="Gender", anchor="center", command=lambda :print(123))

    # 添加数据项
    parent0 = tree.insert("", 0, text="Parent 0", open=True, tags=["pink", "blue"])
    parent1 = tree.insert("", 1, text="Parent 1")
    print(parent0)
    photo = tkinter.PhotoImage(file=r"C:\Users\40437\Desktop\aa.png", height=10, width=10)
    child0_0 = tree.insert(parent0, 0, text="Child 0-1", values=("Alice", 25, photo))
    child0_1 = tree.insert(parent0, 0, text="Child 0-0", values=("Bob", 32, "Male"))
    child1_0 = tree.insert(parent0, 0, text="Child 0-4", values=("Carol", 18, "Female"))
    def hee(event):
        print(1, tree.get_children(parent0))
        tree.focus(child0_1)
    tree.bind("<<TreeviewSelect>>", hee)
    # 显示Treeview小部件
    tree.pack()
    root.mainloop()
mo()