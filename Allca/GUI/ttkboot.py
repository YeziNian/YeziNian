import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from datetime import datetime
import psutil,time,threading
root = ttk.Window(title="Yezi", themename="darkly", minsize=(100, 100))
root.place_window_center()    #让显现出的窗口居中
# root.resizable(False,False)   #让窗口不可更改大小
# root.wm_attributes('-topmost', 1)#让窗口位置其它窗口之上
#root.attributes("-alpha", 0.2)
style = ttk.Style()
theme_selection = ttk.Frame(root, padding=(10, 10, 10, 0))
theme_selection.pack(fill=X, expand=YES)
lbl = ttk.Label(theme_selection, text="选择主题:")
theme_names = style.theme_names()
theme_cbo = ttk.Combobox(master=theme_selection, text=style.theme.name, values=theme_names)
theme_cbo.pack(padx=10, side=RIGHT)
theme_cbo.current(theme_names.index(style.theme.name))
lbl.pack(side=RIGHT)
def change_theme(event):
    theme_cbo_value = theme_cbo.get()
    style.theme_use(theme_cbo_value)
    theme_selected.configure(text=theme_cbo_value)
    theme_cbo.selection_clear()
theme_cbo.bind('<<ComboboxSelected>>', change_theme)
theme_selected = ttk.Label(master=theme_selection, text="litera", font="-size 24 -weight bold")
theme_selected.pack(side=LEFT)
def jiance(event):
    objc = event.widget
    if objc == entry:
        de.set("")
    else:
        if de.get() == "":
            print(1)
            #entry.selection_clear()
            objc.focus()
root.bind("<Button-1>", jiance)
de = ttk.StringVar(value="默认未输入")
entry = ttk.Entry(root, textvariable=de, font="微软雅黑")
entry.pack(padx=10, pady=10)

#文本框
text = ttk.Text(root)
text.pack()
text.insert("insert", "1212获取文件和啊就是的")
text.delete(0.0, END)
text.insert('insert','text-content 2\npy\n')
text.see(ttk.END) #光标跟随着插入的内容移动

#日期
mydate = datetime(1933, 10, 2)
de1 = ttk.DateEntry(startdate=mydate)
de1.pack()
print(de1.entry.get())
now = datetime.now()
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print(type(formatted_date))
print(type(now))
#date_var = ttk.StringVar(value=formatted_date)
de2 = ttk.DateEntry(root, bootstyle="success", dateformat=r"%Y", startdate=now) #r"%Y-%m-%d"
de2.pack()

#多选按钮
"""variable_content = [[ttk.StringVar(),"111"],[ttk.StringVar(),"222"],[ttk.StringVar(),"333"],[ttk.StringVar(),"666"]
]
ttk.Checkbutton(root, text="111", variable=variable_content[0][0]).pack(side=ttk.LEFT, padx=5)
ttk.Checkbutton(root, text="222", variable=variable_content[1][0], bootstyle="square-toggle").pack(side=ttk.LEFT, padx=5)
ttk.Checkbutton(root, text="333", variable=variable_content[2][0], bootstyle="round-toggle").pack(side=ttk.LEFT, padx=5)
ttk.Checkbutton(root, text="666", variable=variable_content[3][0]).pack(side=ttk.LEFT, padx=5)"""
"""def ensure():
    print([v for i, v in variable_content if i.get()])
ttk.Button(text="确定",command=ensure).pack(side=ttk.LEFT, padx=5)"""



a = ttk.Meter(master=root,bootstyle=DEFAULT,metertype="full")#将仪表显示为一个完整的圆形或半圆形（semi）wedgesize=5, #设置弧周围的指示器楔形长度,如果大于 0，则此楔形设置为以当前仪表值为中心的指示器amounttotal=50, #仪表的最大值，默认100amountused=10, #仪表的当前值metersize=200,#仪表大小showtext=True, #指示是否在仪表上显示左、中、右文本标签interactive=True, #是否可以手动调节数字的大小textleft='左边', #插入到中心文本左侧的短字符串textright='右边',textfont="-size 30", #中间数字大小subtext="文本",subtextstyle=DEFAULT,subtextfont="-size 20",#文本大小).pack(side=ttk.LEFT, padx=5)
a.pack()

com = ttk.Combobox(root, values=["2", "asda"])
com.current(1)
com.pack()

def get_dataentry():
    print(de2.entry.get())
ttk.Button(root,text="get_dataentry", bootstyle=(PRIMARY, "outline-toolbutton"),command=get_dataentry).pack()




root.mainloop()


def biaoqian():
    root = ttk.Window()
    ttk.Label(root, text="标签1", bootstyle=INFO).pack(side=ttk.LEFT, padx=5, pady=10)
    ttk.Label(root, text="标签2", bootstyle="inverse").pack(side=ttk.LEFT, padx=5, pady=10)
    ttk.Label(root, text="标签3", bootstyle="inverse-danger").pack(side=ttk.LEFT, padx=5, pady=10)
    ttk.Label(root, text="标签4", bootstyle=WARNING, font=("微软雅黑", 15), background='#94a2a4').pack(side=LEFT,
                                                                                                     padx=5, pady=10)
    root.mainloop()
    '''
    # bootstyle colors
    PRIMARY = 'primary'
    SECONDARY = 'secondary'
    SUCCESS = 'success'
    DANGER = 'danger'
    WARNING = 'warning'
    INFO = 'info'
    LIGHT = 'light'
    DARK = 'dark'# bootstyle types
    OUTLINE = 'outline'
    LINK = 'link'
    TOGGLE = 'toggle'
    INVERSE = 'inverse'
    STRIPED = 'striped'
    TOOLBUTTON = 'toolbutton'
    ROUND = 'round'
    SQUARE = 'square'
    '''
def anniu():
    root = ttk.Window()
    ttk.Button(root, text="Button 1", bootstyle=SUCCESS).pack(side=LEFT, padx=5, pady=10)
    ttk.Button(root, text="Button 2", bootstyle=(INFO, OUTLINE)).pack(side=LEFT, padx=5, pady=10)
    ttk.Button(root, text="Button 3", bootstyle=(PRIMARY, "outline-toolbutton")).pack(side=LEFT, padx=5, pady=10)
    ttk.Button(root, text="Button 4", bootstyle="link").pack(side=LEFT, padx=5, pady=10)
    ttk.Button(root, text="Button 5", bootstyle="success-link").pack(side=LEFT, padx=5, pady=10)
    ttk.Button(root, text="Button 6", state="disabled").pack(side=LEFT, padx=5, pady=10)  # 在禁用状态下创建按钮
    root.mainloop()
