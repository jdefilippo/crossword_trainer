import numpy as np
from numpy import load
from random import randint

clues = np.load('clues.npy', allow_pickle=True)
num_clues = len(clues)

while True:
    rand_number = randint(2000,3000)
    real_clue = "".join(filter(str.isalnum, clues[rand_number][3]))

    print(clues[rand_number][2])
    print(str(len(real_clue)) + " letters")
    print("Popularity: " + str(clues[rand_number][4]))
    input()
    print(real_clue)
    input()
    print(clues[rand_number][5])
    input()
