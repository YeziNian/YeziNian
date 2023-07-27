import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import time
import datetime
from ttkbootstrap.dialogs import Messagebox, Querybox
import random
import threading
lis = [str(i) for i in range(10)]
root = ttk.Window(themename="darkly", size=(400, 400))
root.title("Yezi")
root.place_window_center()
#root.overrideredirect(True)
#root.attributes("-alpha", 0.2)
# root.wm_attributes('-topmost', 1)#让窗口位置其它窗口之上
def jiance():
    while True:
        print(root.clipboard_get())
        if root.clipboard_get() == "1":
            print("yes")
        time.sleep(0.2)

t1 = threading.Thread(target=jiance)
t1.daemon = True
combox = ttk.Combobox(root, values=lis, exportselection=False, foreground="pink", font=("pink"))
combox.bind("<<ComboboxSelected>>", lambda event: combox.selection_clear())
#combox.current()
combox.pack()
label = ttk.Label(root, text="Hello Jack!", bootstyle=INFO)
label.pack()
def coc(data, c, d):
    if data.isdigit():
        print("yes")
        print(c, d)
    else:
        print("no")
        print(c, d)
entry = ttk.Entry(root, validate="all", validatecommand=(root.register(coc), "%P", "%V", "%s"))
entry.pack()
text = ttk.Text(root)
text.insert(0.0, "asdas")
#text.pack()
#print(text.get(0.0, END))
#text.see(END)
mytime = datetime.datetime(2014, 10, 5)
date = ttk.DateEntry(root, dateformat=r"%Y-%m-%d", startdate=mytime)
date.pack()
de = ttk.IntVar(value=0)
t1 = ttk.Checkbutton(root, text="大小", variable=de)
t2 = ttk.Checkbutton(root, text="科学", variable=de)
t1.pack()
t2.pack()
circle = ttk.Meter(root, metertype="full")
#circle.pack()
hh = ttk.IntVar(value=0)
def change():
    for i in range(101):
        hh.set(i)
        time.sleep(0.2)
k = threading.Thread(target=change)
k.daemon = True
#k.start()
bar = ttk.Progressbar(root, orient="horizontal", mode="determinate", variable=hh, phase=20)
bar.pack()
bar.start()
#bar.stop()
cm = ttk.Floodgauge(root, maximum=200, mask="loading...{}", value=20)
cm.pack()
cm.start()
#Messagebox.okcancel(message="是否关闭!", alert=False)
#cm.step(20)
#qw = Querybox.get_date()
qw = Querybox.get_integer(prompt="niha")
print(qw)
root.mainloop()