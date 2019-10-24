import cv2
import matplotlib.pyplot as plt
import tkinter as tk
import glob
from tkinter import ttk
from PIL import ImageTk, Image
import Task1Tain as T1
from tkinter import *
def on_select(event=None):
    print('----------------------------')
    feature1.bind('<<ComboboxSelected>>', on_select)
    feature2.bind('<<ComboboxSelected>>', on_select)
    class1.bind('<<ComboboxSelected>>', on_select)
    class2.bind('<<ComboboxSelected>>', on_select)
    f1,f2,f3,f4,c1,c2 = T1.SetClassesAndFeatures(comboboxes[0].get(),comboboxes[1].get(),comboboxes[2].get(),comboboxes[3].get()) #de l event bta3 zrar OK endhy hna okay foll
    w=T1.MSETrain(f1,f2,f3,f4,c1,c2,R2.get(),R.get(),comboboxes[4].get())
    Acc,M=T1.Test(f1,f2,f3,f4,c1,c2,w)
    T1.Draw(f1,f2,f3,f4,w)
    print(Acc)
    print(M)

top = tk.Tk()
top.title("Task1")
top.geometry("712x400")
top.configure(background="black")

comboboxes = []
feature1 = ttk.Combobox(top, values=("X1", "X2", "X3", "X4"), state='readonly')
feature1.set("Select feature 1")
feature1.pack()
comboboxes.append(feature1)
feature2 = ttk.Combobox(top, values=("X1", "X2", "X3", "X4"), state='readonly')
feature2.set("Select feature 2")
feature2.pack()
comboboxes.append(feature2)
class1 = ttk.Combobox(top, values=("Iris Setosa", "Iris Versicolor", "Iris Virginica"), state='readonly')
class1.set("Select class 1")
class1.pack()
comboboxes.append(class1)
class2 = ttk.Combobox(top, values=("Iris Setosa", "Iris Versicolor", "Iris Virginica"), state='readonly')
class2.set("Select class 2")
class2.pack()
comboboxes.append(class2)
bias = ttk.Combobox(top, values=("With Bias", "Without Bias"), state='readonly')
bias.set("Bias")
bias.pack()
comboboxes.append(bias)

var2 = StringVar()
label2 = Label( top, textvariable=var2, relief=RAISED )
var2.set("please, Enter error")
label2.pack()
R2=tk.Entry(top,bd=5)
R2.pack()


var = StringVar()
label = Label( top, textvariable=var, relief=RAISED )
var.set("please, Enter Learning Rate")
label.pack()
R=tk.Entry(top,bd=5)
R.pack()

TrainAndTest = tk.Button(top, text="TrainAndTest !", command=on_select)
TrainAndTest.pack()
top.mainloop()

