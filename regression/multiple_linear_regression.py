import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression


def main():
    base = pd.read_csv("mt_cars.csv")
    base = base.drop(["Unnamed: 0"], axis=1)
    print(base)

    x_disp = base.iloc[:, 2].values
    y_mpg = base.iloc[:, 0].values

    corr = np.corrcoef(x_disp, y_mpg)
    print(corr)

    x_disp = x_disp.reshape(-1, 1) # formato para usar LinearRegression
    print(x_disp)

    model = LinearRegression()
    model.fit(x_disp, y_mpg)

    print(model.intercept_)
    print(model.coef_)

    # calculo do coef de determinacao
    print(model.score(x_disp, y_mpg))

    preview = model.predict(x_disp)
    print(preview)

    # REGRESSAO MULTIPLA
    # pega todos os valores das linhas
    # entre as colunas 1 e 3 (inclusive). Exclui a 4.
    X1 = base.iloc[:, 1:4].values
    print(X1)

    model.fit(X1, y_mpg)
    print(model.score(X1, y_mpg))
    print(model.intercept_)
    print(model.coef_)

    preview2 = model.predict(np.array([4, 200, 100]).reshape(1, -1))
    print(preview2)
    return


if __name__ == "__main__":
    main()
