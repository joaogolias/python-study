import pandas as pd #carregar os dados
import numpy as np #matematica
import matplotlib.pyplot as plt
from array import array
from sklearn.linear_model import LinearRegression


def calculate_corr(base):
    # vamos separar as informacoes do csv em 2 vetores
    # a previsao que vamos fazer é sobre a speed, que é, então a variavel independente(Y)
    # e a dist é a dependente (X)
    # vamos pegar só a distância (todas as linhas da coluna 1)
    x_dist = base.iloc[:, 1].values

    # e a velocidade
    y_speed = base.iloc[:, 0].values

    # para calcular a correlacao:
    corr = np.corrcoef(x_dist, y_speed)
    return corr


def linear_regression(base):
    x_dist = base.iloc[:, 1].values
    y_speed = base.iloc[:, 0].values
    lr = LinearRegression()

    # precisamos redimensionar o x_dist para o formato da funcao
    x_dist = x_dist.reshape(-1, 1)
    lr.fit(x_dist, y_speed)
    return lr


def main():
    base = pd.read_csv("cars.csv")

    # ele incluiu uma coluna chamada 'unnamed' na posicao 1
    # para retirá-la. o "1"siginifca que queremos tirar a coluna toda e não a linha!
    base = base.drop(['Unnamed: 0'], axis=1)

    # para calcular a correlacao:
    print(calculate_corr(base))

    # para fazer a regressão linear
    model = linear_regression(base)
    print(model.intercept_)
    print(model.coef_)

    # realizando o grafico de X por Y
    # lembrando de redimencionar
    x_dist = base.iloc[:, 1].values.reshape(-1, 1)
    y_speed = base.iloc[:, 0].values

    plt.scatter(x_dist, y_speed)
    plt.plot(x_dist, model.predict(x_dist), color="red")

    # para prever
    y_for_dist_22 = model.intercept_ + 22*model.coef_
    print(y_for_dist_22)

    print(model.predict([[22]]))
    print(model._residues)
    return


if __name__ == "__main__":
    main()
