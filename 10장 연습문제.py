##2021041035 조민규##

from tkinter import *
from tkinter.filedialog import *
from PIL import ImageTk

#전역 변수#
filename = 'D:/충북대/2-1/오픈소스기초프로젝트/7주차과제/dog3.jpg'

#함수 선언#
def func_open():
    global filename
    filename = askopenfilename(parent = window, filetypes = (('GIF 파일', '*.gif'),('모든 파일', '*.*')))
    photo = ImageTk.PhotoImage(file = filename)
    pLabel.configure(image = photo)
    pLabel.image = photo

def func_exit():
    window.quit()
    window.destroy()

def func_zoom(event):
    photo = ImageTk.PhotoImage(file = filename)
    photo = photo.zoom(2)
    pLabel.configure(image = photo)
    pLabel.image = photo

def func_subsample(event):
    photo = ImageTk.PhotoImage(file = filename)
    photo = photo.subsample(2)
    pLabel.configure(image = photo)
    pLabel.image = photo

#메인 코드#
window = Tk()
window.geometry('600x600')
window.title('연습문제')

photo = ImageTk.PhotoImage(file = filename)
pLabel = Label(window, image = photo)
pLabel.pack(expand = 1, anchor = CENTER)

mainMenu = Menu(window)
window.config(menu = mainMenu)
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label = '파일', menu = fileMenu)
fileMenu.add_command(label = '파일 열기', command = func_open)
fileMenu.add_separator()
fileMenu.add_command(label = '프로그램 종료', command = func_exit)

pLabel.bind('<Up>', func_zoom)
pLabel.bind('<Down>', func_subsample)

window.mainloop()
