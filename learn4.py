num = input("enter a number you want to test if it is odd or even numbr : ")
n = float(num)

mod = n % 2

if mod != 0:
    print(num + " is an odd")
else:
    print(num + " is an even number")