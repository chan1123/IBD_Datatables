import pandas as pd
from functions import read_ibd, convert_datatypes_ibd

df = convert_datatypes_ibd(read_ibd('IBD_Excel/20201210_IBD.xlsx'))

print(df)

