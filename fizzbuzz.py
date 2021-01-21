n = int(input("Enter the amount of numbers to generate fizzbuzz for "))
for i in range (1,n):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    if i % 3 == 0:
        print("Fizz")
    if i % 5 == 0:
        print("Buzz")
    else: 
        print(i)