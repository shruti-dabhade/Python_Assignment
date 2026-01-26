"""Design a Python application that creates two threads named Prime and NonPrime.
• Both threads should accept a list of integers.
• The Prime thread should display all prime numbers from the list.
• The NonPrime thread should display all non-prime numbers from the list."""

import threading

def is_prime(no):
    if no < 2:
        return False
    for i in range(2, int(no / 2) + 1):
        if no % i == 0:
            return False
    return True

def Prime(numbers):
    print("Prime numbers:")
    for num in numbers:
        if is_prime(num):
            print(num)

def NonPrime(numbers):
    print("Non-prime numbers:")
    for num in numbers:
        if not is_prime(num):
            print(num)

def main():
    n = int(input("Enter number of elements: "))
    numbers = []

    print("Enter elements:")
    for i in range(n):
        numbers.append(int(input()))

    t1 = threading.Thread(target=Prime, args=(numbers,), name="Prime")
    t2 = threading.Thread(target=NonPrime, args=(numbers,), name="NonPrime")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()
