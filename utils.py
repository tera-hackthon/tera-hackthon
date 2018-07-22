import numpy as np
import pandas as pd

from multiprocessing import cpu_count, Pool

num_cores = cpu_count() #number of cores on your machine
num_partitions = num_cores #number of partitions to split dataframe

def parall_df(df, func):
    df_split = np.array_split(df, num_partitions)
    pool = Pool(num_cores)
    df = pd.concat(pool.map(func, df_split))
    pool.close()
    pool.join()
    return df