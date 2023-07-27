import pygame
import sys
"""
display（显示模块）、font（字体模块）、mixer（声音控制模块）、cursors（光标控制模块）
pygame.display.update() 后者可以根据选定的区域来更新部分内容，而前者则是更新整个待显示的内容。如果后者没有提供区域位置参数时，其作用和 display.flip() 相同。

pygame.FULLSCREEN	创建一个全屏窗口。
pygame.HWSURFACE	创建一个硬件加速窗口，必须和 FULLSCREEN 同时使用。
pygame.OPENGL	创建一个 OPENGL 渲染窗口。
pygame.RESIZABLE	创建一个可以改变大小的窗口。
pygame.DOUBLEBUF	创建一个双缓冲区窗口，建议在 HWSURFACE 或者 OPENGL 时使用。
pygame.NOFRAME	创建一个没有边框的窗口。

scrren.blit(source, dest, area=None, special_flags = 0)
source：表示要粘贴的 Surface 对象。
dest：主窗口中的一个标识的坐标位置，可以接受一个 (x,y) 元组，或者 (x,y,width,height) 元组，也可以是一个 Rect 对象；
area：接受一个 Rect 对象，默认为 None，如果提供该参数则相当于抠图操作，即在屏幕的指定区域显示想要的内容；
special_flags：可选参数，它是 Pygame.1.8 版本新增的功能，用于指定对应位置颜色的混合方式，参数值有 BLEND_RGBA_ADD、BLEND_SUB 等。如果不提供该参数的情况下，默认使用 source 的颜色覆盖 screen 的颜色。

pygame.display.get_surface()	获取当前显示的 Surface 对象。
pygame.display.flip()	更新整个待显示的 Surface 对象到屏幕上。
pygame.display.update()	更新部分软件界面显示。
pygame.display.Info()	产生一个 VideoInfo 对象，包含了显示界面的相关信息。
pygame.display.set_icon()	设置左上角的游戏图标，图标尺寸大小为 32*32。
pygame.display.iconify()	将显示的主窗口即 Surface 对象最小化，或者隐藏。
pygame.display.get_active()	当前显示界面显示在屏幕上时返回 True，如果窗口被隐藏和最小化则返回 False。

通过前面内容的介绍，我们对 Surface 对象有了大体上的认识。Pygame 针对文本、图像、颜色提供了不同模块来生成它们各自的 Surface 对象。Surface 模块是Pygame 中专门用来新建图像的，通过该模块可以创建一个 Surface 对象，语法格式如下：

Surface=pygame.Surface(size=(width,height),flags,depth)
size：表示 Surface 对象的矩形区域大小；
flags：功能标志位，有两个可选参数值 HWSURFACE 和 SPCALPHA，前者代表将创建的 Surface 对象存放于显存中，后者表示让图像的每一个像素都包含一个 alpha 通道
depth：指定像素的颜色深度，默认为自适应模式，由 Pygame 自动调节。

pygame.Surface.blit()	将一个图像（Surface 对象）绘制到另一个图像上
pygame.Surface.convert()	修改图像（Surface 对象）的像素格式
pygame.Surface.fill()	使用纯色填充 Surface 对象
pygame.Surface.scroll()	复制并移动 Surface 对象
pygame.Surface.set_alpha()	设置整个图像的透明度
pygame.Surface.get_at()	获取一个像素的颜色值
pygame.Surface.set_at()	设置一个像素的颜色值
pygame.Surface.get_palette()	获取 Surface 对象 8 位索引的调色板
pygame.Surface.map_rgb()	将一个 RGBA 颜色转换为映射的颜色值
pygame.Surface.set_clip()	设置该 Surface 对象的当前剪切区域
pygame.Surface.subsurface()	根据父对象创建一个新的子 Surface 对象
pygame.Surface.get_offset()	获取子 Surface 对象在父对象中的偏移位置
pygame.Surface.get_size()	获取 Surface 对象的尺寸

pygame.transform.scale()	将图片缩放至指定的大小，并返回一个新的 Surface 对象。
pygame.transform.rotate()	将图片旋转至指定的角度。
pygame.transform.rotozoom()	以角度旋转图像，同时将图像缩小或放大至指定的倍数
pygame.font.SysFont(name, size, bold=False, italic=False)
1
name：列表参数值，表示要从系统中加载的字体名称，它会按照列表中的元素顺序依次搜索，如果系统中没有列表中的字体，将使用 Pygame 默认的字体。

size：表示字体的大小；
bold：字体是否加粗；
italic：字体是否为斜体。


render(text, antialias, color, background=None)
1
参数说明如下所示：

text：要绘制的文本内容
antialias：布尔值参数，是否是平滑字体（抗锯齿）。
color：设置字体颜色；
background：可选参数，默认为 None，该参数用来设置字体的背景颜色。
\
"""
pygame.init()
screen = pygame.display.set_mode((400, 400), flags=pygame.RESIZABLE) #flags表示创建窗口的类型
pygame.display.set_caption("Yezi")
screen.fill("white")
f = pygame.font.Font('C:/Windows/Fonts/simhei.ttf', 50)
text = f.render("叶子", True, (255, 0, 0), (0, 0, 0))
textRect =text.get_rect()
textRect.center = (200, 200)
screen.blit(text, textRect)
face = pygame.Surface((50, 50), flags=pygame.HWSURFACE)
face.fill(color='pink')
image = pygame.image.load(r"C:\Users\40437\Desktop\cc.bmp").convert()
while True:
    for event in pygame.event.get():
        # 判断用户是否点了"X"关闭按钮,并执行if代码段
        if event.type == pygame.QUIT:
            #卸载所有模块
            pygame.quit()
            #终止程序，确保退出程序
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            screen.blit(image, (0, 0))
            #te = f.render("HEHEH", True, (0, 255, 0), (0, 0, 0))
            #tec = te.get_rect()
            #tec.bottom = (300, 300)
            #screen.blit(te, tec)
            #screen.blit(face, (100, 100))
            #print(pygame.display.Info())
            #pygame.display.iconify()
        if event.type == pygame.MOUSEBUTTONUP:
            #image.scroll(10, 10)
            te = f.render("Yue", True, (0, 0, 255), (0, 0, 0))
            face.blit(te, (0, 0))
    pygame.display.flip() #更新屏幕内容
    #print(pygame.display.get_active())


