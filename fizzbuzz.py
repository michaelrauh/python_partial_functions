def fizz_buzz(chosen_number):
    return both(chosen_number) or fizz(chosen_number) or buzz(chosen_number) or neither(chosen_number)


def both(chosen_number):
    if chosen_number % 15 == 0:
        return "FizzBuzz"

def fizz(chosen_number):
    if chosen_number % 3 == 0:
        return "Fizz"

def buzz(chosen_number):
    if chosen_number % 5 == 0:
        return "Buzz"

def neither(chosen_number):
    return str(chosen_number)