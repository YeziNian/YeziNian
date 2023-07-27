import socket
import tkinter
import tkinter.filedialog
import tkinter.messagebox
import datetime
import time
import threading
import tkinter.simpledialog
import re
import os
from tkinter import TclError
from PIL import ImageGrab, ImageTk, Image
port = 51037
def Ui():
    newtop = None
    root = tkinter.Tk()
    root.title("Yezi")
    height = root.winfo_screenheight()
    width = root.winfo_screenwidth()
    root.geometry("200x200+{0}+{1}".format((width-200)//2, (height-200)//2))
    root.attributes("-alpha", 0.9)
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #canva.create_image(-100, 0, image=image, anchor=tkinter.NW)
    def on_entry_click(event):
        try:
            # 禁用输入法
            event.widget.tk.call('tk', 'windowingsystem', 'xim', 'unset')
        except TclError:
            pass
    admin = tkinter.StringVar(value="")
    pwd = tkinter.StringVar(value="")
    button_admin = tkinter.Entry(root, textvariable=admin)
    button_admin.place(x=65, y=40, height=20, width=100)
    button_admin.bind("<FocusIn>", on_entry_click)
    button_pwd = tkinter.Entry(root, textvariable=pwd, show="*")
    button_pwd.place(x=65, y=70, height=20, width=100)
    button_pwd.bind("<FocusIn>", on_entry_click)
    Reme = tkinter.IntVar(value=0)
    check_button = tkinter.Checkbutton(root, variable=Reme, onvalue=1, offvalue=0)
    check_button.place(x=171, y=70, height=20, width=20)
    def zhuce():
        if label_fuwu["fg"] == "blue":
            if admin.get() and pwd.get():
                pattern = r"[\u4e00-\u9fa5]"
                pattern1 = r"^[!@#$%^^&*()_+]"
                if re.search(pattern, admin.get()):
                    tkinter.messagebox.showerror(title="Yezi", message="账号中不能存在中文!")
                elif re.search(pattern1, admin.get()):
                    tkinter.messagebox.showerror(title="Yezi", message="账号不能以字符开头!")
                else:
                    with open("data.txt", "w") as fp:
                        fp.write(admin.get() + "\n" + pwd.get())
                    tkinter.messagebox.showinfo(title="Yezi", message="注册成功!")
            else:
                tkinter.messagebox.showerror(title="Yeze", message="账号或密码不能为空!")
        else:
            tkinter.messagebox.showerror(title="Yezi", message="请按F连接,然后在注册!")
    Zhuce = tkinter.Button(root, text="注册", command=zhuce)
    Zhuce.place(x=120, y=120, height=30, width=40)
    def login():
        if label_fuwu["fg"] == "blue":
            if not os.path.exists("data.txt"):
                tkinter.messagebox.showerror(title="Yezi", message="账号不存在!")
                return
            with open("data.txt", "r") as fp:
                a = fp.readline().strip()
                b = fp.readline().strip()
                if a == admin.get() and b == pwd.get():
                    global newtop
                    tkinter.messagebox.showinfo(title="Yezi", message="登录成功!")
                    newtop = tkinter.Toplevel(root, width=200, height=200)
                    newtop.title("Yezi")
                    button = tkinter.Button(newtop, text="Hello")
                    button.pack(fill=tkinter.BOTH, expand=tkinter.YES)
                    tanchuang = True
                    labe = tkinter.Label(newtop, text="Ok")
                    labe.pack()
                    def Ok():
                        filename = tkinter.filedialog.askopenfilename(title="Yezi", filetypes=[("text files", "* .txt")])
                        labe["text"] = filename
                        button["state"] = "disabled"
                        if tanchuang:
                            tkinter.messagebox.showinfo(title="Yezi", message="Locked! Press w to unlock it!")
                    def jietui():
                        newtop.geometry("{0}x{1}".format(width, height))
                        newtop.overrideredirect(True)
                        X = tkinter.IntVar(value=0)
                        Y = tkinter.IntVar(value=0)
                        def queding(event):
                            X.set(event.x)
                            Y.set(event.y)
                        def move(event):
                            global lastDraw
                            try:
                                canvas.delete(lastDraw)
                            except Exception:
                                pass
                            lastdraw = canvas.create_rectangle(X.get(), Y.get(), event.x, event.y, outline="black")
                        png = ImageGrab.grab(bbox=(0, 0, width//2, height//2))
                        png.save(r"C:\Users\40437\Desktop\what.png")
                        image1 = Image.open(r"C:\Users\40437\Desktop\what.png")
                        png = ImageTk.PhotoImage(image1)
                        image = tkinter.PhotoImage(file=r"C:\Users\40437\Desktop\what.png")
                        canvas = tkinter.Canvas(newtop)
                        canvas.pack(fill=tkinter.BOTH, expand=tkinter.YES)
                        #canvas.create_line(0, 0, 110, 110)
                        canvas.create_image(0, 0, image=tkinter.PhotoImage(file=r"C:\Users\40437\Desktop\what.png"))
                        canvas.bind("<Button-1>", queding)
                        canvas.bind("<B1-Motion>", move)
                    def unlock(event):
                        button["state"] = "normal"
                        yesno = tkinter.messagebox.askyesno(title="Yezi", message="Do you want to jie tu?")
                        if yesno == tkinter.YES:
                            tanchuang = False
                            root.state("iconic")
                            button.pack_forget()
                            labe.pack_forget()
                            jietui()
                            #tkinter.messagebox.showinfo(title="Yezi", message="Please Login again!")
                        else:
                            pass
                    newtop.bind_all("<KeyPress-W>", unlock)
                    newtop.bind_all("<KeyPress-w>", unlock)
                    button["command"] = Ok
                else:
                    tkinter.messagebox.showwarning(title="Yezi", message="登录失败!")
            Login.wait_window(newtop)
        else:
            tkinter.messagebox.showerror(title="Yezi", message="请按F连接,然后在注册!")
    Menu = tkinter.Menu(root, tearoff=0)
    def autu(event):
        with open("data.txt", "r") as fp:
            if fp:
                admin1 = fp.readline().strip()
                pwd1 = fp.readline().strip()
                admin.set(admin1)
                pwd.set(pwd1)
            else:
                tkinter.messagebox.showerror('Yezi', message='Sorry, You need to register!')
    root.bind("<KeyPress-Q>", autu)
    def close():
        root.destroy()
    Menu.add_command(label="Close", command=close)
    def clear():
        admin.set("")
        pwd.set("")
    Menu.add_command(label="Clear", command=clear)
    def kek(event):
        Menu.post(event.x_root, event.y_root)
    root.bind("<ButtonRelease-3>", kek)
    def Jiance():
        while True:
            if Reme.get() == 1:
                button_pwd["show"] = ""
            elif Reme.get() == 0:
                button_pwd["show"] = "*"
            time.sleep(0.1)
    Linkyesorno = 0
    def lianjie(event):
        try:
            soc.connect((socket.gethostbyname(socket.gethostname()), port))
            label_wenben.set("连接成功!")
            Linkyesorno = 1
            label_fuwu["fg"] = "blue"
        except Exception as e:
            tkinter.messagebox.showerror(title="Yezi", message="连接失败!")
    def on_closing():
        if tkinter.messagebox.askokcancel("关闭窗口", "确定要退出吗?"):
            if Linkyesorno == 1:
                soc.send(b"bye")
                soc.close()
                root.destroy()
            else:
                root.destroy()
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.bind("<KeyPress-F>", lianjie)
    eje = threading.Thread(target=Jiance)
    eje.daemon = True
    eje.start()
    Login = tkinter.Button(root, text="登录", command=login)
    Login.place(x=60, y=120, height=30, width=40)
    label_admin = tkinter.Label(root, text="admin:")
    label_pwd = tkinter.Label(root, text="pwd:")
    label_admin.place(x=20, y=40, height=20, width=40)
    label_pwd.place(x=20, y=70, height=20, width=40)
    label1 = tkinter.Label(root)
    label1.place(x=60, y=170, height=30, width=140)
    label_wenben = tkinter.StringVar(value="当前未连接!")
    label_fuwu = tkinter.Label(root, textvariable=label_wenben, fg="red")
    label_fuwu.place(x=60, y=10, width=80, height=20)
    def TI():
        while 1:
            now = datetime.datetime.now()
            s = str(now.year) + "-" + str(now.month) + "-" + str(now.day) + " "
            s += str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)
            label1["text"] = s
            time.sleep(0.2)
    t = threading.Thread(target=TI)
    t.daemon = True
    t.start()
    root.mainloop()
Ui()
