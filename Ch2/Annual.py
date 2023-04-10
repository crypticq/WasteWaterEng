#!/usr/bin/env python3

def main(Grawth , Pop , Perdiction , Year):
    Grawh = Grawth / 100
    P = Pop * (1 + Grawh) ** (Perdiction - Year)
    print(f"Perdiction for {Perdiction} is {round(P)} Captia")

    


if __name__ == "__main__":
    Grawth = 2.195
    Pop = 165000
    Perdiction = 2020
    Year = 1970
    main(Grawth , Pop , Perdiction , Year)