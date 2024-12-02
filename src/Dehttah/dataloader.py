import os
import glob
import gc

import pandas as pd



def load_janestreet_train(path_raw_dir):
    
    glob_path = os.path.join(path_raw_dir, "**/*.parquet")
    list_raw_file = glob.glob(glob_path, recursive=True)
    df = pd.DataFrame()
    for file in list_raw_file:
        data = pd.read_parquet(file, engine="fastparquet")
        # df = pd.concat([df, data], ignore_index=True, copy=False)
        del data
        gc.collect()
        import psutil
        print(f"사용 메모리: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} MB")
        # import sys
        # size = sys.getsizeof(df)
        # print(size)
        

    return df


if __name__ == "__main__":
    import os

    from dotenv import load_dotenv
    load_dotenv(verbose = False)

    PATH_DATA = os.getenv("PATH_DATA_VIRTUAL")
    PATH_RAW = os.path.join(PATH_DATA, "raw")

    data = load_janestreet_train(PATH_RAW)
    print(data)