import statistics
import math



def main(Y, P, Perdiction=None):
    log = lambda x: math.log(x)
    r = lambda x: round(x)
    l_pop = [log(i) for i in P]
    POPULATION = [l_pop[i + 1] - l_pop[i] for i in range(len(Y) - 1)]
    YEARS = [(Y[i + 1]) - (Y[i]) for i in range(len(Y) - 1)]
    Kg = []
    for delta_y, delta_p in zip(YEARS, POPULATION):
        Kg.append(delta_p / delta_y)
    Kg = statistics.mean(Kg)
    
    if Perdiction:
        
        Perdiction = l_pop[-1] + (Kg) * (Perdiction - Y[-1])
        Perdiction = math.exp(Perdiction)
        print(f"Perdiction for {Perdiction} is {r(Perdiction)}")


    


if __name__ == "__main__":
    YEARS = [1910, 1920, 1930, 1940, 1950, 1960, 1970]
    POPULATION = [45000, 60000, 87000, 115000, 129000, 149000, 165000]
    main(YEARS, POPULATION, Perdiction=2020)
