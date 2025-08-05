class NonNegativeNumberException(Exception):
    pass


n = 0
while True:
    try:
        n = int(input("Enter your number: "))
        if n < 0:
            raise NonNegativeNumberException(
                "Number should not be negative number")
        break
    except NonNegativeNumberException as error:
        print(error)
    except Exception as error:
        print("Something went wrong, please try again")


fibonacci_sequence = []

if n == 1:
    fibonacci_sequence = [0]
elif n == 2:
    fibonacci_sequence = [0, 1]
else:
    fibonacci_sequence = [0, 1]
    for i in range(2, n):
        next_number = fibonacci_sequence[i-1] + fibonacci_sequence[i-2]
        fibonacci_sequence.append(next_number)

print(fibonacci_sequence)
