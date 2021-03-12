from tkinter import *
import numpy as np
import random

worddata = []
wordlen = []
gendata = []
keys_data = []
check_radiobutton = 0

def word_to_bin():
    word = entry_text.get()
    forstring = ''
    for symbol in word:
        worddata.append(format(ord(symbol), 'b'))
        forstring += format(ord(symbol), 'b')
    bin_entry_text.config(state='normal')
    bin_entry_text.insert(0, forstring)
    bin_entry_text.config(state='disabled')

    for i in worddata:
        wordlen.append(len(i))

    return 0

def key():
    k = key_text.get()

    if len(worddata) > len(k):
        for i in range(len(worddata) - len(k)):
            k += k[i]
    elif len(worddata) < len(k):
        new_k = ''
        for i in range(len(k) - len(worddata)):
            new_k += k[i]
        k = new_k

    for_string = ''
    for symbol in k:
        keys_data.append(format(ord(symbol), 'b'))
        for_string += format(ord(symbol), 'b')

    bin_key_text.config(state='normal')
    bin_key_text.insert(0, for_string)
    bin_key_text.config(state='disabled')


def generate():
    generate_text.config(state='normal')
    generate_text.delete(0, END)
    generate_text.config(state='disabled')
    if len(bin_entry_text.get()) % 2 == 0:
        ones = np.ones(int(len(bin_entry_text.get()) / 2), dtype=np.int8)
        zeros = np.zeros(int(len(bin_entry_text.get()) / 2), dtype=np.int8)
        result = np.hstack((ones, zeros))
        random.shuffle(result)

        for_string = ''
        for symbol in result:
            for_string += str(symbol)
        generate_text.config(state='normal')
        generate_text.insert(0, for_string)
        generate_text.config(state='disabled')

        diff = 0
        for l in range(len(wordlen)):
            gendata.append(for_string[diff:(wordlen[l] + diff)])
            diff += wordlen[l]

    else:
        ones = np.ones(int(len(bin_entry_text.get()) / 2) + 1, dtype=np.int8)
        zeros = np.zeros(int(len(bin_entry_text.get()) / 2), dtype=np.int8)
        result = np.hstack((ones, zeros))
        random.shuffle(result)

        for_string = ''
        for symbol in result:
            for_string += str(symbol)
        generate_text.config(state='normal')
        generate_text.insert(0, for_string)
        generate_text.config(state='disabled')

        diff = 0
        for l in range(len(wordlen)):
            gendata.append(for_string[diff:(wordlen[l] + diff)])
            diff += wordlen[l]

    return 0


def generate_clear():
    generate_text.config(state='normal')
    generate_text.delete(0, END)
    generate_text.config(state='disabled')
    return 0


def key_clear():
    key_text.delete(0, END)
    bin_key_text.config(state='normal')
    bin_key_text.delete(0, END)
    bin_key_text.config(state='disabled')
    return 0

def encrypt():
    encrypt_text.config(state='normal')
    encrypt_text.delete(0, END)
    encrypt_text.config(state='disabled')

    result = []
    bin_result = ''
    word_result = ''

    check = var.get()
    if check == 1:
        for i in range(len(worddata)):
            result.append(int(worddata[i], base=2) ^ int(gendata[i], base=2))
            bin_result += format(int(worddata[i], base=2) ^ int(gendata[i], base=2), 'b')
            word_result += chr(int(worddata[i], base=2) ^ int(gendata[i], base=2))
    elif check == 2:
        for i in range(len(worddata)):
            result.append(int(worddata[i], base=2) ^ int(keys_data[i], base=2))
            bin_result += format(int(worddata[i], base=2) ^ int(keys_data[i], base=2), 'b')
            word_result += chr(int(worddata[i], base=2) ^ int(keys_data[i], base=2))

    encrypt_text.config(state='normal')
    encrypt_text.insert(0, word_result)
    encrypt_text.config(state='disabled')

    bin_encrypt_text.config(state='normal')
    bin_encrypt_text.insert(0, bin_result)
    bin_encrypt_text.config(state='disabled')

    return 0

