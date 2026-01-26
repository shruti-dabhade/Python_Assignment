""": Design a Python application that creates two threads.
• Thread 1 should compute the sum of elements from a list.
• Thread 2 should compute the product of elements from the same list.
• Return the results to the main thread and display them."""


import threading

sum_result = 0
product_result = 1

def ComputeSum(numbers):
    global sum_result
    sum_result = sum(numbers)

def ComputeProduct(numbers):
    global product_result
    product_result = 1
    for num in numbers:
        product_result *= num

def main():
    n = int(input("Enter number of elements: "))
    numbers = []

    print("Enter elements:")
    for i in range(n):
        numbers.append(int(input()))


    t1 = threading.Thread(target=ComputeSum, args=(numbers,), name="ThreadSum")
    t2 = threading.Thread(target=ComputeProduct, args=(numbers,), name="ThreadProduct")

    t1.start()
    t2.start()


    t1.join()
    t2.join()

  
    print("Sum of elements:", sum_result)
    print("Product of elements:", product_result)
    print("Exit from main")

if __name__ == "__main__":
    main()
