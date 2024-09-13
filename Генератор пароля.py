from random import *


def generate_password(length, _chars):
    a = ""
    for _ in range(length):
        a += choice(_chars)
    return a


digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'

chars = ""

cnt = int(input("Количество паролей для генерации; "))
ln = int(input("Длину одного пароля; "))
digit = input("Включать ли цифры 0123456789? ")
upper = input("Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? ")
lower = input("Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? ")
t_chars = input("Включать ли символы !#$%&*+-=?@^_? ")
f_chars = input("Исключать ли неоднозначные символы il1Lo0O? ")

if upper.lower() == "да":
    chars += uppercase_letters
if lower.lower() == "да":
    chars += lowercase_letters
if digit.lower() == "да":
    chars += digits
if t_chars.lower() == "да":
    chars += punctuation
if f_chars.lower() == "да":
    chars.replace("i", "")
    chars.replace("l", "")
    chars.replace("1", "")
    chars.replace("L", "")
    chars.replace("o", "")
    chars.replace("0", "")
    chars.replace("O", "")

for _ in range(cnt):
    print(generate_password(ln, chars))
