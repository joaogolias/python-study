def my_pow(value=2, exponent=10):
    aux = 1
    result = value
    while aux < exponent:
        result *= value
        aux += 1
    return result


def main():
    print(my_pow())
    print(my_pow(2, 2))
    print(my_pow(5, 3))


if __name__ == "__main__":
    main()
