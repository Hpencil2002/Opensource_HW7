##2021041035 조민규##

from tkinter import *
from tkinter import ttk
from PIL import ImageTk

window = Tk()

baseTab = ttk.Notebook(window)

tabDog = ttk.Frame(baseTab)
baseTab.add(tabDog, text = '강아지')
tabCat = ttk.Frame(baseTab)
baseTab.add(tabCat, text = '고양이')

baseTab.pack(expand = 1, fill = 'both')

photoDog = ImageTk.PhotoImage(file = 'D:/충북대/2-1/오픈소스기초프로젝트/7주차과제/dog3.jpg')
labelDog = Label(tabDog, image = photoDog)
labelDog.pack()

photoCat = ImageTk.PhotoImage(file = 'D:/충북대/2-1/오픈소스기초프로젝트/7주차과제/cat.jpg')
labelCat = Label(tabCat, image = photoCat)
labelCat.pack()

window.mainloop()
