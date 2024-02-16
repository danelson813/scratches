import pandas as pd
import numpy as np
from tqdm import tqdm
df = pd.DataFrame(np.random.randint(0, 100, (100000, 1000)))
tqdm.pandas(desc='Processing Dataframe')
df.progress_apply(lambda x: (x+3)**3)