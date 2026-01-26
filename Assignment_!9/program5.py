""".Write a program which contains filter(), map() and reduce() in it. Python application which 
contains one list of numbers. List contains the numbers which are accepted from user. Filter 
should filter out all prime numbers. Map function will multiply each number by 2. Reduce will 
return Maximum number from that numbers. (You can also use normal functions instead of 
lambda functions). 
Input List = [2, 70 , 11, 10, 17, 23, 31, 77] 
List after filter = [2, 11, 17, 23, 31] 
List after map = [4, 22, 34, 46, 62] 
Output of reduce = 62"""


from functools import reduce

def ChkPrime(no):
    if no < 2:
        return False
    for i in range(2, int(no / 2) + 1):
        if no % i == 0:
            return False
    return True

def main():
    numbers = []
    n = int(input("Enter number of elements: "))

    print("Enter elements:")
    for i in range(n):
        numbers.append(int(input()))

    filtered = list(filter(ChkPrime, numbers))

    mapped = list(map(lambda x: x * 2, filtered))

    result = reduce(lambda x, y: x if x > y else y, mapped)

    print("Input List =", numbers)
    print("List after filter =", filtered)
    print("List after map =", mapped)
    print("Output of reduce =", result)

if __name__ == "__main__":
    main()
