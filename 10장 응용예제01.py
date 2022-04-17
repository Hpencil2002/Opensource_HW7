##2021041035 조민규##

from tkinter import *
from PIL import ImageTk

#함수 선언#
def myFunc():
    if var.get() == 1:
        labelImage.configure(image = photo1)
    elif var.get() == 2:
        labelImage.configure(image = photo2)
    else:
        labelImage.configure(image = photo3)

#전역 변수#
var, labelImage = 0, None
photo1, photo2, photo3 = [None] * 3

#메인 코드#
window = Tk()
window.geometry('400x400')
window.title('애완동물 선택하기')
labelText = Label(window, text = '좋아하는 동물 투표', fg = 'blue', font = ('궁서체', 20))

var = IntVar()
rb1 = Radiobutton(window, text = '강아지', variable = var, value = 1)
rb2 = Radiobutton(window, text = '고양이', variable = var, value = 2)
rb3 = Radiobutton(window, text = '토끼', variable = var, value = 3)
buttonOk = Button(window, text = '사진 보기', command = myFunc)

photo1 = ImageTk.PhotoImage(file = 'D:/충북대/2-1/오픈소스기초프로젝트/7주차과제/dog3.jpg')
photo2 = ImageTk.PhotoImage(file = 'D:/충북대/2-1/오픈소스기초프로젝트/7주차과제/cat.jpg')
photo3 = ImageTk.PhotoImage(file = 'D:/충북대/2-1/오픈소스기초프로젝트/7주차과제/rabbit.jpg')

labelImage = Label(window, width = 200, height = 200, bg = 'yellow', image = None)

labelText.pack(padx = 5, pady = 5)
rb1.pack(padx = 5, pady = 5)
rb2.pack(padx = 5, pady = 5)
rb3.pack(padx = 5, pady = 5)
buttonOk.pack(padx = 5, pady = 5)
labelImage.pack(padx = 5, pady = 5)

window.mainloop()
