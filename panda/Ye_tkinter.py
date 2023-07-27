import os
import tkinter
import tkinter.messagebox
import tkinter.filedialog
import tkinter.colorchooser
import tkinter.scrolledtext
import tkinter.ttk
import tkinter.simpledialog
import threading
import time
import datetime
import turtle
from PIL import ImageGrab
from PIL import Image
def Logi():
    root = tkinter.Tk()
    root["height"] = 200
    root["width"] = 200
    nameVar = tkinter.StringVar()
    nameVar.set("")
    pwdVar = tkinter.StringVar()
    pwdVar.set("")

    label = tkinter.Label(root, text="admin:", justify=tkinter.RIGHT, fg="red", bg="yellow") #wraplength换行宽度 justify=末行对齐方式) fo汉字颜色，bg背景颜色
    label.place(x=20, y=10, height=40, width=40)

    label1 = tkinter.Label(root, text="pwd:", justify=tkinter.RIGHT)
    label1.place(x=20, y=50, height=20, width=40)

    Adentry = tkinter.Entry(root, textvariable=nameVar)
    Adentry.place(x=70, y=10, height=20, width=80)

    Pwentry = tkinter.Entry(root, textvariable=pwdVar, show="*")
    Pwentry.place(x=70, y=50, height=20, width=80)

    def jiance():
        a = nameVar.get()
        b = pwdVar.get()
        if a == b:
            tkinter.messagebox.showinfo(title="Yezi", message="Ok!")
        else:
            tkinter.messagebox.showerror(title="Yezi", message="Wrong!")
    button = tkinter.Button(root, text="Login", command=jiance)
    button.place(x=70, y=100, height=20, width=40)

    root.mainloop()

