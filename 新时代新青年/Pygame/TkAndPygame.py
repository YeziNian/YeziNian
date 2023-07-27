import tkinter
import pygame
import tkinter.messagebox
import tkinter.filedialog
import tkinter.simpledialog
import tkinter.ttk
from PIL import Image
import sys
i = 0
clock = pygame.time.Clock()
def han():
    global i
    imag = pygame.image.load(r"C:\Users\40437\Desktop\cc\{0}.png".format(i))
    i += 1
    if i == 11:
        i = 0
    return pygame.transform.scale(imag, (300, 300))
class Mypygame:

    Isrun = 1

    def __init__(self, filename):
        self.filename = filename
        self.image = Image.open(filename)
        try:
            while True:
                current = self.image.tell()
                self.image.save(r"C:\Users\40437\Desktop\cc"+"\\"+str(current)+".png")
                self.image.seek(current+1)
        except Exception:
            pass

    def run(self):
        pygame.init()
        self.screen = pygame.display.set_mode((300, 300))
        self.fps = combox.get()
        if fps:
            try:
                while True:
                    clock.tick(int(self.fps))
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            Mypygame.Isrun = 0
                            pygame.quit()
                            break
                            #sys.exit()
                    self.data = han()
                    self.screen.blit(self.data, (0, 0))
                    pygame.display.flip()
            except Exception:
                pass
        else:
            pass


root = tkinter.Tk()
width, height = 300, 300
root.geometry("{0}x{1}+{2}+{3}".format(width, height,
        (root.winfo_screenwidth()-width)//2,
        (root.winfo_screenheight()-height)//2))
root.title("Yezi")
root.resizable(False, False)
def dakai():
    filename = tkinter.filedialog.askopenfilename(title="Yezi", filetypes=[("Only gif", "* .gif")])
    if filename:
        path.set(filename)
        #entry_path["state"] = "disabled"
        #button_path["state"] = "disabled"
def jiance():
    if path.get().endswith(".gif"):
        root.state("iconic")
        button_create["state"] = "disabled"
        jietu = Mypygame(r"C:\Users\40437\Desktop\aa.gif")
        jietu.run()
        while jietu.Isrun:
            pass
        entry_path["state"] = "normal"
        button_path["state"] = "normal"
        root.state("normal")
        button_create["state"] = "normal"
    else:
        tkinter.messagebox.showerror(title="Yezi", message="请使用gif图片！")
fps = [str(i*10) for i in range(1, 11)]
path = tkinter.StringVar(value="")
label_path = tkinter.Label(root, text="图片地址:")
label_path.place(x=10, y=20, width=60, height=20)
entry_path = tkinter.Entry(root, textvariable=path)
entry_path.place(x=70, y=20, width=180, height=20)
button_path = tkinter.Button(root, text="打开", command=dakai)
button_path.place(x=250, y=20, height=20, width=40)
lable = tkinter.Label(root, text="帧率:")
lable.place(x=10, y=80, width=40, height=20)
combox = tkinter.ttk.Combobox(root, values=tuple(fps))
combox.place(x=50, y=80, height=20, width=60)
button_create = tkinter.Button(root, text="生成", command=jiance)
button_create.place(x=130, y=200, width=40, height=30)

root.mainloop()