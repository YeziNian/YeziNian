import pyautogui
import numpy as np
import threading
import queue
import time
position = ["W", "A", "S", "D"]
path = r"C:\Users\40437\Desktop"
feiji = path + r"\heh.png"
target = path + r"\data.png"
de = pyautogui.locateOnScreen(feiji)
que = queue.Queue()
que.maxsize = 1
#print(de)
def get_target():
    while True:
        posi = pyautogui.locateOnScreen(target)
        if not posi:
            continue
        if que.empty():
            que.put(posi)
        time.sleep(0.5)
def get_posi(tup):
    return (40, 20)
class Auto_run:

    def __init__(self, feiji_path: str = feiji):
        self.feiji = pyautogui.locateOnScreen(feiji_path)

    def run(self, feiji_path: str = feiji):

        t = threading.Thread(target=get_target)
        t.daemon = True
        t.start()
        while True:
            new_posi = que.get()
            new_width, new_height = get_posi(new_posi)
            self.width, self.height = get_posi(self.feiji)
            if new_width <= 90 and new_height <= 400:
                pyautogui.press(position[1])
                pyautogui.press(position[0])
            elif new_width >= 90 and new_height <= 400:
                pyautogui.press(position[0])
                pyautogui.press(position[3])
            time.sleep(0.5)
            self.feiji = pyautogui.locateOnScreen(feiji_path)
if __name__ == '__main__':
    pe = Auto_run()
    pe.run()







