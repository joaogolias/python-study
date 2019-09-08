prime_arr = [2]


def get_next_prime(n):
    is_prime = False
    k = n
    while not is_prime:
        k = k + 1
        for m in prime_arr:
            if k % m == 0:
                is_prime = False
                break
            else:
                is_prime = True
    prime_arr.append(k)
    return k


def primeFactors(n):
    result = n
    index = 0
    result_arr = []
    while result != 1:
        if result % prime_arr[index] == 0:
            result = result/prime_arr[index]
            result_arr.append(prime_arr[index])
        else:
            get_next_prime(prime_arr[index])
            index += 1
    return convert_arr_to_string(result_arr)


def convert_arr_to_string(arr):
    str_result = ""
    last_i = 0
    pot = 1
    for i in arr:
        if i != last_i:
            if last_i != 0:
                str_result += "(" + str(last_i)
                if pot == 1:
                    str_result += ")"
                else:
                    str_result += "**" + str(pot) + ")"
                pot = 1
        else:
            pot += 1
        last_i = i
    if pot == 1:
        str_result += "(" + str(last_i) + ")"
    else:
        str_result += "(" + str(last_i) + "**" + str(pot) + ")"
    return str_result


def main():
    print(primeFactors(4))
    print(primeFactors(8))
    print(primeFactors(50))
    print(primeFactors(24))
    print(primeFactors(40))
    print(primeFactors(7775460))
    return


if __name__ == "__main__":
    main()
