import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""
        法则:
                如果
"""


"""data = pd.DataFrame([[*np.random.randint(4, 100, 2), *np.random.randn(1)] for i in range(1000)], columns=["age", "weight", "ratio"])
for m, n in enumerate(data.loc[:, "age"]):
    if n >= 70:
       data.iat[m, 0] = np.NAN
    else:
        pass
data.to_csv("pipe.csv", index=0, float_format="%.2f", na_rep=np.NAN)  #空值会用1替代

Data = pd.read_csv("pipe.csv")
a = Data["age"].value_counts()
num = sum(a)
Data.fillna(10, inplace=True)
"""
a = 1
dic = {a: 1}
import tkinter
root = tkinter.Tk()
heitht = root.winfo_screenheight()
width = root.winfo_screenwidth()
root.geometry("800x600+{0}+{1}".format((width - 800) // 2, (heitht - 600) // 2))
root.title("Yezi Canvas")
root.resizable(False, False)

def Ck(event):
    print(event.x, event.x_root)
canva = tkinter.Canvas(root)
canva.pack(fill=tkinter.BOTH, expand=tkinter.YES)
canva.bind("<Button-1>", Ck)
canva.create_line(10, 10, 30, 30, fill="blue")
root.mainloop()