import pandas as pd
from variables import abcde_map, abcde_plus_map, abcde_plus_list, abcde_list, numeric_list

def read_ibd(filename):
    """
    Cleaning the IBD datatables
    :param filename:
    :return: df
    """

    df = pd.read_excel(filename, index_col=0)

    first_row_index = df.index.get_loc('Symbol')
    last_row_index = df.index.get_loc(df.last_valid_index()) + 1
    df = df.iloc[first_row_index:last_row_index]

    df.columns = df.iloc[0]
    df = df.iloc[1:]
    return df


def convert_datatypes_ibd(df):

    df[numeric_list] = df[numeric_list].apply(pd.to_numeric, errors='coerce')

    for item in abcde_list:
        df[item] = df[item].map(abcde_map)

    for item in abcde_plus_list:
        df[item] = df[item].map(abcde_plus_map)

    df['IPO Date'] = pd.to_datetime(df['IPO Date'])

    return df

