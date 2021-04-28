from tkinter import*
from tkinter import messagebox
import random
import math
import time


alphabet = ['А','Б','В','Г','Д','Е','Ж','З','И',\
    'Й','К','Л','М','Н','О','П','Р','С','Т','У','Ф','Х',\
        'Ц','Ч','Ш','Щ','Ъ','Ы','Ь','Э','Ю','Я','а','б','в','г',\
            'д','е','ж','з','и','й','к','л','м','н','о','п','р','с',\
                'т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','ю','э','я']

nums = [str(i) for i in range(16, 80)]                

code_dict = dict(zip(nums, alphabet))
def gcd(a, b):
    #пока b не ноль
    while b:
        #обновляем значения: НОД(a, b)=НОД(b, a mod b)
        a, b = b, a % b
    return a

def euclid(phi, e):

    x1, x2, y1, y2 = 1, 0, 0, 1
    while e:
        x1, x2, y1, y2 = x2, x1 - x2 * (phi // e), y2, y1 - y2 * (phi // e)
        phi, e = e, phi % e

    return y1




def pollard(n):
    x = 2
    y = x
    f = lambda x: ((x**2) - 1) % n
    d = 1
    iteration_count = 0
    while d == 1:
        x = f(x)
        y = f(f(y))
        iteration_count += 1
        d = gcd(abs(y - x), n)
    if 1 < d < n:
        return d, iteration_count


def decrypt(encrypt_data, d, n):
    encrypt_data = str(pow(int(encrypt_data), d, n))
    temp = ''
    for i in range(len(encrypt_data)):
        temp += encrypt_data[i]
        if i % 2 != 0:
            temp += ' '
    temp = temp.split(' ')
    del temp[-1]
    decrypt_data = ''
    for symbol in temp:
        decrypt_data += str(code_dict.get(str(symbol)))   
        
    return decrypt_data


def dec():  
    etext = enc_text.get("1.0", "end-1c")
    if etext=='':
        messagebox.showinfo("Ошибка", "Криптограмма отсутствует!")
        return
    #etext = etext.split(' ')
    d = int(d_entry.get())
    n = int(n_entry.get())
    try:
        d_text = decrypt(etext, d, n)
    except Exception:
        messagebox.showinfo("Ошибка", "Неверный формат криптограммы")
        enc_text.delete("1.0", END)
        dec_text.delete("1.0", END)
        return
    dec_text.delete("1.0", END)
    dec_text.insert("1.0", d_text)



def compute():
    try:
        n = int(n_entry.get())
        e = int(e_entry.get())
        if n <= 0 or e <= 0:
            messagebox.showinfo("Ошибка", "Число должно быть положительным")
            n_entry.delete(0, END)
            e_entry.delete(0, END)
            return
    except Exception:
        messagebox.showinfo("Ошибка", "Неверный формат ввода")
        n_entry.delete(0, END)
        e_entry.delete(0, END)
        return

    start = time.time()
    p, iteration_count = pollard(n)
    finish = time.time() - start
    q = n // p
    phi = (p - 1)*(q - 1)
    d = euclid(phi, e) % phi


    
    d_entry.delete(0, END)
    d_entry.insert(0, d)

    p_entry.delete(0, END)
    p_entry.insert(0, p)

    q_entry.delete(0, END)
    q_entry.insert(0, q)

    phi_entry.delete(0, END)
    phi_entry.insert(0, phi)

    iter_entry.delete(0, END)
    iter_entry.insert(0, iteration_count)

    time_entry.delete(0, END)
    time_entry.insert(0, finish)







#главная форма
window = Tk()
window.geometry('1200x600')
window.title("Лабораторная работа №5")
window.resizable(0, 0)


#Дешифрование
lab_label = Label(text='Дешифрование:', font=('ar_Aquaguy', 15))
lab_label.place(x=450, y=20)

#text_label
enc_label = Label(text='Криптограмма:', font=('ar_Aquaguy', 15))
enc_label.place(x=480, y=60)

#dec_text_label
dec_label = Label(text='Расшифровка:', font=('ar_Aquaguy', 15))
dec_label.place(x=480, y=250)

#text
enc_text = Text(window, width=40, height=5, font=('ar_Aquaguy', 15))
enc_text.place(x=670, y=60)

#enc_text
dec_text = Text(window, width=40, height=5, font=('ar_Aquaguy', 15))
dec_text.place(x=670, y=250)


#open key label
okey_label = Label(text='Введите открытый ключ:', font=('ar_Aquaguy', 15))
okey_label.place(x=20, y=20)

#computing params
params_label = Label(text='Вычисленные параметры:', font=('ar_Aquaguy', 15))
params_label.place(x=20, y=140)

#n
n_label = Label(text='n=', font=('ar_Aquaguy', 15))
n_label.place(x=50, y=60)
n_entry = Entry(width=13, font=('ar_Aquaguy', 15), justify=CENTER)
n_entry.place(x=85, y=60)

#e
e_label = Label(text='e=', font=('ar_Aquaguy', 15))
e_label.place(x=50, y=100)
e_entry = Entry(width=13, font=('ar_Aquaguy', 15), justify=CENTER)
e_entry.place(x=85, y=100)

#p
p_label = Label(text='p=', font=('ar_Aquaguy', 15))
p_label.place(x=50, y=180)
p_entry = Entry(width=13, font=('ar_Aquaguy', 15), justify=CENTER)
p_entry.place(x=85, y=180)


time_label = Label(text='Затраченное время: ', font=('ar_Aquaguy', 15))
time_label.place(x=20, y=400)

time_entry = Entry(width=12, font=('ar_Aquaguy', 15), justify=CENTER)
time_entry.place(x=240, y=400)


iter_entry = Entry(width=7, font=('ar_Aquaguy', 15), justify=CENTER)
iter_entry.place(x=215, y=440)

iter_label = Label(text='Кол-во итераций: ', font=('ar_Aquaguy', 15))
iter_label.place(x=20, y=440)


compute_button = Button(text='Вычислить', width=14,font=('ar_Aquaguy', 15), command=compute)
compute_button.place(x=20,y=340)

dec_button = Button(text='Расшифровать', width=14,font=('ar_Aquaguy', 15), command=dec)
dec_button.place(x=480,y=400)



#q
q_label = Label(text='q=', font=('ar_Aquaguy', 15))
q_label.place(x=50, y=220)
q_entry = Entry(width=13, font=('ar_Aquaguy', 15), justify=CENTER)
q_entry.place(x=85, y=220)


phi_label = Label(text='φ(n)=', font=('ar_Aquaguy', 15))
phi_label.place(x=50, y=260)
phi_entry = Entry(width=11, font=('ar_Aquaguy', 15), justify=CENTER)
phi_entry.place(x=110, y=260)

#d
d_label = Label(text='d=', font=('ar_Aquaguy', 15))
d_label.place(x=50, y=300)
d_entry = Entry(width=13, font=('ar_Aquaguy', 15), justify=CENTER)
d_entry.place(x=85, y=300)


window.mainloop()