def decrypt():
    decrypt_text.delete(0, END)

    word = encrypt_text.get()
    encrypt_data = []
    for symbol in word:
        encrypt_data.append(format(ord(symbol), 'b'))

    result = []
    bin_result = ''
    word_result = ''

    check = var.get()
    if check == 1:
        for i in range(len(encrypt_data)):
            result.append(int(encrypt_data[i], base=2) ^ int(gendata[i], base=2))
            bin_result += format(int(encrypt_data[i], base=2) ^ int(gendata[i], base=2), 'b')
            word_result += chr(int(encrypt_data[i], base=2) ^ int(gendata[i], base=2))
    elif check == 2:
        for i in range(len(encrypt_data)):
            result.append(int(encrypt_data[i], base=2) ^ int(keys_data[i], base=2))
            bin_result += format(int(encrypt_data[i], base=2) ^ int(keys_data[i], base=2), 'b')
            word_result += chr(int(encrypt_data[i], base=2) ^ int(keys_data[i], base=2))

    decrypt_text.config(state='normal')
    decrypt_text.insert(0, word_result)
    decrypt_text.config(state='disabled')

    bin_decrypt_text.config(state='normal')
    bin_decrypt_text.insert(0, bin_result)
    bin_decrypt_text.config(state='disabled')

    return 0

window = Tk()
window.geometry('800x700')
window.title("XOR")
window.resizable(0, 0)

entry_title = Label(text='Исходное слово', font=('ar_Aquaguy', 20))
entry_title.place(x=280, y=10)

entry_text = Entry(width=20, font=('ar_Aquaguy', 20), justify=CENTER)
entry_text.place(x=100, y=50)
entry_text.focus()

bin_entry_text = Entry(width=20, font=('ar_Aquaguy', 20), justify=CENTER, state='disabled')
bin_entry_text.place(x=440, y=50)

generate_title = Label(text='Генерация ключа', font=('ar_Aquaguy', 20))
generate_title.place(x=270, y=100)

generate_text = Entry(width=20, font=('ar_Aquaguy', 20), justify=CENTER, state='disabled')
generate_text.place(x=100, y=150)

generate_button = Button(text='Сгенерировать', font=('ar_Aquaguy', 15), command=generate)
generate_button.place(x=400, y=150)

clear_button = Button(text='Очистить', font=('ar_Aquaguy', 15), command=generate_clear)
clear_button.place(x=600, y=150)

key_title = Label(text='Ввод ключа', font=('ar_Aquaguy', 20))
key_title.place(x=310, y=200)

key_text = Entry(width=20, font=('ar_Aquaguy', 20), justify=CENTER)
key_text.place(x=100, y=250)

bin_key_text = Entry(width=20, font=('ar_Aquaguy', 20), justify=CENTER, state='disabled')
bin_key_text.place(x=440, y=250)

key_clear_button = Button(text='Очистить', font=('ar_Aquaguy', 15), command=key_clear)
key_clear_button.place(x=345, y=300)

encrypt_title = Label(text='Зашифровка', font=('ar_Aquaguy', 20))
encrypt_title.place(x=310, y=360)

encrypt_text = Entry(width=20, font=('ar_Aquaguy', 20), justify=CENTER, state='disabled')
encrypt_text.place(x=100, y=410)

bin_encrypt_text = Entry(width=20, font=('ar_Aquaguy', 20), justify=CENTER, state='disabled')
bin_encrypt_text.place(x=440, y=410)

encrypt_button = Button(text='Зашифровать', font=('ar_Aquaguy', 15), command=encrypt)
encrypt_button.place(x=325, y=460)

decrypt_title = Label(text='Дешифровка', font=('ar_Aquaguy', 20))
decrypt_title.place(x=310, y=530)

decrypt_text = Entry(width=20, font=('ar_Aquaguy', 20), justify=CENTER, state='disabled')
decrypt_text.place(x=100, y=580)

bin_decrypt_text = Entry(width=20, font=('ar_Aquaguy', 20), justify=CENTER, state='disabled')
bin_decrypt_text.place(x=440, y=580)

decrypt_button = Button(text='Дешифровать', font=('ar_Aquaguy', 15), command=decrypt)
decrypt_button.place(x=325, y=630)

entry_to_bin = Button(text='-------->', command=word_to_bin)
entry_to_bin.place(x=372, y=55)

key_to_bin = Button(text='-------->', command=key)
key_to_bin.place(x=372, y=255)

var = IntVar()
var.set(0)
check_gen = Radiobutton(value=1, variable=var).place(x=50, y=155)
check_key = Radiobutton(value=2, variable=var).place(x=50, y=257)

window.mainloop()
