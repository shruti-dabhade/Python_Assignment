"""
    : Design a Python application that creates two separate threads named Even and Odd.
    • The Even thread should display the first 10 even numbers.
    • The Odd thread should display the first 10 odd numbers.
    • Both threads should execute independently using the threading module.
    • Ensure proper thread creation and execution
"""
import threading

def DisplayEven():
    print("Even Thread:")
    for i in range(1, 21):
        if i % 2 == 0:
            print(i)

def DisplayOdd():
    print("Odd Thread:")
    for i in range(1, 21):
        if i % 2 != 0:
            print(i)

def main():
    even_thread = threading.Thread(target=DisplayEven, name="Even")
    odd_thread = threading.Thread(target=DisplayOdd, name="Odd")

    even_thread.start()
    odd_thread.start()

    even_thread.join()
    odd_thread.join()

    print("Both threads executed successfully")

if __name__ == "__main__":
    main()
