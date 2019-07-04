import pandas
import numpy

from math import ceil


def main():
    # vamos criar a amostragem sistematica na mao, pq nao tem uma lib no python para isso
    # a ideia eh: vamos gerar uma lista com todos os indexes, e, entao pegar de um data frame
    # queremos pegar 15 elemenos em um data frame com 150

    population_length = 150
    sample_length = 15
    proportion = ceil(population_length/sample_length)
    random_numbers = numpy.random.randint(
        1,#  inicio
        proportion+1,#  fim
        1#  quantos numeros aleatorios
    )
    aux = random_numbers[0]

    drawn_list = []

    for i in range(sample_length):
        drawn_list.append(aux)
        aux += proportion

    print(drawn_list)

    iris = pandas.read_csv("iris.csv")
    sample = iris.loc[drawn_list]# pega os elementos com os indexes nessa lista
    print(sample)
    return


if __name__ == "__main__":
    main()
