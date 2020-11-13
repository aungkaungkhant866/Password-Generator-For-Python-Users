# Coded by Akk
# Contact Info : aungkaungkhant866@gmail.com

import random
chars='abcdefghijklmnopurstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890{[]!@#$%^&*()_+|:<>-=[]\;~`,./}?'
print('>__Welcome to our Password Generator__<')
print('>__We make strongest password for security__<')

while 1:
    password_len = int(input('How long do you want your password to be : '))
    password_count = int(input('How many password do you want to see : '))
    
    for x in range(0,password_count):
        password = ""
        
        for x in range(0,password_len):
            password_chars = random.choice(chars)
            password = password + password_chars
            
        print('Here is your password : ',password)
