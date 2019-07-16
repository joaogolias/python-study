from scipy.stats import binom

def main():
    # probabilidade de cair 3 caras ao se jogar uma moeda 5 vezes
    prob = binom.pmf(3, 5, 0.5)
    print(prob)
    prob = binom.pmf(0, 5, 0.5)
    prob += binom.pmf(1, 5, 0.5)
    prob += binom.pmf(2, 5, 0.5)
    prob += binom.pmf(3, 5, 0.5)
    #probabilidade cumulativa
    pac = binom.cdf(3, 5, 0.5)
    print(pac == prob)
    return


if __name__ == "__main__":
    main()