def Xuanze():
    root = tkinter.Tk()
    heitht = root.winfo_screenheight()
    width = root.winfo_screenwidth()
    root.geometry("320x400+{0}+{1}".format((width-320)//2, (heitht-400)//2))
    root.title("Selection widgets")
    #变量
    varname = tkinter.StringVar()
    varname.set("")
    labelname = tkinter.Label(root, text="name", justify=tkinter.RIGHT, width=50)
    labelname.place(x=10, y=5, width=50, height=20)
    entryname = tkinter.Entry(root, textvariable=varname, width=120)
    entryname.place(x=70, y=5, width=120, height=20)
    labelgarde = tkinter.Label(root, text="Grade:", justify=tkinter.RIGHT, width=50)
    labelgarde.place(x=10, y=40, width=50, height=20)
    Studenclass = {"1": ["1", "2", "3"],
                   "2": ["1", "2"],
                   "3": ["1", "2", "3", "4"]}
    #组合框
    comboGrade = tkinter.ttk.Combobox(root, width=50, values=tuple(Studenclass.keys()))
    comboGrade.place(x=70, y=40, width=50, height=20)
    def commo(event):
        grade = comboGrade.get()
        if grade:
            comboclass["values"] = Studenclass.get(grade)
        else:
            comboclass.set([])
    comboGrade.bind("<<ComboboxSelected>>", commo)
    labelclass = tkinter.Label(root, text="Class:", justify=tkinter.RIGHT, width=50)
    labelclass.place(x=130, y=40, width=50, height=20)
    comboclass = tkinter.ttk.Combobox(root, width=50)
    comboclass.place(x=190, y=40, width=50, height=20)

    labelsex = tkinter.Label(root, text="sex:")
    labelsex.place(x=10, y=70, width=50, height=20)
    #1 为男 2 为女
    sex = tkinter.IntVar()
    sex.set(1)
    radioMan = tkinter.Radiobutton(root, variable=sex, value=1, text="Man")
    radioMan.place(x=70, y=70, width=50, height=20)
    radiowoMan = tkinter.Radiobutton(root, variable=sex, value=0, text="Woman")
    radiowoMan.place(x=130, y=70, width=70, height=20)
    monitor = tkinter.IntVar()
    monitor.set(0)
    check = tkinter.Checkbutton(root, text="Is monitor?", variable=monitor, onvalue=1, offvalue=0)
    check.place(x=20, y=100, width=100, height=20)
    def Add():
        if entryname.get() and comboclass.get() and comboGrade.get():
            result = "Name:" + entryname.get()
            result += ";Grade," + comboGrade.get()
            result += ";Class," + comboclass.get()
            result += ";Sex," + ("Man" if sex.get() else "Woman")
            result += ";Monitor." + ("Yes" if monitor.get() else "No")
            listbox.insert(0, result)
        else:
            tkinter.messagebox.showerror(title="Yezi", message="Exist empty!")
    button = tkinter.Button(root, text="ADD", command=Add)
    button.place(x=130, y=100, width=40, height=20)
    def deletee():
        selc =listbox.curselection()
        if not selc:
            tkinter.messagebox.showinfo(title="Yezi", message="No Seletion!")
        else:
            listbox.delete(selc)
    buttonDe = tkinter.Button(root, text="Delete", command=deletee)
    buttonDe.place(x=180, y=100, width=100, height=20)
    listbox = tkinter.Listbox(root, width=300)
    listbox.place(x=10, y=130, width=300, height=200)
    def Xie():
        book = listbox.curselection()
        if not book:
            tkinter.messagebox.showerror(title="Yezi", message="No selected!")
        else:
            if not os.path.exists("pe.txt"):
                with open("pe.txt", "w") as fp:
                     pass
            with open("pe.txt", "a") as fp:
                fp.write(listbox.get(book) + "\n")
            tkinter.messagebox.showinfo(title="Yezi", message="Ok!")
    newbutton = tkinter.Button(root, text="保存", command=Xie)
    newbutton.place(x=140, y=340, width=40, height=30)
    root.mainloop()
    with open("pe.txt", "w") as fp:
        pass

def Wenben():
    root = tkinter.Tk()
    heitht = root.winfo_screenheight()
    width = root.winfo_screenwidth()
    root.geometry("800x600+{0}+{1}".format((width - 800) // 2, (heitht - 600) // 2))
    root.title("Yezi notepad")

    textChange = tkinter.IntVar(value=0)
    filename = ""

    #创建菜单
    menu = tkinter.Menu(root)
    #File菜单
    submenu = tkinter.Menu(menu, tearoff=0) #不设置会出现虚线 独立出一个窗口
    def Open():
        global filename
        if textChange.get():
            yesno = tkinter.messagebox.askyesno(title="Save or not?", message="Do you want to save?")  #确认和否定
            if yesno == tkinter.YES:
                Save()
        filename = tkinter.filedialog.askopenfilename(title="Open file", filetypes=[("Text files", "*.txt")])
        """
        tkinter.filedialog.asksaveasfilename():选择以什么文件名保存，返回文件名
        tkinter.filedialog.asksaveasfile():选择以什么文件保存，创建文件并返回文件流对象
        tkinter.filedialog.askopenfilename():选择打开什么文件，返回文件名
        tkinter.filedialog.askopenfile():选择打开什么文件，返回IO流对象
        tkinter.filedialog.askdirectory():选择目录，返回目录名
        tkinter.filedialog.askopenfilenames():选择打开多个文件，以元组形式返回多个文件名
        tkinter.filedialog.askopenfiles():选择打开多个文件，以列表形式返回多个IO流对   
        """
        if filename:
            #清空内容, 0.0是lineNumber.Column的表示方法
            textContent.delete(0.0, tkinter.END)
            fp = open(filename, "r")
            textContent.insert(tkinter.INSERT, "".join(fp.readlines()))
            fp.close()
            textChange.set(0)
    submenu.add_command(label='open', command=Open)
    def Save():
        global filename
        if not filename:
            SaveAs()
        elif textChange.get():
            with open(filename, "w") as fp:
                fp.write(textContent.get(0.0, tkinter.END))
            textChange.set(0)
    submenu.add_command(label="Save", command=Save)
    def SaveAs():
        global filename
        #打开另存为窗口
        newfilename = tkinter.filedialog.asksaveasfilename(title="Sava as", initialdir=r"c:\\", initialfile="new.txt")
        if newfilename:
            with open(newfilename, "w") as fp:
                fp.write(textContent.get(0.0, tkinter.END))
            filename = newfilename
            textChange.set(0)
    submenu.add_command(label="Save as", command=SaveAs)
    #添加分割线
    submenu.add_separator()
    def Close():
        global filename
        Save()
        textContent.delete(0.0, tkinter.END)
        filename = ""

    submenu.add_command(label="Close", command=Close)

    menu.add_cascade(label="File", menu=submenu)

    #Edit 菜单
    submenu = tkinter.Menu(menu, tearoff=0)
    def Undo():
        textContent["undo"] = True
        try:
            textContent.edit_undo()
        except Exception as e:
            pass
    submenu.add_command(label="Undo", command=Undo)
    def Redo():
        textContent["undo"] = True
        try:
            textContent.edit_redo()
        except Exception as f:
            pass
    submenu.add_command(label="Redo", command=Redo)
    submenu.add_separator()

    def Copy():
        textContent.clipboard_clear()
        textContent.clipboard_append(textContent.selection_get())
    submenu.add_command(label="Copy", command=Copy)
    def Cut():
        Copy()
        textContent.delete(tkinter.SEL_FIRST, tkinter.SEL_LAST)
    submenu.add_command(label="Cut", command=Cut)
    def Paste():
        try:
            textContent.insert(tkinter.SEL_FIRST, textContent.clipboard_get())
            textContent.delete(tkinter.SEL_FIRST, tkinter.SEL_LAST)  #######################
            return
        except Exception as fp:
            pass
        textContent.insert(tkinter.INSERT, textContent.clipboard_get())
    submenu.add_command(label="Paste", command=Paste)
    submenu.add_separator()
    def Search():
        textTosearch = tkinter.simpledialog.askstring(title="Search", prompt="What to search?")
        start = textContent.search(textTosearch, 0.0, tkinter.END)
        if start:
            tkinter.messagebox.showinfo(title="Yezi", message="Ok")
    submenu.add_command(label="Search", command=Search)
    menu.add_cascade(label="Xiaoxi", menu=submenu)

    submenu = tkinter.Menu(menu, tearoff=0)
    def About():
        tkinter.messagebox.showinfo(title="About", message="Author Yezi")
    submenu.add_command(label="About", command=About)
    menu.add_cascade(label="Help", menu=submenu)

    root.config(menu=menu)
    textContent = tkinter.scrolledtext.ScrolledText(root, wrap=tkinter.WORD)
    textContent.pack(fill=tkinter.BOTH, expand=tkinter.YES)
    #root.resizable(False, False)
    def Key(event):
        textChange.set(1)
    textContent.bind("<KeyPress>", Key)
    """
    < Button - 1 >: 鼠标左键单击事件
    < ButtonRelease - 1 >: 鼠标左键释放事件
    < Button - 2 >: 鼠标中键单击事件
    < ButtonRelease - 2 >: 鼠标中键释放事件
    < Button - 3 >: 鼠标右键单击事件
    < ButtonRelease - 3 >: 鼠标右键释放事件
    < KeyPress >: 键盘按键事件（按下按键）
    < KeyRelease >: 键盘按键事件（释放按键）
    < Return > 或 < Enter >: 键盘回车键事件
    < Tab >: 键盘Tab键事件
    < BackSpace >: 键盘后退键事件
    < Delete >: 键盘删除键事件
    < MouseWheel >：鼠标滚轮事件，"""
    root.mainloop()

def clock():
    lastDraw = 0
    root = tkinter.Tk()
    heitht = root.winfo_screenheight()
    width = root.winfo_screenwidth()
    root.geometry("800x600+{0}+{1}".format((width - 800) // 2, (heitht - 600) // 2))
    root.title("Yezi Canvas")
    root.resizable(False, False)
    yesno = tkinter.IntVar(value=0)
    what = tkinter.IntVar(value=1) #1为曲线 2为直线 3为矩形 4为文本 5为橡皮

    X = tkinter.IntVar(value=0)
    Y = tkinter.IntVar(value=0)

    #前景色
    foreColor = "#000000"
    backColor = "#FFFFFF"
    #创建画布
    image = tkinter.PhotoImage()
    canva = tkinter.Canvas(root, bg="white", width=800, height=600)
    #canva.pack(fill=tkinter.BOTH, expand=tkinter.YES)
    canva.create_image(800, 600, image=image)
    def Onle(event):
        yesno.set(1)
        X.set(event.x)
        Y.set(event.y)
        if what.get() == 4:
            canva.create_text(event.x, event.y, text=text)
    canva.bind("<Button-1>", Onle)
    def He(event):
       # canva.itemconfigure(canva.create_line(), tags=("shape", "wro")) 修改对象的标签 可以使用 canvas.delete("shape")删除
        global lastDraw
        if yesno.get() == 0:
            return
        if what.get() == 1:
            canva.create_line(X.get(), Y.get(), event.x, event.y, fill=foreColor)
            X.set(event.x)
            Y.set(event.y)
        elif what.get() == 2:
            try:
                canva.delete(lastDraw)
            except Exception as pes:
                pass
            lastDraw = canva.create_line(X.get(), Y.get(), event.x, event.y, fill="blue") #dash(20, 10)为虚线 width=5
        elif what.get() == 3:
            try:
                canva.delete(lastDraw)
            except Exception as m:
                pass
            lastDraw = canva.create_rectangle(X.get(), Y.get(), event.x, event.y, fill=backColor, outline=foreColor)
        elif what.get() == 5:
            canva.create_rectangle(event.x-5, event.y-5, event.x+5, event.y+5, outline=backColor, fill=backColor)
    canva.bind("<B1-Motion>", He)  #按住鼠标左键移动

    def ui(event):
        if what.get() == 2:
            canva.create_line(X.get(), Y.get(), event.x, event.y, fill="blue")
        elif what.get() == 3:
            canva.create_rectangle(X.get(), Y.get(), event.x, event.y, fill=backColor, outline=foreColor)
        yesno.set(0)
        global lastDraw
        lastDraw = 0
    canva.bind("<ButtonRelease-1>", ui)

    menu = tkinter.Menu(root, tearoff=0)
    def Open():
        filename = tkinter.filedialog.askopenfilename(title="Yezi", filetypes=[("image", "* .jpg * .png * .gif")])
        if filename:
            global image
            image = tkinter.PhotoImage(file=filename)
            canva.create_image(80, 80, image=image)
    menu.add_command(label="Open", command=Open)
    def Clear():
        for item in canva.find_all():
            canva.delete(item)
    menu.add_command(label="Close", command=Clear)
    menu.add_separator()
    menutype = tkinter.Menu(menu, tearoff=0)
    def drawCurve():
        what.set(1)
    menutype.add_command(label="Curve", command=drawCurve)
    def drawline():
        what.set(2)
    menutype.add_command(label="Line", command=drawline)
    def drawRec():
        what.set(3)
    menutype.add_command(label="Rec", command=drawRec)
    def drawText():
        global text
        text = tkinter.simpledialog.askstring(title="Input what you wang to draw", prompt="")
        what.set(4)
    menutype.add_command(label="Text", command=drawText)
    menutype.add_separator()
    menu.add_cascade(label="Type", menu=menutype)
    def On(event):
        menu.post(event.x_root, event.y_root)
    canva.bind("<ButtonRelease-3>", On)
    canva.pack(fill=tkinter.BOTH, expand=tkinter.YES)
    root.mainloop()

def autu():
    root = tkinter.Tk()
    heitht = root.winfo_screenheight()
    width = root.winfo_screenwidth()
    #root.geometry("320x400+{0}+{1}".format((width - 320) // 2, (heitht - 400) // 2))
    root.title("Auto clock")
    root.overrideredirect(True) #不显示标题栏
    root.attributes("-alpha", 0.9) #设置透明度
    root.attributes("-topmost", 1) #窗口总是在窗口上面弹出
    root.geometry("110x25+100+100")
    labelDatetime = tkinter.Label(root)
    labelDatetime.pack(fill=tkinter.BOTH, expand=tkinter.YES)
    labelDatetime.configure(bg="gray")
    X = tkinter.IntVar(value=0)
    Y = tkinter.IntVar(value=0)
    #表示窗口是否可以拖动
    canMove = tkinter.IntVar(value=0)
    #表示是否仍在运行的变量
    still = tkinter.IntVar(value=1)
    def Onleft(event):
        #开始时增加透明度
        root.attributes("-alpha", 0.4)
        X.set(event.x)
        Y.set(event.y)
        canMove.set(1)
    labelDatetime.bind("<Button-1>", Onleft)
    def Onmove(event):
        root.attributes("-alpha", 0.9)
        canMove.set(0)
    labelDatetime.bind("<ButtonRelease-1>", Onmove)

    def He(event):
        if canMove.get() == 0:
            return
        newX = root.winfo_x() + (event.x-X.get())
        newY = root.winfo_y() + (event.y-Y.get())
        g = "110x25+" + str(newX) + "+" + str(newY)
        root.geometry(g)
    labelDatetime.bind("<B1-Motion>", He)

    def Onright(event):
        still.set(0)
        t.join(0.2)
        root.destroy()
    labelDatetime.bind("<Button-3>", Onright)

    def nowtime():
        while still.get() == 1:
            now = datetime.datetime.now()
            s = str(now.year) + "-" + str(now.month) + "-" + str(now.day) + " "
            s += str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)
            labelDatetime["text"] = s
            time.sleep(0.2)
    t = threading.Thread(target=nowtime)
    t.daemon = True
    t.start()
    root.mainloop()

def Motion():
    root = tkinter.Tk()
    heitht = root.winfo_screenheight()
    width = root.winfo_screenwidth()
    #print(heitht, width)
    root.geometry("800x600+{0}+{1}".format((width - 800) // 2, (heitht - 600) // 2))
    root.title("Motion")
    canva = tkinter.Canvas(root, bg="white", width=800, height=600)
    image = tkinter.PhotoImage(file=r"C:\Users\40437\Desktop\AA.png")
    id_actor = canva.create_image(0, 0, image=image, anchor=tkinter.NW) #默认为图片中心点 现在改为左上角
    flag = False
    X = tkinter.IntVar(value=0)
    Y = tkinter.IntVar(value=0)
    def Onleft(event):
        global flag
        X.set(event.x)
        Y.set(event.y)
        flag = True
        """while flag:
            canva.move(id_actor, 5, 0)
            canva.update()
            time.sleep(0.05)"""
    canva.bind("<Button-1>", Onleft)
    def move_still(event):
        delta_x = event.x - X.get()
        delta_y = event.y - Y.get()
        canva.move(id_actor, delta_x, delta_y)
        canva.update()
        X.set(event.x)
        Y.set(event.y)
    canva.bind("<B1-Motion>", move_still)
    #def cer(event):
       # X.set(event.x)
        #Y.set(event.y)
    #canva.bind("<ButtonRelease-1>", cer)
    def OnRight(event):
        global flag
        flag = False
        root.destroy()
    canva.bind("<ButtonRelease-3>", OnRight)
    def Keycontrol(event):
        if event.keysym == "Up":
            canva.move(id_actor, 0, -5)
            canva.update()
        if event.keysym == "Down":
            canva.move(id_actor, 0, 5)
            canva.update()
        if event.keysym == "Left":
            canva.move(id_actor, -5, 0)
            canva.update()
        if event.keysym == "Right":
            canva.move(id_actor, 5, 0)
            canva.update()
    canva.bind_all("<KeyPress-Up>", Keycontrol)
    canva.bind_all("<KeyPress-Down>", Keycontrol)
    canva.bind_all("<KeyPress-Left>", Keycontrol)
    canva.bind_all("<KeyPress-Right>", Keycontrol)
    canva.pack(fill=tkinter.BOTH, expand=tkinter.YES)
    canva.focus()
    root.mainloop()

def donghua():
    t = turtle.Pen()
    t.color(1, 0, 0)
    t.up()
    t.backward(280)
    t.left(90)
    t.forward(100)
    t.right(90)
    t.down()
    for i in range(4):
        t.forward(150)
        t.left(90)

    t.color(0, 0, 0)
    t.up()
    t.forward(200)
    t.down()
    for i in range(3):
        t.forward(200)
        t.left(120)

    t.up()
    t.forward(100)
    t.down()
    t.fillcolor(1, 0.6, 0.3)
    t.begin_fill()
    t.circle(50)
    t.end_fill()
    t.up()
    t.forward(120)
    t.left(90)
    t.forward(90)
    t.right(90)
    t.down()
    t.width(3)
    t.fillcolor(0, 0.6, 0.8)
    t.begin_fill()
    for i in range(5):
        t.forward(150)
        t.right(144)
    t.end_fill()

    t.up()
    t.backward(270)
    t.right(90)
    t.forward(150)
    t.write("Yezi", font=("隶书", 16, "normal"))
    t.forward(10)
    t.left(90)
    t.width(1)
    t.down()
    t.forward(350)

def Manyui():

    class Mywindow:

        def __init__(self, root, myTitle, flag):
            self.top = tkinter.Toplevel(root, width=300, height=200)
            self.top.title(myTitle)
            self.top.attributes("-topmost", 1)
            if flag == 1:
                label = tkinter.Label(self.top, text=myTitle)
                label.place(x=50, y=50)
            elif flag == 2:
                def buttonOk():
                    tkinter.messagebox.showinfo(title="Yezi", message="Hello Iack!")
                button = tkinter.Button(self.top, text=myTitle, command=buttonOk)
                button.place(x=50, y=50)
    root = tkinter.Tk()
    root.config(width=400)
    root.config(height=200)
    root.title("Mutiple Windows Demo!")
    window1 = tkinter.IntVar(root, value=0)
    window2 = tkinter.IntVar(root, value=0)
    def buttonClick():
        if window1.get() == 0:
            window1.set(1)
            w1 = Mywindow(root, "First window", 1)
            button1.wait_window(w1.top)
            window1.set(0)
    button1 = tkinter.Button(root, text="First window", command=buttonClick)
    button1.place(x=70, y=40, height=40, width=200)
    def buttonClick1():
        if window2.get() == 0:
            window2.set(1)
            w1 = Mywindow(root, "Second window", 2)
            button2.wait_window(w1.top)
            window2.set(0)
    button2 = tkinter.Button(root, text="Second window", command=buttonClick1)
    button2.place(x=70, y=40, height=40, width=200)
    root.mainloop()

def Jietu():

    root = tkinter.Tk()
    root.geometry("100x40+400+300")
    root.resizable(False, False)
    root.title("Yezi")

    class Mycapature:

        def __init__(self, png):
            self.X = tkinter.IntVar(value=0)
            self.Y = tkinter.IntVar(value=0)
            screenWidth = root.winfo_screenwidth()
            screenHeitht = root.winfo_screenheight()
            self.top = tkinter.Toplevel(root, width=screenWidth, height=screenHeitht)
            self.top.overrideredirect(True)
            self.canvas = tkinter.Canvas(self.top, bg="white", width=screenWidth, height=screenHeitht)
            self.image = tkinter.PhotoImage(file=png)
            self.canvas.create_image(screenWidth//2, screenHeitht//2, image=self.image)
            self.sel = True
            def Onlef(event):
                self.X.set(event.x)
                self.Y.set(event.y)
                self.sel = True
            self.canvas.bind("<Button-1>", Onlef)
            def oN(event):
                if not self.sel:
                    return
                global lastDraw
                try:
                    self.canvas.delete(lastDraw)
                except Exception as fp:
                    pass
                lastDraw = self.canvas.create_rectangle(self.X.get(), self.Y.get(), event.x, event.y, outline="black")
            self.canvas.bind("<B1-Motion>", oN)

            def he(event):
                self.sel = False
                try:
                    self.canvas.delete(lastDraw)
                except Exception as fp:
                    pass
                time.sleep(0.1)
                left, right = sorted([self.X.get(), event.x])
                top, bottom = sorted([self.Y.get(), event.y])
                pic = ImageGrab.grab((left+1, top+1, right, bottom))
                fileName = tkinter.filedialog.asksaveasfilename(title="保存截图", filetypes=[("image", "* .jpg * .png")])
                if fileName:
                    pic.save(fileName)
                self.top.destroy()
            self.canvas.bind("<ButtonRelease-1>", he)
            self.canvas.pack(fill=tkinter.BOTH, expand=tkinter.YES)
    def cc():
        root.state("icon")
        time.sleep(0.2)
        filename = "temp.png"
        im = ImageGrab.grab()
        im.save(filename)
        im.close()
        w = Mycapature(filename)
        bu.wait_window(w.top)
        root.state("normal")
        os.remove(filename)
    bu = tkinter.Button(root, text="截图", command=cc)
    bu.place(x=10, y=10, width=80, height=20)

    root.mainloop()


def bofang():
    import pygame
    import random
    floder = ""
    def play():
        musics = [music for music in os.listdir()\
                  if music.endswith((".mp3", ".wav", ".pgg"))]
        print(musics)
        total = len(musics)
        #初始化混音器设备
        pygame.mixer.init()
        playing = True
        while playing:
            if not pygame.mixer.get_busy():
                nextMusic = random.choice(musics)
                pygame.mixer.music.load(nextMusic.encode())
                pygame.mixer.music.play(1)
                musicName.set("Playing..." + nextMusic)
            else:
                time.sleep(0.3)
    root = tkinter.Tk()
    root.title("Yezi")
    root.geometry("280x70+400+300")
    root.resizable(False, False)

    def Close():
        global playing
        playing = False
        try:
            pygame.mixer.music.stop()
            pygame.mixer.quit()
        except:
            pass
        root.destroy()
    root.protocol("WM_DELETE_WINDOW", Close)
    pause_resume = tkinter.StringVar(root, value="NotSet")
    playing = False
    def buttonPly():
        global playing
        playing = True
        t = threading.Thread(target=play)
        t.start()
        buttonPlay["state"] = "disabled"
        buttonStop["state"] = "normal"
        pause_resume.set("Pause")
    buttonPlay = tkinter.Button(root, text="Play", command=buttonPly)
    buttonPlay.place(x=20, y=10, width=50, height=20)

    def buttonstop():
        global playing
        playing = False
        pygame.mixer.music.stop()
        musicName.set("暂时没有播放音乐!")
        buttonPlay["state"] = "normal"
        buttonStop["state"] = "disabled"

    buttonStop = tkinter.Button(root, text="Stop", textvariable=pause_resume, command=buttonstop)
    buttonStop.place(x=80, y=10, width=50, height=20)
    buttonStop["state"] = "disabled"

    musicName = tkinter.StringVar(root, value="暂时没有音乐!")
    labelName = tkinter.Label(root, textvariable=musicName)
    labelName.place(x=0, y=40, width=270, height=20)
    root.mainloop()