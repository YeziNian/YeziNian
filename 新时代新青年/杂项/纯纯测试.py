import ttkbootstrap as ttk
from ttkbootstrap.dialogs import Querybox, Messagebox
from ttkbootstrap.constants import *
import tkinter.filedialog
import re
import tkinter
import time

# focus Scro Floodgauge
"""
pattern = r"^[a-z]+[0-9]+"
tkinter.BitmapImage
#style = ttk.Style(theme="darkly")
def filename():
    de = tkinter.filedialog.askopenfilename(title='Yezi', filetypes=["* txt"])
    root.title(de)
root = ttk.Window(size=(400, 400), themename='darkly')
root.place_window_center()
button = ttk.Button(root, text="Click", command=filename, cursor='hand1')
button.pack()
sco = ttk.Scrollbar(root, orient="vertical")
sco.place(x=0, y=10, width=100, height=30)
def jiance(content):
    print(re.search(pattern, content))
comx = ttk.Combobox(root, state="readonly", values=[str(i) for i in range(100)], postcommand=lambda: print(1), takefocus=False)
entry = ttk.Entry(root, exportselection=True, validate="key")
entry.pack()
entry.bind("<FocusOut>", lambda x: print(x))
text = ttk.Text(root)
text.place(x=10, y=200, width=40, height=40)
sco.config(command=comx.xview())
comx.configure(xscrollcommand=sco.set)
heh = ttk.Labelframe(root, text='提示')
#heh.place(x=30, y=200, width=100, height=80)
#sco.configure(comx.xview)
#comx.config(sco.set)
comx.pack()
#flood = ttk.Floodgauge(root, mask="loading... {}%", maximum=200, value=10)
#flood.pack()
#flood.step(10)
tree = ttk.Treeview(root, columns=[0, 1], show=HEADINGS, height=10)
table_data = [(1,'one'),(2, 'two'),(3, 'three'),(4, 'four'),(5, 'five')
]
menu = ttk.Menu(root)
target = None
def delete():
    global target
    if target:
        tree.delete(target)
def copy():
    global target
    if target:
        print(tree.item(target, "values"))
menu.add_command(label="复制", command=copy)
menu.add_command(label="删除", command=delete)
x, y = 0, 0
def ji(event):
    global target, x, y
    y = event.y
    x = event.x
    #print(event.x, event.y)
    if event.widget == tree:
        target = tree.identify_row(y)
        if target:
            #print(target)
            #tree.selection_clear()
            tree.selection_set(target)
        menu.post(event.x_root, event.y_root)
for row in table_data:
    tree.insert('', END, values=row)
tree.heading(0, text="序号")
tree.heading(1, text="名字")
tree.column(0, width=60, minwidth=50)
tree.column(1, width=300, anchor=CENTER, minwidth=200)
tree.selection_add("I002")
#print(tree.selection_get())
root.bind("<Button-3>", ji)
#tree.heading(2, text="名字")
tree.pack()
def change():
    global target, x, y
    if target:
        #style.configure("Custom", padding=(0, 0, 0, 0))
        entry1 = ttk.Entry(root, width=60, cursor="cross")
        entry1.place(x=20, y=156 + y//35 * 35, width=60, height=20)
        entry2 = ttk.Entry(root, width=300, font=("Arial", 10))
        entry2.place(x=80, y=156 + y//35 * 35, width=300, height=20)
        entry1.focus_set()
        def j1(event):
            id1 = entry1.get()
            entry1.destroy()
            if id1:
                tree.set(target, 0, id1)
            entry2.focus_set()
        def j2(event):
            name1 = entry2.get()
            entry2.destroy()
            if name1:
                tree.set(target, 1, name1)
        entry1.bind("<FocusOut>", j1)
        entry2.bind("<FocusOut>", j2)
menu.add_command(label="修改", command=change)
def double(event):
    y = event.y
    x = event.x
    if event.widget == tree:
        target = tree.identify_row(y)
        if target:
            entry1 = ttk.Entry(root, width=60)
            entry1.place(x=20, y=156 + y // 35 * 35, width=60, height=20)
            entry2 = ttk.Entry(root, width=300)
            entry2.place(x=80, y=156 + y // 35 * 35, width=300, height=20)
            entry1.focus_get()
            def j1(event):
                id1 = entry1.get()
                entry1.destroy()
                entry2.focus_get()
                tree.set(target, 0, id1)
            def j2(event):
                name1 = entry2.get()
                entry2.destroy()
                tree.set(target, 1, name1)
            entry1.bind("<FocusOut>", j1)
            entry2.bind("<FocusOut>", j2)
tree.bind("<Double-Button-1>", double)
root.mainloop()"""
content = None
def clear():
    for k in canva.find_all():
        canva.delete(k)
def Draw_text():
    global content
    content = Querybox.get_string(title="Yezi", prompt="What do you wang to Input?")
    graphical.set(3)
root = ttk.Window(size=(400, 400), themename="darkly")
root.place_window_center()
photo = ttk.PhotoImage(file=r"C:\Users\40437\Desktop\aa.png")
note = ttk.Labelframe(root, text="Draw:")
note.pack()
graphical = ttk.IntVar(value=0)
menu = ttk.Menu(root, tearoff=0)
menu.add_radiobutton(label="Line", command=lambda: graphical.set(0))
menu.add_radiobutton(label="Rectangle", command=lambda: graphical.set(1))
menu.add_radiobutton(label="Circle", command=lambda: graphical.set(2))
menu.add_radiobutton(label="Text", command=Draw_text)
menu.add_separator()
menu.add_command(label="Clear", command=clear)
root.bind("<Button-3>", lambda event: menu.post(event.x_root, event.y_root))
x = ttk.IntVar()
y = ttk.IntVar()
lastdraw = 0
list_draw = []
def Draw_graphical(event):
    global lastdraw, content
    if lastdraw:
        canva.delete(lastdraw)
    if graphical.get() == 0:
        lastdraw = canva.create_line(x.get(), y.get(), event.x, event.y, smooth=True, joinstyle='bevel', arrow='last', fill='white')

    if graphical.get() == 1:
        lastdraw = canva.create_rectangle(x.get(), y.get(), event.x, event.y, fill='red')

    if graphical.get() == 2:
        lastdraw = canva.create_oval(x.get(), y.get(), event.x, event.y, fill='blue')

    if graphical.get() == 3:
        if content:
            lastdraw = canva.create_text(event.x, event.y, text=content, fill='pink')
def firsr_Dot(event):
    x.set(event.x)
    y.set(event.y)
def clear_ache(event):
    global lastdraw, list_draw
    list_draw.append(lastdraw)
    lastdraw = 0

root.bind("<ButtonRelease-1>", clear_ache)
root.bind("<Button-1>", firsr_Dot)
root.bind("<B1-Motion>", Draw_graphical)
canva = ttk.Canvas(note, cursor="hand1", highlightcolor='orange')
canva.pack()
root.mainloop()
