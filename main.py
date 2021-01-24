import pandas as pd
from functions import read_ibd, convert_datatypes_ibd
from functions import latest_file

df = convert_datatypes_ibd(read_ibd(latest_file()))

print(df)

