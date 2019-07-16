from scipy.stats import norm, probplot, shapiro
import matplotlib.pyplot as plt # lib de plot mais famosa do python


def main():
    print(prob_less_3())
    print(prob_more_5())
    print(prob_less_13_more_5())
    test_normal_distribution()
    return


# Considere uma cesta que tenha elemenots
# cujos pesos segue uma distribuição normal com media=10kg e desvio_padrao=5kg
# Qual a prob de se obter um peso menor que 3kg?
# P[X<x]


def prob_less_3():
    return norm.cdf(3, 10, 5)

# Qual a prob de se obter um peso maior que 5kg?
# P[X>x]


def prob_more_5():
    # return 1-norm.cdf(5, 10, 5)
    return norm.sf(5, 10, 5)

# Qual a prob de se obter um peso maior que 5kg e menor que 13kg?
# P[x1<X<x2]


def prob_less_13_more_5():
    return norm.cdf(13, 10, 5)-norm.cdf(5, 10, 5)

# Vamos fazer teste de distribuição normal


def test_normal_distribution():
    data = norm.rvs(size=100) # gera uma distribuição normal com 100 elementos
    probplot(data, plot=plt)
    plt.show()
    print(shapiro(data))


if __name__ == "__main__":
    main()
