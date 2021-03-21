from tkinter import*
from tkinter import messagebox
import random
import math


def gcd(a, b):
    #пока b не ноль
    while b:
        #обновляем значения: НОД(a, b)=НОД(b, a mod b)
        a, b = b, a % b
    return a


def Legendre(a, p):
    if a == 0 or a == 1:
        return a
    if a % 2 == 0:
        r = Legendre(a // 2, p)
        if p * p - 1 & 8 != 0:
            r *= -1
    else:
        r = Legendre(p % a, a)
        if (a - 1) * (p - 1) & 4 != 0:
            r *= -1
    return r

def TestSS(num):
    rounds = int(math.log2(num))
    for i in range(rounds):
        a = random.randint(2, num)
        f = pow(a, (num - 1) // 2, num)
        s = Legendre(a, num)
        if gcd(a, num) > 1 or f != s % num:
            return FALSE
    return TRUE



def TestMR(n):
    # n-1 = 2^s * d (d нечётное)
    d, s = n - 1, 0
    while d % 2 == 0:
        s += 1
        d //= 2

    #кол-во итераций log2(n)
    rounds = int(math.log2(n))
    for i in range(rounds):
        #рандомное число в отрезке [2, r+1]
        a = random.randint(2, rounds + 2)
        #x = a^d mod n
        x = pow(a, d, n)
        #если x принадлежит мн-ву {1, n-1}, то а - свидетель простоты
        if x == 1 or x == n - 1:
            continue
        #ищем n-1 в ge(s-1):
        for j in range(s-1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
            if x == 1:
                return FALSE
        #если цикл не нашёл n-1 в пос-ти
        else:
            return FALSE
    return TRUE


def checkSS():
    #ловим ввод НЕ числа
    try:
        n = int(numberSS.get())
        #четное число n < 3
        if n < 3 or n % 2 == 0:
            messagebox.showinfo("Ошибка", "Число должно быть нечетным и не меньше трех")
            numberSS.delete(0, END)
            return
    except Exception:
        messagebox.showinfo("Ошибка", "Неверный формат ввода")
        numberSS.delete(0, END)
        return

    if TestSS(n):
        resultSS.config(state='normal')
        resultSS.delete(0, END)
        resultSS.insert(0, 'Число вероятно простое')
        resultSS.config(state='disabled')
    else:
        resultSS.config(state='normal')
        resultSS.delete(0, END)
        resultSS.insert(0, 'Число составное')
        resultSS.config(state='disabled')

    return 0


def checkMR():
    #ловим ввод НЕ числа
    try:
        n = int(number.get())
        #четное число n < 3
        if n < 3 or n % 2 == 0:
            messagebox.showinfo("Ошибка", "Число должно быть нечетным и не меньше трех")
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
        if n < 0:
            messagebox.showinfo("Ошибка", "Число должно быть положительным")
            bits.delete(0, END)
            return
    except Exception:
        messagebox.showinfo("Ошибка", "Неверный формат ввода")
        bits.delete(0, END)
        return

    num = random.getrandbits(n)
    while num % 2 == 0:
        num = random.getrandbits(n)

    if num < 3:
        messagebox.showinfo("Упс", "Сгенерированное число меньше трёх, попробуйте ввести большее кол-во бит")
        bits.delete(0, END)
        return

    while TestMR(num) == FALSE:
        num += 2

    prime.config(state='normal')
    prime.delete(0, END)
    prime.insert(0, num)
    #prime.config(state='disabled')

    return 0

def generateSS():
    try:
        n = int(bitsSS.get())
        if n < 0:
            messagebox.showinfo("Ошибка", "Число должно быть положительным")
            bitsSS.delete(0, END)
            return
    except Exception:
        messagebox.showinfo("Ошибка", "Неверный формат ввода")
        bitsSS.delete(0, END)
        return

    num = random.getrandbits(n)
    while num % 2 == 0:
        num = random.getrandbits(n)

    if num < 3:
        messagebox.showinfo("Упс", "Сгенерированное число меньше трёх, попробуйте ввести большее кол-во бит")
        bitsSS.delete(0, END)
        return

    while TestSS(num) == FALSE:
        num += 2

    primeSS.config(state='normal')
    primeSS.delete(0, END)
    primeSS.insert(0, num)
    #primeSS.config(state='disabled')

    return 0





#главная форма
window = Tk()
window.geometry('1200x400')
window.title("Лабораторная работа №3")
window.resizable(0, 0)


number_title = Label(text='Число(МР)', font=('ar_Aquaguy', 20))
number_title.place(x=150, y=20)

number_titleSS = Label(text='Число(СШ)', font=('ar_Aquaguy', 20))
number_titleSS.place(x=700, y=20)

#Вводим число
number = Entry(width=15, font=('ar_Aquaguy', 20), justify=CENTER)
number.place(x=50, y=60)
number.focus()

#Вводим число
numberSS = Entry(width=15, font=('ar_Aquaguy', 20), justify=CENTER)
numberSS.place(x=650, y=60)


#Вывод результата
result = Entry(width=30, font=('ar_Aquaguy', 15), justify=CENTER, state='disabled')
result.place(x=50, y=120)

#Вывод результата
resultSS = Entry(width=30, font=('ar_Aquaguy', 15), justify=CENTER, state='disabled')
resultSS.place(x=650, y=120)

#Кнопка проверки МР
check = Button(text='Проверить', font=('ar_Aquaguy', 20), command=checkMR)
check.place(x=310, y=57)

#Кнопка проверки СШ
checkSS = Button(text='Проверить', font=('ar_Aquaguy', 20), command=checkSS)
checkSS.place(x=910, y=57)

#надпись "Кол-во бит(МР)"
bits_title = Label(text='Кол-во бит(МР)', font=('ar_Aquaguy', 20))
bits_title.place(x=190, y=180)

#надпись "Кол-во бит(СШ)"
bits_titleSS = Label(text='Кол-во бит(СШ)', font=('ar_Aquaguy', 20))
bits_titleSS.place(x=690, y=180)


#надпись "Кол-во бит"
bits_title = Label(text='Кол-во бит', font=('ar_Aquaguy', 20))
bits_title.place(x=190, y=180)

#Вводим кол-во бит
bits = Entry(width=8, font=('ar_Aquaguy', 20), justify=CENTER)
bits.place(x=195, y=220)

#Вводим кол-во бит
bitsSS = Entry(width=8, font=('ar_Aquaguy', 20), justify=CENTER)
bitsSS.place(x=695, y=220)

#надпись "вероятно простое число"
prime_title = Label(text='Вероятно простое число(МР)', font=('ar_Aquaguy', 16))
prime_title.place(x=40, y=280)


#надпись "вероятно простое число"
prime_title = Label(text='Вероятно простое число(CШ)', font=('ar_Aquaguy', 16))
prime_title.place(x=640, y=280)

#вывод простого числа
prime = Entry(width=15, font=('ar_Aquaguy', 20), justify=CENTER, state='disabled')
prime.place(x=50, y=320)

#вывод простого числа
primeSS = Entry(width=15, font=('ar_Aquaguy', 20), justify=CENTER, state='disabled')
primeSS.place(x=650, y=320)

#кнопка для запуска генерирования
generate = Button(text='Сгенерировать(МР)', font=('ar_Aquaguy', 15), command=generate)
generate.place(x=290, y=320)


#кнопка для запуска генерирования
generateSS = Button(text='Сгенерировать(СШ)', font=('ar_Aquaguy', 15), command=generateSS)
generateSS.place(x=910, y=320)


window.mainloop()
