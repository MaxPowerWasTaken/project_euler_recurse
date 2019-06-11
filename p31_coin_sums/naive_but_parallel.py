from itertools import combinations_with_replacement
from tqdm import tqdm
from multiprocessing import Pool, cpu_count

if __name__ == '__main__':
    coins = [1,2,5,10,20,50,100,200]
    result_count = 0
    all_combos = combinations_with_replacement(coins, 200)
    num_combos = 2872408791  # 'n multichoose k, for n=6 and k=200'
    
    with Pool(processes=cpu_count()) as p:
        with tqdm(total=num_combos) as pbar:
            for sum_ in tqdm(p.imap_unordered(sum, all_combos)): 
                pbar.update()
                if sum_ == 200:
                    result_count = result_count + 1
    print(f'result count: {result_count}')

# Notes: this is even slower than the naive-single-threaded, way slower.
#        reason must be that the function is so light (sum of a short list),
#        the mp overhead of pickling the data and moving it around is not worth it