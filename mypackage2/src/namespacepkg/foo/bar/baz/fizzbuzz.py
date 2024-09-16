def fizz_buzz(value: int) -> str:
    if value % 15 == 0:  # divisible by 3 three and 5 (i.e. divisible by 15)
        return "fizz buzz"
    elif value % 3 == 0:
        return "fizz"
    elif value % 5 == 0:
        return "buzz"
    return str(value)
