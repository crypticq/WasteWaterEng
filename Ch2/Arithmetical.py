import statistics


def main(Y, P, Perdiction=None):
    POPULATION = [P[i + 1] - P[i] for i in range(len(Y) - 1)]
    YEARS = [Y[i + 1] - Y[i] for i in range(len(Y) - 1)]
    # Delta p = p1 - p0 , Delta t = t1 - t0
    # Kav = Delta p / Delta t
    Ka = []
    for Delta_p, Delta_t in zip(POPULATION, YEARS):
        # print(f"Kav = {Delta_p / Delta_t}")
        Ka.append(round(Delta_p / Delta_t, 2))
    print(f"Average increment = {round(statistics.mean(Ka))}")

    if Perdiction:
        Pop = P[-1] + Ka[-1] * (Perdiction - Y[-1])
        print("The population in 2020 is: ", round(Pop, 2), "Captia.")


if __name__ == "__main__":
    YEARS = [1910, 1920, 1930, 1940, 1950, 1960, 1970]
    POPULATION = [45000, 60000, 87000, 116000, 129000, 145000, 165000]
    main(YEARS, POPULATION, Perdiction=2020)
