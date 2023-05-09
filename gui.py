# -*- coding: utf-8 -*-
"""
Created on Wed May  3 10:16:27 2023

@author: asus
"""

from tkinter import *


root = Tk()

#judul
root.title("Kalkulator GUI Python")
#ukuran window
root.geometry('600x400')

label1 = Label(root, text ="Input Nilai Pertama : ", anchor="e",width=20)
label1.grid(column=0, row=0)

label2 = Label(root, text ="Input Nilai Kedua : ", anchor="e",width=20)
label2.grid(column=0, row=1)

label3 = Label(root, text ="Hasil : ", anchor="e",width=20)
label3.grid(column=0, row=2)

#form input
nilai1 = Entry(root,width=20)
nilai1.grid(column=1,row=0)

nilai2 = Entry(root,width=20)
nilai2.grid(column=1,row=1)

hasil = Label(root, text="0",anchor="w",width=10)
hasil.grid(column=1,row=2)

#function
def tambah():
    hasil.configure(text=(float(nilai1.get())+float(nilai2.get())))
    
def kurang():
    hasil.configure(text=(float(nilai1.get())-float(nilai2.get())))
    
def kali():
    hasil.configure(text=(float(nilai1.get())*float(nilai2.get()))) 
    
def bagi():
    hasil.configure(text=(float(nilai1.get())/float(nilai2.get())))
    
def pangkat():
    hasil.configure(text=(float(nilai1.get())**float(nilai2.get())))
    
def modulus():
    hasil.configure(text=(float(nilai1.get())%float(nilai2.get())))
    
def akar():
    hasil.configure(text=(float(nilai1.get())**(1/float(nilai2.get()))))

    
#button
btn = Button(root, text="Tambah",command=tambah)
btn.grid(column=0,row=3)

btn = Button(root, text="Kurang",command=kurang)
btn.grid(column=1,row=3)

btn = Button(root, text="Kali",command=kali)
btn.grid(column=0,row=4)

btn = Button(root, text="Bagi",command=bagi)
btn.grid(column=1,row=4)

btn = Button(root, text="Pangkat",command=pangkat)
btn.grid(column=0,row=5)

btn = Button(root, text="Mod",command=modulus)
btn.grid(column=1,row=5)

btn = Button(root, text="X Akar Y",command=akar)
btn.grid(column=0,row=6)

root.mainloop()