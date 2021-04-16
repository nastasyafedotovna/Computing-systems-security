from tkinter import*
from tkinter import messagebox
import random
import math




def gcd(a, b):
    #пока b не ноль
    while b:
        #обновляем значения: НОД(a, b)=НОД(b, a mod b)
        a, b = b, a % b
    if a == 1:
        return 1
    else:
        return 0    


def encrypt(word, e, n):
    encrypt_data = []

    for symbol in word:
        encrypt_data.append(pow(ord(symbol), e, n))
    return encrypt_data


def euclid(phi, e):

    x1, x2, y1, y2 = 1, 0, 0, 1
    while e:
        x1, x2, y1, y2 = x2, x1 - x2 * (phi // e), y2, y1 - y2 * (phi // e)
        phi, e = e, phi % e

    return y1

def decrypt(encrypt_data, d, n):
    
    decrypt_data = ''
    for symbol in encrypt_data:
        #print(symbol)
        decrypt_data += str((chr(pow(int(symbol), d, n) % 1500)))
    return decrypt_data





def generate(bits):
    number = random.getrandbits(bits)
    while number % 2 == 0:
        number = random.getrandbits(bits)

    if number < 3:
        return    

    while TestMR(number) == 0:
        number += 2

    return number

def get_e(n, phi):
    l = n.bit_length()//3
    e = random.getrandbits(l)
    while gcd(e, phi) == 0:
        e = random.getrandbits(l)

    return e

     

def TestMR(n):
    # n-1 = 2^s * d (d нечётное)
    d, s = n - 1, 0
    while d % 2 == 0:
        s += 1
        d //= 2

    #кол-во итераций log2(n)
    rounds = int(math.log2(n))
    for _ in range(rounds):
        #рандомное число в отрезке [2, r+1]
        a = random.randint(2, rounds + 2)
        #x = a^d mod n
        x = pow(a, d, n)
        #если x принадлежит мн-ву {1, n-1}, то а - свидетель простоты
        if x == 1 or x == n - 1:
            continue
        #ищем n-1 в ge(s-1):
        for _ in range(s-1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
            if x == 1:
                return 0
        #если цикл не нашёл n-1 в пос-ти
        else:
            return 0
    return 1


def enc_data():
    text = org_text.get("1.0", "end-1c")
    e = int(e_entry.get())
    n = int(n_entry.get())
    e_text = encrypt(text, e, n)

    enc_text.delete("1.0", END)
    enc_text.insert("1.0", e_text)

def dec_data():
    
    etext = enc_text.get("1.0", "end-1c")
    if etext=='':
        messagebox.showinfo("Ошибка", "Криптограмма отсутствует!")
        return
    etext = etext.split(' ')
    d = int(d_entry.get())
    n = int(n_entry.get())
    d_text = decrypt(etext, d, n)
    dec_text.delete("1.0", END)
    dec_text.insert("1.0", d_text)





def generate_params():
    try:
        bits = int(bits_entry.get())
        if bits < 8:
            messagebox.showinfo("Ошибка", "Введите хотя бы 8 бит :)")
            bits_entry.delete(0, END)
            return
        if bits < 0:
            messagebox.showinfo("Ошибка", "Число должно быть положительным")
            bits_entry.delete(0, END)
            return
    except Exception:
        messagebox.showinfo("Ошибка", "Неверный формат ввода")
        bits_entry.delete(0, END)
        return
    
    
    p = generate(bits)
    if p is None:
        messagebox.showinfo("Ошибка", "Число p < 3, попробуйте ещё раз или введите болльшее кол-во бит")
        return


    q = generate(bits)
    if q is None:
        messagebox.showinfo("Ошибка", "Число q < 3, попробуйте ещё раз или введите большее кол-во бит")
        return

    n=q*p

        
    phi = (p - 1) * (q - 1)
    e = get_e(n, phi)
    d = euclid(phi, e) % phi

    p_entry.delete(0, END)
    p_entry.insert(0, p)

    q_entry.delete(0, END)
    q_entry.insert(0, q)

    n_entry.delete(0, END)
    n_entry.insert(0, n)

    phi_entry.delete(0, END)
    phi_entry.insert(0, phi)

    e_entry.delete(0, END)
    e_entry.insert(0, e)

    d_entry.delete(0, END)
    d_entry.insert(0, d)



#главная форма
window = Tk()
window.geometry('1200x600')
window.title("Лабораторная работа №4")
window.resizable(0, 0)


#Шифрование/Дешифрование
lab_label = Label(text='Шифрование/Дешифрование:', font=('ar_Aquaguy', 15))
lab_label.place(x=450, y=20)

#text_label
org_label = Label(text='Исходный текст:', font=('ar_Aquaguy', 15))
org_label.place(x=480, y=60)

#enc_text_label
enc_label = Label(text='Криптограмма:', font=('ar_Aquaguy', 15))
enc_label.place(x=480, y=250)

#dec_text_label
dec_label = Label(text='Расшифровка:', font=('ar_Aquaguy', 15))
dec_label.place(x=480, y=440)

#text
org_text = Text(window, width=40, height=5, font=('ar_Aquaguy', 15))
org_text.place(x=670, y=60)

#enc_text
enc_text = Text(window, width=40, height=5, font=('ar_Aquaguy', 15))
enc_text.place(x=670, y=250)

#dec_text
dec_text = Text(window, width=40, height=5, font=('ar_Aquaguy', 15))
dec_text.place(x=670, y=440)

#params label
params_label = Label(text='Параметры:', font=('ar_Aquaguy', 15))
params_label.place(x=20, y=20)

#bits
bits_label = Label(text='Кол-во бит=', font=('ar_Aquaguy', 15))
bits_label.place(x=50, y=60)
bits_entry = Entry(width=5, font=('ar_Aquaguy', 15), justify=CENTER)
bits_entry.place(x=185, y=60)
bits_entry.focus()

#p
p_label = Label(text='p=', font=('ar_Aquaguy', 15))
p_label.place(x=50, y=100)
p_entry = Entry(width=13, font=('ar_Aquaguy', 15), justify=CENTER)
p_entry.place(x=85, y=100)

#q
q_label = Label(text='q=', font=('ar_Aquaguy', 15))
q_label.place(x=50, y=140)
q_entry = Entry(width=13, font=('ar_Aquaguy', 15), justify=CENTER)
q_entry.place(x=85, y=140)

#n
n_label = Label(text='n=', font=('ar_Aquaguy', 15))
n_label.place(x=50, y=180)
n_entry = Entry(width=13, font=('ar_Aquaguy', 15), justify=CENTER)
n_entry.place(x=85, y=180)


#phi(n)
phi_label = Label(text='φ(n)=', font=('ar_Aquaguy', 15))
phi_label.place(x=50, y=220)
phi_entry = Entry(width=11, font=('ar_Aquaguy', 15), justify=CENTER)
phi_entry.place(x=110, y=220)

#e
e_label = Label(text='e=', font=('ar_Aquaguy', 15))
e_label.place(x=50, y=260)
e_entry = Entry(width=13, font=('ar_Aquaguy', 15), justify=CENTER)
e_entry.place(x=85, y=260)

#d
d_label = Label(text='d=', font=('ar_Aquaguy', 15))
d_label.place(x=50, y=300)
d_entry = Entry(width=13, font=('ar_Aquaguy', 15), justify=CENTER)
d_entry.place(x=85, y=300)

#generator button
gen_params = Button(text='Сгенерировать', width=14,font=('ar_Aquaguy', 15), command=generate_params)
gen_params.place(x=50, y=350)

#enc_button
enc_button = Button(text='Зашифровать', width=14,font=('ar_Aquaguy', 15), command=enc_data)
enc_button.place(x=670, y=190)

#dec_button
dec_button = Button(text='Дешифровать', width=14,font=('ar_Aquaguy', 15), command=dec_data)
dec_button.place(x=670, y=380)

window.mainloop()
