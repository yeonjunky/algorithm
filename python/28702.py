fb = ["Fizz", "Buzz", "FizzBuzz"]

output = ""
for i in range(1, 4):
    s = input()
    if s not in fb and output == "":
        num = int(s) + 4 - i
        if num % 3 == 0 and num % 5 == 0:
            output = "FizzBuzz"
        elif num % 3 == 0:
            output = "Fizz"
        elif num % 5 == 0:
            output = "Buzz"
        else:
            output = num

print(output)
