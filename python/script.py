#! /usr/bin/env python3


#task description: написать скрипт заменяющий одну букву на другую в слове

#word1 = str(input("Enter the word: "))
#letter1 = str(input("Enter the letter you want to change in the word: "))
#letter2 = str(input(f"Enter the letter you want to replace with the {letter1} in the word: "))
#word2 = word1.replace(f"{letter1}", f"{letter2}")
#print(f"The result is: {word2}")


#task description: написать генератор пароля

#import random
#
#password = "abcdefghijklopqrstuvwxyz!@#$%^&*()_+".join("ABCDEFGHIJKLOPQRSTUVWXYZ123215498712936789213")
#password_length = int(input("Enter the length of the password: "))
#
#a = "".join(random.sample(password,password_length))
#
#print(f"Your password is: {a} \nSave it in safe place and dont show anybody!")


##task description: отсортировать данный массив из чисел

#numbers = [1, 3, 5, 2, 0, 75, 71, 69, 68, 34, 23, 99]
#print(sorted(numbers))
## + вывести числа меньше определённого
#for num in numbers:
#    if num < 5:
#        print(num)


#task description: посчитать сумму цифр двузначного числа введённого с клавиатуры

#twod_number = input("Enter the two-digit number: ")
#digits_summ  = 0
#for num in twod_number:
#    digits_summ += int(num)
#print(digits_summ)


#task description: зашифровать файл

from cryptography.fernet import Fernet

key = Fernet.generate_key()

cipher = Fernet(key)

with open("./file.txt", "rb") as file:
    data = file.read()
    encrypted_data = cipher.encrypt(data)


with open("./encrypted_file.txt", "wb") as file:
    file.write(encrypted_data)