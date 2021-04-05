#inorder to implement the Data Structures and Algorithms in Python projects. Now let’s see how to implement the FizzBuzz algorithm using Python:


for i in range(1, 20):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
