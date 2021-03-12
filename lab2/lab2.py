from tkinter import*
from tkinter import messagebox


def Euclid():
    NOD_text.config(state='normal')
    NOD_text.delete(0, END)
    NOD_text.config(state='disabled')
    try:
        a = int(A_text.get())
        b = int(B_text.get())
        if a <= 0 & b <= 0:
            messagebox.showinfo("Ошибка", "Числа должны быть положительными")
            A_text.delete(0, END)
            B_text.delete(0, END)
            return
    except Exception:
        messagebox.showinfo("Ошибка", "Неверный формат ввода")
        A_text.delete(0, END)
        B_text.delete(0, END)
        return

    x1, x2, y1, y2 = 1, 0, 0, 1
    while b:
        x1, x2, y1, y2 = x2, x1 - x2 * (a // b), y2, y1 - y2 * (a // b)
        a, b = b, a % b

    X_text.config(state='normal')
    X_text.insert(0, x1)
    X_text.config(state='disabled')

    Y_text.config(state='normal')
    Y_text.insert(0, y1)
    Y_text.config(state='disabled')

    NOD_text.config(state='normal')
    NOD_text.insert(0, a)
    NOD_text.config(state='disabled')
    return 0


def Stepen():
    try:
        a = int(a_text.get())
        b = int(b_text.get())
        n = int(n_text.get())
        if a <= 0 & b <= 0 & n <= 0:
            messagebox.showinfo("Ошибка", "Числа должны быть положительными")
            a_text.delete(0, END)
            b_text.delete(0, END)
            n_text.delete(0, END)
            return
    except Exception:
        messagebox.showinfo("Ошибка", "Неверный формат ввода")
        a_text.delete(0, END)
        b_text.delete(0, END)
        n_text.delete(0, END)
        return

    c = 1
    while b:
        if b % 2 == 0:
            b /= 2
            a = a**2 % n
        else:
            b -= 1
            c = (c*a) % n

    z_text.config(state='normal')
    z_text.delete(0, END)
    z_text.insert(0, c)
    z_text.config(state='disabled')
    return 0


window = Tk()
window.geometry('800x500')
window.title("Расширенный алгоритм евклида и быстрое возведение в степень")
window.resizable(0, 0)

A_title = Label(text='A', font=('ar_Aquaguy', 20))
A_title.place(x=100, y=10)

A_text = Entry(width=10, font=('ar_Aquaguy', 20), justify=CENTER)
A_text.place(x=70, y=50)
A_text.focus()

B_title = Label(text='B', font=('ar_Aquaguy', 20))
B_title.place(x=280, y=10)

B_text = Entry(width=10, font=('ar_Aquaguy', 20), justify=CENTER)
B_text.place(x=250, y=50)

X_title = Label(text='X', font=('ar_Aquaguy', 20))
X_title.place(x=100, y=100)

X_text = Entry(width=10, font=('ar_Aquaguy', 20), justify=CENTER, state='disabled')
X_text.place(x=70, y=150)

Y_title = Label(text='Y', font=('ar_Aquaguy', 20))
Y_title.place(x=280, y=100)

Y_text = Entry(width=10, font=('ar_Aquaguy', 20), justify=CENTER, state='disabled')
Y_text.place(x=250, y=150)

NOD_title = Label(text='НОД(A,B)', font=('ar_Aquaguy', 20))
NOD_title.place(x=450, y=50)

NOD_text = Entry(width=10, font=('ar_Aquaguy', 20), justify=CENTER, state='disabled')
NOD_text.place(x=450, y=150)

euclid = Button(text='Евклид', font=('ar_Aquaguy', 15), command=Euclid)
euclid.place(x=630, y=100)

a_title = Label(text='A', font=('ar_Aquaguy', 20))
a_title.place(x=100, y=310)

a_text = Entry(width=10, font=('ar_Aquaguy', 20), justify=CENTER)
a_text.place(x=70, y=350)

b_title = Label(text='B', font=('ar_Aquaguy', 20))
b_title.place(x=280, y=310)

b_text = Entry(width=10, font=('ar_Aquaguy', 20), justify=CENTER)
b_text.place(x=250, y=350)

n_title = Label(text='N', font=('ar_Aquaguy', 20))
n_title.place(x=460, y=310)

n_text = Entry(width=10, font=('ar_Aquaguy', 20), justify=CENTER)
n_text.place(x=430, y=350)

stepen = Button(text='Степень', font=('ar_Aquaguy', 15), command=Stepen)
stepen.place(x=630, y=300)

z_title = Label(text='Z', font=('ar_Aquaguy', 20))
z_title.place(x=630, y=370)

z_text = Entry(width=10, font=('ar_Aquaguy', 20), justify=CENTER, state='disabled')
z_text.place(x=615, y=410)

window.mainloop()