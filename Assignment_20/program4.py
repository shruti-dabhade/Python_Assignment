""": Design a Python application that creates three threads named Small, Capital, and 
Digits.
• All threads should accept a string as input.
• The Small thread should count and display the number of lowercase characters.
• The Capital thread should count and display the number of uppercase characters.
• The Digits thread should count and display the number of numeric digits.
• Each thread must also display:
◦ Thread ID
◦ Thread Name"""

import threading

def Small(text):
    count = 0
    for ch in text:
        if ch.islower():
            count += 1
    print("Thread Name:", threading.current_thread().name)
    print("Thread ID:", threading.get_ident())
    print("Number of lowercase characters:", count)
    print()

def Capital(text):
    count = 0
    for ch in text:
        if ch.isupper():
            count += 1
    print("Thread Name:", threading.current_thread().name)
    print("Thread ID:", threading.get_ident())
    print("Number of uppercase characters:", count)
    print()

def Digits(text):
    count = 0
    for ch in text:
        if ch.isdigit():
            count += 1
    print("Thread Name:", threading.current_thread().name)
    print("Thread ID:", threading.get_ident())
    print("Number of digits:", count)
    print()

def main():
    string = input("Enter a string: ")

    t1 = threading.Thread(target=Small, args=(string,), name="Small")
    t2 = threading.Thread(target=Capital, args=(string,), name="Capital")
    t3 = threading.Thread(target=Digits, args=(string,), name="Digits")

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    print("Exit from main")

if __name__ == "__main__":
    main()
