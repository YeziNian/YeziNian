import MySQLdb
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import random
from ttkbootstrap.dialogs import Messagebox, Querybox
db_config = {
    'host': 'localhost',
    'user': 'root',
    'passwd': 'xingxing',
    'port': 3306,
    'db': 'test'
}
root = ttk.Window(themename="darkly", size=(400, 400), resizable=(False, False))
root.title('Yezi')
root.place_window_center()
data = None
def jiance():
    global data
    conn = MySQLdb.connect(**db_config, autocommit=False)
    conn.autocommit(False)
    cur = conn.cursor()
    cur.execute("SELECT * FROM new")
    data = cur.fetchall()
    cur.close()
    conn.close()
    Messagebox.show_info(title="Yezi", message="连接成功!")
    for row in data:
        lisbox.insert('', END, values=row)

button = ttk.Button(root, text='连接', command=jiance)
button.place(x=140, y=20, width=80, height=50)
sco = ttk.Scrollbar(root, orient='vertical')
sco.pack(fill=Y, side='right')
lisbox = ttk.Treeview(root, columns=['id', 'name', 'price'], show=HEADINGS, height=5)
lisbox.heading(0, text='ID')
lisbox.heading(1, text='NAME')
lisbox.heading(2, text='PRICE')
lisbox.column(0, width=60, anchor=CENTER)
lisbox.column(1, width=60, anchor=S)
lisbox.column(2, width=200, anchor=S)
sco.config(command=lisbox.yview)
lisbox.config(yscrollcommand=sco.set)
lisbox.place(x=0, y=80, width=380, height=300)
root.mainloop()