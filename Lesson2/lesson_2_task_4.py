
def fizz_buzz(n):
    for n in range(1, n + 1):
        if (n % 3 == 0) and (n % 5 == 0):
            print("FizzBuzz")
        else:
             if (n % 3) == 0:
              print("Fizz")
             else:
                if (n % 5) == 0:
                    print("Buzz")
                else:
                    print(n)
                

n = input("Введите N=")
n = int(n)
fizz_buzz(n)