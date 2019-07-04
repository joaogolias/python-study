import pandas
from sklearn.model_selection import train_test_split


def main():
    infert = pandas.read_csv("infert.csv")

    x, _, y, _ = train_test_split(
        infert.iloc[:, 2:9],# passamos todos os valores a serem considerados
        infert.iloc[:, 1],# passamos a classe de estratificacao (no caso, education)
        test_size=0.6,# porcentagem da populacao que queremos na amostra
        stratify= infert.iloc[:, 1],# passamos a classe de estratificacao (no caso, education)
    )

    print(x)
    print(y)
    print(x.shape)
    print(y.shape)
    print(y.value_counts())
    return



if __name__ == "__main__":
    main()
