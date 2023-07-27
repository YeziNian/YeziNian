import time
import pyautogui
#pyautogui.moveTo(400, 400)
#print(pyautogui.position())
x = 588
y = 415

#pyautogui.dragTo(1000, 415, 0.1, button="left")
import ttkbootstrap as ttk
from ttkbootstrap.dialogs import Messagebox, Querybox
import threading
import time
import queue
root = ttk.Window(size=(400, 400), themename="darkly")
root.place_window_center()
text = ttk.StringVar(value='')
que = queue.Queue()
def change():

    for i in range(100):
        text.set(str(i))
        time.sleep(0.01)
    #Messagebox.show_info(message="heh")
    #que.put(Messagebox.show_info(message="heh"))
    root.after(0, lambda: Messagebox.show_info(message="heh"))
t = threading.Thread(target=change)
t.daemon = True
t.start()
#que.get()
label = ttk.Label(root, textvariable=text)
label.pack()
root.mainloop()