"""Write a lambda function which accepts three numbers and returns largest number"""


Maximum = lambda a,b,c : (
    a if a > b and a > c 
    else b if b > a and b > c
    else c
)
print("number is maximum")
print("maxmum is :", Maximum(10,20,30))