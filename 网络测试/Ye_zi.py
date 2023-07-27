import threading
import socket
import tkinter
import re
import time
import datetime
import tkinter.messagebox
import tkinter.filedialog
import tkinter.ttk
import os
ip = socket.gethostbyname(socket.gethostname())
port = 51259
T_addr = (ip, port)

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

def UI():

    root = tkinter.Tk()
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    #image = tkinter.PhotoImage(file=r"C:\Users\40437\Desktop\QQ浏览器截图20230530214903.png")
    label = tkinter.Label(root)
    root.attributes("-alpha", 0.8)
    label.place(relwidth=1, relheight=1)
    root.title("Yezi")
    root.geometry("270x270+{0}+{1}".format((width-270)//2, (height-270)//2))
    admin = tkinter.StringVar(value="")
    pwd = tkinter.StringVar(value="")
    label_admin = tkinter.Label(root, text="admin:")
    label_admin.place(x=20, y=20, width=40, height=40)
    label_pwd = tkinter.Label(root, text="pwd:")
    label_pwd.place(x=20, y=60, width=40, height=40)
    entry_admin = tkinter.Entry(root, textvariable=admin)
    entry_admin.place(x=70, y=30, height=20, width=110)
    entry_pwd = tkinter.Entry(root, textvariable=pwd, show="*")
    entry_pwd.place(x=70, y=70, height=20, width=110)
    check = tkinter.IntVar(value=0)
    check_button = tkinter.Checkbutton(root, variable=check, onvalue=1, offvalue=0)
    check_label = tkinter.Label(root, text="显示密码")
    check_label.place(x=210, y=70, height=20, width=50)
    check_button.place(x=180, y=70, height=20, width=40)
    Button_admin = tkinter.Button(root, text="登录")
    Button_admin.place(x=60, y=120, height=30, width=40)
    Button_pwd = tkinter.Button(root, text="注册")
    Button_pwd.place(x=160, y=120, height=30, width=40)
    time_label = tkinter.Label(root)
    time_label.place(x=120, y=240, height=40, width=140)
    menu = tkinter.Menu(root, tearoff=0)
    zhuce_admin = tkinter.StringVar(value="")
    zhuce_pwd = tkinter.StringVar(value="")
    zhuce_re_pwd = tkinter.StringVar(value="")
    top_checked = tkinter.IntVar(value=0)
    def zhuce():
        root.state("iconic")
        pattern = r"[\u4e00-\u9fa5]"
        Button_pwd["state"] = "disabled"
        Button_admin["state"] = "disabled"
        top = tkinter.Toplevel(root)
        top.resizable(False, False)
        top.title("Yezi")
        top.geometry("260x260+{0}+{1}".format((width-260)//2, (height-260)//2))
        top_label_admin = tkinter.Label(top, text="admin:")
        top_label_admin.place(x=20, y=20, width=40, height=40)
        top_label_pwd = tkinter.Label(top, text="pwd:")
        top_label_pwd.place(x=20, y=60, width=40, height=40)
        top_label_re = tkinter.Label(top, text="Re_pwd:")
        top_label_re.place(x=15, y=100, width=50, height=40)
        top_label_mima = tkinter.Label(top, text="显示密码")
        top_label_mima.place(x=200, y=110, width=50, height=20)
        top_check = tkinter.Checkbutton(top, variable=top_checked, onvalue=1, offvalue=0)
        top_check.place(x=180, y=110, width=20, height=20)

        top_entry_admin = tkinter.Entry(top, textvariable=zhuce_admin)
        top_entry_pwd = tkinter.Entry(top, textvariable=zhuce_pwd, show="*")
        top_entry_repwd = tkinter.Entry(top, textvariable=zhuce_re_pwd, show="*")

        top_entry_admin.place(x=70, y=30, width=100, height=20)
        top_entry_pwd.place(x=70, y=70, width=100, height=20)
        top_entry_repwd.place(x=70, y=110, width=100, height=20)

        top_Button = tkinter.Button(top, text="注册")
        top_Button.place(x=100, y=160, width=40, height=30)
        check_run = 1

        def register():
            top_Button["state"] = "disabled"
            soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            pattern1 = r"^[!@#$%^&*()_+]"
            admin = zhuce_admin.get()
            pwd = zhuce_pwd.get()
            repwd = zhuce_re_pwd.get()
            if admin and pwd and repwd:
                if re.search(pattern, admin) or re.search(pattern, pwd):
                    tkinter.messagebox.showerror(title="Yezi", message="账号或密码里不能存在中文!")
                elif pwd != repwd:
                    tkinter.messagebox.showerror(title="Yezi", message="请保持两个密码一样!")
                elif not re.search(pattern, pwd):
                    if re.search(pattern1, admin):
                        tkinter.messagebox.showerror(title="Yezi", message="账号首字母不能为非法字符!")
                    elif len(admin) < 8 or len(pwd) < 8:
                        tkinter.messagebox.showerror(title="Yezi", message="长度不能小于8位!")
                    else:
                        def hehe():
                            soc.connect(T_addr)
                            soc.send("2".encode())
                            time.sleep(0.3)
                            message = admin + "," + pwd
                            soc.send(message.encode())
                            time.sleep(1)
                            de = soc.recv(1024).decode()
                            if de == "ok":
                                tkinter.messagebox.showinfo(title="Yezi", message="注册成功!")
                            else:
                                tkinter.messagebox.showinfo(title="Yezi", message="注册失败!")
                            top_Button["state"] = "normal"
                        t = threading.Thread(target=hehe)
                        t.daemon = True
                        t.start()
            else:
                tkinter.messagebox.showerror(title="Yezi", message="账号或密码里不能为空!")

        top_Button["command"] = register
        def on_closing():
            if tkinter.messagebox.askokcancel("关闭窗口", "确定要退出吗?"):
                Button_pwd["state"] = "normal"
                Button_admin["state"] = "normal"
                root.state("normal")
                top.destroy()
        top.protocol("WM_DELETE_WINDOW", on_closing)

        """   
                Error"""
        def check_top():
            while True:
                if check_run == 1:
                    try:
                        if top_checked.get() == 1:
                            top_entry_pwd["show"] = ""
                            top_entry_repwd["show"] = ""
                            #top_entry_pwd.config(show="")
                            #top_entry_re_pwd.config(show="")
                        else:
                            top_entry_pwd["show"] = "*"
                            top_entry_repwd["show"] = "*"
                            #top_entry_pwd.config(show="*")
                            #top_entry_re_pwd.config(show="*")
                        time.sleep(0.2)
                    except:
                        pass
                else:
                    break
        """top_check_thread = threading.Thread(target=check_top)
        top_check_thread.daemon = True
        top_check_thread.start()
        Button_pwd.wait_window(top)"""
        def check_But(event):
            if top_checked.get() == 0:
                top_entry_pwd["show"] = ""
                top_entry_repwd["show"] = ""
            else:
                top_entry_pwd["show"] = "*"
                top_entry_repwd["show"] = "*"
        top_check.bind("<Button-1>", check_But)

    def Login():
        Button_admin["state"] = "disabled"
        admin1 = admin.get()
        pwd1 = pwd.get()
        soc1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        def hehe():
            try:
                soc1.connect(T_addr)
                message = admin1 + "," + pwd1
                soc1.send("1".encode())
                time.sleep(0.3)
                soc1.send(message.encode())
                time.sleep(1)
                data = soc1.recv(1024)
                if data == b"no":
                    tkinter.messagebox.showerror(title="Yezi", message="该账号或密码错误!")
                else:
                    tkinter.messagebox.showinfo(title="Yezi", message="登录成功!")
                    root.state("iconic")
                    My_top(root)
            except:
                tkinter.messagebox.showerror(title="Yezi", message="未连接到服务器!")
            finally:
                Button_admin["state"] = "normal"
        if not admin1 or not pwd1:
            tkinter.messagebox.showerror(title="Yezi", message="账号或密码不能为空!")
        else:
            t = threading.Thread(target=hehe)
            t.daemon = True
            t.start()
    Button_admin["command"] = Login
    Button_pwd["command"] = zhuce
    def Clear():
        admin.set("")
        pwd.set("")
    menu.add_command(label="Clear", command=Clear)
    def Close():
        root.destroy()
    menu.add_command(label="Close", command=Close)
    def Xinshi(event):
        menu.post(event.x_root, event.y_root)
    root.bind("<ButtonRelease-3>", Xinshi)

    def time_run():
        while True:
            now = datetime.datetime.now()
            s = str(now.year) + "-" + str(now.month) + "-" + str(now.day) + " "
            s += str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)
            time_label["text"] = s
            time.sleep(0.2)
    time_thread = threading.Thread(target=time_run)
    time_thread.daemon = True
    time_thread.start()

    def Check_pwd():
        while True:
            time.sleep(0.2)
            if check.get() == 1:
                entry_pwd["show"] = ""
            else:
                entry_pwd["show"] = "*"
    """check_thred = threading.Thread(target=Check_pwd)
    check_thred.daemon = True
    check_thred.start()"""
    def chek(event):
        if check.get() == 0:
            entry_pwd["show"] = ""
        else:
            entry_pwd["show"] = "*"
    check_button.bind("<Button-1>", chek)
    root.mainloop()
UI()