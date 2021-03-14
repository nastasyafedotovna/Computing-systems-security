from tkinter import *
from tkinter import messagebox
import numpy as np
import random
import math


def TestMR(n):
    d, s = n - 1, 0
    while d % 2 == 0:
        s += 1
        d //= 2

    rounds = int(math.log2(n))
    for i in range(rounds):
        a = np.random.randint(2, rounds + 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for j in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
            if x == 1:
                return FALSE
        else:
            return FALSE
    return TRUE


def check():
    try:
        n = int(number.get())
        if n <= 3 or n % 2 == 0:
            messagebox.showinfo("Ошибка", "Число должно быть нечетным и больше трех")
            number.delete(0, END)
            return
    except Exception:
        messagebox.showinfo("Ошибка", "Неверный формат ввода")
        number.delete(0, END)
        return

    if TestMR(n):
        result.config(state='normal')
        result.delete(0, END)
        result.insert(0, 'Число вероятно простое')
        result.config(state='disabled')
    else:
        result.config(state='normal')
        result.delete(0, END)
        result.insert(0, 'Число составное')
        result.config(state='disabled')

    return 0


def generate():
    try:
        n = int(bits.get())
        if n <= 0 & n > 512:
            messagebox.showinfo("Ошибка", "Число должно быть положительным")
            number.delete(0, END)
            return
    except Exception:
        messagebox.showinfo("Ошибка", "Неверный формат ввода")
        number.delete(0, END)
        return

    num = random.getrandbits(n)
    while num % 2 == 0:
        num = random.getrandbits(n)

    while TestMR(num) == FALSE:
        num += 2

    prime.config(state='normal')
    prime.delete(0, END)
    prime.insert(0, num)
    prime.config(state='disabled')

    return 0


window = Tk()
window.geometry('500x400')
window.title("Лабораторная работа №3")
window.resizable(0, 0)

number_title = Label(text='Число', font=('ar_Aquaguy', 20))
number_title.place(x=100, y=20)

number = Entry(width=15, font=('ar_Aquaguy', 20), justify=CENTER)
number.place(x=50, y=60)
number.focus()

result = Entry(width=30, font=('ar_Aquaguy', 15), justify=CENTER, state='disabled')
result.place(x=50, y=120)

check = Button(text='Проверить', font=('ar_Aquaguy', 20), command=check)
check.place(x=300, y=40)

bits_title = Label(text='Кол-во бит', font=('ar_Aquaguy', 20))
bits_title.place(x=170, y=180)

bits = Entry(width=8, font=('ar_Aquaguy', 20), justify=CENTER)
bits.place(x=195, y=220)

prime_title = Label(text='Вероятно простое число', font=('ar_Aquaguy', 16))
prime_title.place(x=10, y=280)

prime = Entry(width=15, font=('ar_Aquaguy', 20), justify=CENTER, state='disabled')
prime.place(x=50, y=320)

generate = Button(text='Сгенерировать', font=('ar_Aquaguy', 15), command=generate)
generate.place(x=290, y=320)

window.mainloop()
