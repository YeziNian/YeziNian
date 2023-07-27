import tkinter
import threading
import tkinter.ttk
import os
root = tkinter.Tk()
import tkinter.messagebox

class My_top:

    def __init__(self, root):
        self.root = root
        self.top = tkinter.Toplevel(self.root)
        self.top.resizable(False, False)
        self.top.geometry("320x400")
        self.top.title("Yezi")
        # 变量
        self.varname = tkinter.StringVar()
        self.varname.set("")
        self.labelname = tkinter.Label(self.top, text="name", justify=tkinter.RIGHT, width=50)
        self.labelname.place(x=10, y=5, width=50, height=20)
        self.entryname = tkinter.Entry(self.top, textvariable=self.varname, width=120)
        self.entryname.place(x=70, y=5, width=120, height=20)
        self.labelgarde = tkinter.Label(self.top, text="Grade:", justify=tkinter.RIGHT, width=50)
        self.labelgarde.place(x=10, y=40, width=50, height=20)
        self.Studenclass = {"1": ["1", "2", "3"],
                       "2": ["1", "2"],
                       "3": ["1", "2", "3", "4"]}
        # 组合框
        self.comboGrade = tkinter.ttk.Combobox(self.top, width=50, values=tuple(self.Studenclass.keys()))
        self.comboGrade.place(x=70, y=40, width=50, height=20)

        def commo(event):
            grade = self.comboGrade.get()
            if grade:
                self.comboclass["values"] = self.Studenclass.get(grade)
            else:
                self.comboclass.set([])

        self.comboGrade.bind("<<ComboboxSelected>>", commo)
        self.labelclass = tkinter.Label(self.top, text="Class:", justify=tkinter.RIGHT, width=50)
        self.labelclass.place(x=130, y=40, width=50, height=20)
        self.comboclass = tkinter.ttk.Combobox(self.top, width=50)
        self.comboclass.place(x=190, y=40, width=50, height=20)

        self.labelsex = tkinter.Label(self.top, text="sex:")
        self.labelsex.place(x=10, y=70, width=50, height=20)
        # 1 为男 2 为女
        self.sex = tkinter.IntVar()
        self.sex.set(1)
        self.radioMan = tkinter.Radiobutton(self.top, variable=self.sex, value=1, text="Man")
        self.radioMan.place(x=70, y=70, width=50, height=20)
        self.radiowoMan = tkinter.Radiobutton(self.top, variable=self.sex, value=0, text="Woman")
        self.radiowoMan.place(x=130, y=70, width=70, height=20)
        self.monitor = tkinter.IntVar()
        self.monitor.set(0)
        self.check = tkinter.Checkbutton(self.top, text="Is monitor?", variable=self.monitor, onvalue=1, offvalue=0)
        self.check.place(x=20, y=100, width=100, height=20)

        def Add():
            if self.entryname.get() and self.comboclass.get() and self.comboGrade.get():
                result = "Name:" + self.entryname.get()
                result += ";Grade," + self.comboGrade.get()
                result += ";Class," + self.comboclass.get()
                result += ";Sex," + ("Man" if self.sex.get() else "Woman")
                result += ";Monitor." + ("Yes" if self.monitor.get() else "No")
                self.listbox.insert(0, result)
            else:
                tkinter.messagebox.showerror(title="Yezi", message="Exist empty!")

        self.button = tkinter.Button(self.top, text="ADD", command=Add)
        self.button.place(x=130, y=100, width=40, height=20)

        def deletee():
            selc = self.listbox.curselection()
            if not selc:
                tkinter.messagebox.showinfo(title="Yezi", message="No Seletion!")
            else:
                self.listbox.delete(selc)

        self.buttonDe = tkinter.Button(self.top, text="Delete", command=deletee)
        self.buttonDe.place(x=180, y=100, width=100, height=20)
        self.listbox = tkinter.Listbox(self.top, width=300)
        self.listbox.place(x=10, y=130, width=300, height=200)
        def Xie():
            book = self.listbox.curselection()
            if not book:
                tkinter.messagebox.showerror(title="Yezi", message="No selected!")
            else:
                if not os.path.exists("pe.txt"):
                    with open("pe.txt", "w") as fp:
                        pass
                with open("pe.txt", "a") as fp:
                    fp.write(self.listbox.get(book) + "\n")
                tkinter.messagebox.showinfo(title="Yezi", message="Ok!")

        self.newbutton = tkinter.Button(self.top, text="保存", command=Xie)
        self.newbutton.place(x=140, y=340, width=40, height=30)

class my(threading.Thread):
    def __init__(self, root):
        threading.Thread.__init__(self)
        self.root = root
    def run(self):
        self.top = tkinter.Toplevel(self.root)
        self.top.resizable(False, False)
        self.top.geometry("400x400")
        self.top.title("Yezi")
        while True:
            pass
image = tkinter.PhotoImage(file=r"C:\Users\40437\Desktop\QQ浏览器截图20230530214903.png")
label = tkinter.Label(root, image=image)
root.attributes("-alpha", 1)
label.place(relwidth=1, relheight=1)
button = tkinter.Button(root, text="呵呵呵阿斯顿a")
button.place(x=20, y=33, width=50, height=101)

button.configure(bg=label['bg'],
                fg=label['bg'],
                highlightthickness=0,
                highlightbackground=label['bg'])


"""t = my(root)
t.daemon = False
t.start()"""
My_top(root)
root.mainloop()