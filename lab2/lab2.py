from tkinter import*
from tkinter import messagebox


#функция нахождения НОД, с помощью расширенного алгоритма Евклида
def gcd():
    #проверяем, записывают ли числа
    try:
        #записываем числа
        a = int(A_text.get())
        b = int(B_text.get())
        #на случай записи отрицательных чисел
        if a <= 0 & b <= 0:
            #ловим ошибку, очищаем поля А и В, делаем return
            messagebox.showinfo("Ошибка", "Числа должны быть положительными")
            A_text.delete(0, END)
            B_text.delete(0, END)
            return


    #записались не числа
    except Exception:
        #ловим ошибку, очищаем поля А и В, делаем return
        messagebox.showinfo("Ошибка", "Неверный формат ввода")
        A_text.delete(0, END)
        B_text.delete(0, END)
        return

    #начальные значения коэффициентов(0 и 1 шаги)
    x0, x1, y0, y1 = 1, 0, 0, 1
    #пока b не ноль
    while b:
        #вычисление коэффициентов
        #x_i = y_i+1
        #y_i = x_i+1 - y_i+1*(A div B)
        x0, x1, y0, y1 = x1, x0 - x1 * (a // b), y1, y0 - y1 * (a // b)
        #обновляем значения: НОД(a, b)=НОД(b, a mod b)
        a, b = b, a % b

    #делаем entry активным, очищаем старое, записываем новое, отключаем entry
    X_text.config(state='normal')
    X_text.delete(0, END)
    X_text.insert(0, x0)
    X_text.config(state='disabled')

    #делаем entry активным, очищаем старое, записываем новое, отключаем entry
    Y_text.config(state='normal')
    Y_text.delete(0, END)
    Y_text.insert(0, y0)
    Y_text.config(state='disabled')

    #делаем entry активным, очищаем старое, записываем новое, отключаем entry
    NOD_text.config(state='normal')
    NOD_text.delete(0, END)
    NOD_text.insert(0, a)
    NOD_text.config(state='disabled')
    return 0


def power():
    #ловим не числа
    try:
        #записываем числа
        a = int(a_text.get())
        b = int(b_text.get())
        n = int(n_text.get())
        #проверяем, чтобы они были положительные
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

#Инициализируем главную форму
window = Tk()
window.geometry('800x500')
window.title("Лабораторная работа №2")
window.resizable(0, 0)
#--------------Интерфейс для алгоритма Евклида----------------------------------

#Надпись "А"
A_title = Label(text='A', font=('ar_Aquaguy', 20))
A_title.place(x=100, y=10)

#Поле со значением А
A_text = Entry(width=10, font=('ar_Aquaguy', 20), justify=CENTER)
A_text.place(x=70, y=50)
A_text.focus()

#Надпись "В"
B_title = Label(text='B', font=('ar_Aquaguy', 20))
B_title.place(x=280, y=10)

#Поле со значением В
B_text = Entry(width=10, font=('ar_Aquaguy', 20), justify=CENTER)
B_text.place(x=250, y=50)

#Надпись "Х"
X_title = Label(text='X', font=('ar_Aquaguy', 20))
X_title.place(x=100, y=100)

#Поле со значением х
X_text = Entry(width=10, font=('ar_Aquaguy', 20), justify=CENTER, state='disabled')
X_text.place(x=70, y=150)

#Надпись "Y"
Y_title = Label(text='Y', font=('ar_Aquaguy', 20))
Y_title.place(x=280, y=100)

#Поле со значением у
Y_text = Entry(width=10, font=('ar_Aquaguy', 20), justify=CENTER, state='disabled')
Y_text.place(x=250, y=150)

#Надпись "НОД(А, В)"
NOD_title = Label(text='НОД(A,B)', font=('ar_Aquaguy', 20))
NOD_title.place(x=450, y=50)

#Поле со значением НОД(А, В)
NOD_text = Entry(width=10, font=('ar_Aquaguy', 20), justify=CENTER, state='disabled')
NOD_text.place(x=450, y=150)

#Кнопка запуска процесса нахождения НОД(А, В) расширенным алгоритмом Евклида
euclid = Button(text='Евклид', font=('ar_Aquaguy', 15), command=gcd)
euclid.place(x=630, y=100)



#--------------Интерфес для алгоритма быстрого возведения в степень-------------

#Надпись "А"
a_title = Label(text='A', font=('ar_Aquaguy', 20))
a_title.place(x=100, y=310)

#Поле со значением А
a_text = Entry(width=10, font=('ar_Aquaguy', 20), justify=CENTER)
a_text.place(x=70, y=350)

#Надпись "В"
b_title = Label(text='B', font=('ar_Aquaguy', 20))
b_title.place(x=280, y=310)

#Поле со значением В
b_text = Entry(width=10, font=('ar_Aquaguy', 20), justify=CENTER)
b_text.place(x=250, y=350)

#Надпись "N"
n_title = Label(text='N', font=('ar_Aquaguy', 20))
n_title.place(x=460, y=310)

#Поле со значением N
n_text = Entry(width=10, font=('ar_Aquaguy', 20), justify=CENTER)
n_text.place(x=430, y=350)

#Кнопка запуска процесса быстрого возведения в степень
power = Button(text='Степень', font=('ar_Aquaguy', 15), command=power)
power.place(x=630, y=300)

#Надпись "Z"
z_title = Label(text='Z', font=('ar_Aquaguy', 20))
z_title.place(x=630, y=370)

#Поле со значеним z
z_text = Entry(width=10, font=('ar_Aquaguy', 20), justify=CENTER, state='disabled')
z_text.place(x=615, y=410)

#запуск формы
window.mainloop()
