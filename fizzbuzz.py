def fizz_buzz(chosenNumber):
    if chosenNumber %15 == 0:
        return "FizzBuzz"
    if chosenNumber %3 == 0:
        return "Fizz"
    if chosenNumber %5 == 0:
        return "Buzz"
    return str(chosenNumber)
