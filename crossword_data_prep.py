import csv
from random import randint
from numpy import save
import pandas as pd

df = pd.read_excel('crossword_data.xlsx')
clues = df.values
save('clues.npy', clues)