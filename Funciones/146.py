for Johan in range(1, 16):
    if Johan % 3 == 0 and Johan % 5 == 0:
        print("FizzBuzz")
    elif Johan % 3 == 0:
        print("Fizz")
    elif Johan % 5 == 0:
        print("Buzz")
    else:
        print(Johan)