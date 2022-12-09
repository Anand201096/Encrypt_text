import os
import time
import sys
from cfonts import render
from termcolor import colored

banner = render("encrypt_text", colors=['blue', 'yellow'], align='center')
print(banner)

print('Warning: It performs only simple encryption...')

print("======================================================")


cred='Coded by:--> @AnandGurav'
print(colored(cred,'red'))
lang='You are doing safe encryption.'
print(colored(lang,'green'))
print("======================================================")

ann = str(input(colored("Enter the method (Encrypt / Decrypt): ", 'red')))

key = 'abcdefghijklmnopqrstuvwxyz'

if "encrypt" in ann:

    def encrypt(n, plaintext):

        """Encrypt the string and return the ciphertext"""

        result = ''



        for l in plaintext.lower():

            try:

                i = (key.index(l) + n) % 26

                result += key[i]

            except ValueError:

                result += l



        return result.lower()
    offset = 5   
    text = str(input(colored('[*]  Enter a text or sentence:--> ','red')))   
    encrypted = encrypt(offset, text)
    out= colored('[+] your encrypted text is here:--> ', 'green')
    print(colored(out,'green'),encrypted)
    

elif "decrypt" in ann:
    def decrypt(n, ciphertext):

        """Decrypt the string and return the plaintext"""

        result = ''



        for l in ciphertext:

            try:

                i = (key.index(l) - n) % 26

                result += key[i]

            except ValueError:

                result += l



        return result
    offset = 5
    text = str(input(colored('[*]  Enter a text or sentence:--> ','red')))
    decrypted = decrypt(offset, text)
    out= colored('[+] your decrypted text is here:--> ', 'green')
    print(colored(out,'green'),decrypted)
    

else:
    pass





time.sleep(1)

output = render('Thankyou!', colors=['yellow', 'red'], align='center')
print(output)



def restart_program():
	python = sys.executable
	os.execl(python, python, * sys.argv)

if __name__ == "__main__":
    answer = input("\n [-] Do you want to restart this program ?(y/n) ")
    if answer.lower().strip() in "y".split():
        restart_program()
