import pandas
import numpy

def main():
    data = pandas.read_csv("iris.csv")
    print(data.shape)

    # criando uma amostra aleatoria de 0s e 1s

    sample = generate_random_sample()
    get_sample_statistics(sample)

    #  podemos definir uma seed para garantir que ele sempre
    #  vai retornar os mesmos resultados
    numpy.random.seed(123)
    sample = generate_random_sample()
    get_sample_statistics(sample)

    return


def get_sample_statistics(sample):
    print("Total de elementos: ")
    print(len(sample))
    print("\nQuantidade de 1: ")
    print(get_number_quantity(sample, 1))
    print("\nQuantidade de 2: ")
    print(get_number_quantity(sample, 0))
    print("\n\n")


def get_number_quantity(sample, number):
    return len(sample[sample == number])


def generate_random_sample():
    return numpy.random.choice(
        [0, 1],  # populacao
        150,  # tamanho da amostra
        True,  # com reposição ou não
        [0.5, 0.5])


if __name__ == "__main__":
    main()
