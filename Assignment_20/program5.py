""" Design a Python application that creates two threads named Thread1 and Thread2.
• Thread1 should display numbers from 1 to 50.
• Thread2 should display numbers from 50 to 1 in reverse order.
• Ensure that:
◦ Thread2 starts execution only after Thread1 has completed.
• Use appropriate thread synchronizatio"""


import threading

def DisplayForward():
    print("Thread1: Numbers from 1 to 50")
    for i in range(1, 51):
        print(i)

def DisplayReverse():
    print("Thread2: Numbers from 50 to 1")
    for i in range(50, 0, -1):
        print(i)

def main():
    t1 = threading.Thread(target=DisplayForward, name="Thread1")
    t2 = threading.Thread(target=DisplayReverse, name="Thread2")

    t1.start()
    t1.join()     # Thread2 waits until Thread1 completes

    t2.start()
    t2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()
