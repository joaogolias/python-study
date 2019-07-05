import pandas
import numpy


def main():
    iris = pandas.read_csv("iris.csv")
    iris_petal_length = iris.iloc[:, 2]

    numpy.random.seed(10)
    sample = numpy.random.choice(iris_petal_length, 20, False)

    print(numpy.mean(sample))
    print(numpy.median(sample))
    print(numpy.quantile(sample, [0, 0.25, 0.5, 0.75, 1]))
    print(numpy.std(sample, ddof=1))# ao dividir, ele usa N-ddof. Como é uma amostra, temos que colocar como 1
    return


if __name__ == "__main__":
    main()
