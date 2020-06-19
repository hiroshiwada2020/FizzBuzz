def fizzbuzz_convert(number):
    if number % 3 == 0:
        return "Fizz"
    if number % 5 == 0:
        return "Buzz"
    if number % 15 == 0:
        return "FizzBuzz"


assert fizzbuzz_convert(3) == "Fizz"
assert fizzbuzz_convert(5) == "Buzz"
