from tkinter import ttk
from tkinter import Tk
import threading
import time
def paste_text():
    text = root.clipboard_get()
    print("Pasted Text:", text)
def hehe():
    print("ok")
def ok():
    for i in range(100):
        scrollbar.set(i, 100)
        time.sleep(1)
def scroll_update(*args):
    combobox.xview(*args)
def cm(data):
    if data.isdigit():
        print("yes")
    else:
        print("no")

root = Tk()
values = ["Option 1", "Option 2", "Option 3"]
combobox = ttk.Combobox(root, values=values, exportselection=False, height=21, postcommand=hehe, takefocus=True)
combobox.pack()
labe = ttk.Label(root, text="asdasd")
labe.pack()
# 绑定粘贴事件到combobox
def change():
    while True:
        if entry["validata"] == "none":
            entry.configure(validate="focusout")
        time.sleep(1)
root.bind('<Control-v>', lambda e: paste_text())
values = [str(i) for i in range(100)]
combobox = ttk.Combobox(root, values=values)
combobox.pack()
aosda = threading.Thread(target=change)
aosda.daemon = True
aosda.start()
scrollbar = ttk.Scrollbar(root, orient="horizontal", command=scroll_update)
scrollbar.pack(fill="x")#scrollbar.set(0, 100)
h = threading.Thread(target=ok)
h.daemon = True
h.start()
# 设置xscrollcommand选项为scrollbar.set命令
combobox["xscrollcommand"] = scrollbar.set
entry = ttk.Entry(root, validate="focusout", validatecommand=(root.register(cm), "%P"))
entry.pack()
root.mainloop()