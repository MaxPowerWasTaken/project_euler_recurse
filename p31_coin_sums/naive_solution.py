from itertools import combinations_with_replacement
from tqdm import tqdm

if __name__ == '__main__':
    coins = [1,2,5,10,20,50,100,200]
    result_count = 0

    all_combos = combinations_with_replacement(coins, 200)
    for sequence in tqdm(all_combos, total = 2872408791):  # total is 'n multichoose k' for n=6 and k=200
        if sum(sequence) == 200:
            result_count = result_count + 1
    print(f'result count: {result_count}')

# Notes: this will take around 70-75 minutes on my machine according to tqdm and running til about 20%



