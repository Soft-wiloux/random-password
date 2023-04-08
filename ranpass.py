import random
import os
from termcolor import colored

def header():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(" ")
    print(colored("random-password", "cyan"))
    print(" ")
    print(colored("--------------------", "yellow"))

def generate_password(characters):
    password = ""
    for i in range(characters):
        password += random.choice("abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?")
    return password

header()
lang_s = input(colored("Language: [1 ES / 2 EN] ", "yellow"))

if lang_s == "1":
    password_c = int(input(colored("Hola! ¿Cuántos caracteres quieres que tenga tu contraseña? ", "green")))
    password = generate_password(password_c)
    print(colored(f"\nTu contraseña generada es: {password}", "green"))

elif lang_s == "2":
    password_c = int(input(colored("Hello! How many characters do you want your password to have? ", "green")))
    password = generate_password(password_c)
    print(colored(f"\nYour generated password is: {password}", "green"))

else:
    print(colored("Invalid language choice.", "red"))