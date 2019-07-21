from scipy.stats import t


def calculate_normal_t_student():
    return t.cdf(
        1.5, # valor que buscamos
        8 # grau de liberdade n-1
    )


def calculate_opposite_t_student():
    return t.sf(
        1.5,
        8
    )


def main():
    normal = calculate_normal_t_student()
    opposite = calculate_opposite_t_student()
    print(normal)
    print(opposite)
    print(normal + opposite)
    return


if __name__ == "__main__":
    main()
