import re

def check_password(password):
    if (len(password) >= 8 and
        re.search(r'[a-z]', password) and
        re.search(r'[A-Z]', password) and
        re.search(r'[0-9]', password) and
        re.search(r'[@$!%*?&#]', password)): 
        return True
    return False

def check_passwords(passwords):
    for password in passwords:
        if check_password(password):
            print(f"Пароль '{password}' соответствует требованиям.")
        else:
            print(f"Пароль '{password}' не соответствует требованиям.")

passwords = ['Password123!', 'simplepass', 'P@ssw0rd', 'WeakPass', 'Str0ng@123']
check_passwords(passwords)