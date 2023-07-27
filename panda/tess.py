import tkinter
from tkinter import ttk
from ttkbootstrap import Style
import tkinter.messagebox
style = Style(theme="darkly")
root = style.master
root.geometry("300x300+600+260")
root.title("Message")
def Create():
    newtop = tkinter.Toplevel(root, width=300, height=300)
    root.state("iconic")
    newtop.geometry("300x300+600+260")
    Sex = tkinter.IntVar(value=1)
    radio_man = ttk.Radiobutton(newtop, variable=Sex, value=1, text="男")
    radio_woman = ttk.Radiobutton(newtop, variable=Sex, value=0, text="女")
    label = ttk.Label(newtop, text="性别:")
    label.place(x=10, y=10, width=30, height=30)
    radio_man.place(x=50, y=10, width=40, height=30)
    radio_woman.place(x=100, y=10, width=40, height=30)
    label_name = ttk.Label(newtop, text="姓名:")
    label_name.place(x=10, y=40, width=40, height=30)
    name_var = tkinter.StringVar(value="")
    entry_name = ttk.Entry(newtop, textvariable=name_var)
    entry_name.place(x=50, y=40, width=200, height=25)
    label_age = ttk.Label(newtop, text="年龄:")
    label_age.place(x=10, y=70, width=40, height=30)
    age = ttk.Spinbox(newtop, from_=0, to=100, increment=1, wrap=True)
    age.place(x=50, y=70, width=70, height=30)
    label_class = ttk.Label(newtop, text="班级:")
    label_class.place(x=10, y=100, height=30, width=40)
    com = ttk.Combobox(newtop, values=["class_1", "class_2", "class_3"], state="readonly")
    label_height = ttk.Label(newtop, text="身高:")
    label_height.place(x=10, y=140, width=40, height=30)
    height = ttk.Spinbox(newtop, from_=100, to=220, increment=0.1, wrap=True, format="%3.1f")
    height.place(x=50, y=140, width=70, height=30)
    com.place(x=50, y=104, height=25, width=100)
    def add():
        lie = []
        if not name_var or not age.get() or not height.get():
            root.deiconify()
            newtop.destroy()
            return
        else:
            lie.append(name_var.get())
            lie.append(str(Sex.get()))
            lie.append(age.get())
            lie.append(height.get())
        if com.get():
            tree.insert(eval(com.get()), 0, text="Child 0-1", values=lie)
            newtop.destroy()
        else:
            root.deiconify()
            newtop.destroy()
    bur = ttk.Button(newtop, text="确定", command=add)
    bur.place(x=110, y=220, width=50, height=30)
    def on_closing():
        newtop.destroy()
        root.deiconify()
    newtop.protocol("WM_DELETE_WINDOW", on_closing)

def dele():
    cur = tree.focus()
    tree.delete(cur)
button = ttk.Button(root, text="添加", command=Create, padding=2)
button.place(x=10, y=10, width=60, height=30)
button_delete = ttk.Button(root, text="删除", padding=2, command=dele)
button_delete.place(x=80, y=10, width=60, height=30)
tree = ttk.Treeview(root, selectmode="browse")
tree["columns"] = ["姓名", "性别", "年龄", "身高"]
tree.column("#0", width=0, stretch="yes")
tree.column("姓名", width=50, anchor="center")
tree.column("性别", width=50, anchor="center")
tree.column("年龄", width=50, anchor="center")
tree.column("身高", width=50, anchor="center")
tree.heading("#0", text="", anchor="w")
tree.heading("姓名", text="Name", anchor="center")
tree.heading("性别", text="sex", anchor="center")
tree.heading("年龄", text="age", anchor="center")
tree.heading("身高", text="height", anchor="center")
class_1 = tree.insert("", 0, text="class 0", open=False)
class_2 = tree.insert("", 0, text="class 1", open=False)
class_3 = tree.insert("", 0, text="class 2", open=False)
tree.place(x=0, y=50, width=300, height=250)
root.mainloop()