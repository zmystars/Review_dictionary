# -*- coding: utf-8 -*-
"""
程序名称：简易单词翻译器
题目要求：
让用户输入英语单词或者中文后，单机“中翻英”显示英文，单机”英翻中“显示中文
"""


def ctoe():
    i = entry.get()
    ans = ""
    for k, v in dictionary.items():
        if v == i:
            ans = k
            break
    if ans:
        label.config(text=ans)
    else:
        label.config(text="找不到["+i+"]")


def etoc():
    i = entry.get()  # 获取entry组件输入的内容
    ans = dictionary.get(i, "找不到["+i+"]")
    label.config(text=ans)  # 在label组件显示文字


def clear():
    entry.delete(0, "end")
    label.config(text="")


dictionary = {"bird": "鸟", "cat": "猫", "dog": "狗", "pig": "猪"}


# GUI 界面
import tkinter as tk
win = tk.Tk()
win.title("简易单词翻译器")

frame = tk.Frame(win)
frame.pack(padx=5, pady=5)
frame1 = tk.Frame(win)
frame1.pack(padx=5, pady=5)

entry = tk.Entry(frame, bg="#99ffcc", borderwidth=3)
entry.config(width=10)
entry.grid(column=0, row=0)

label = tk.Label(frame, bg="#ffffcc", text="")
label.config(width=10)
label.grid(column=1, row=0)

btnCtoe = tk.Button(frame1, text="中翻英", command=ctoe)
btnCtoe.grid(column=0, row=0)
btnEtoc = tk.Button(frame1, text="英翻中", command=etoc)
btnEtoc.grid(column=1, row=0)
btnClear = tk.Button(frame1, text="清除", command=clear)
btnClear.grid(column=2, row=0)

win.mainloop()
