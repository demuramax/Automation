# DS4B 101-P: PYTHON FOR BUSINESS ANALYSIS ----
# Module 2 (Pandas Import): Importing Files ----

# IMPORTS ----
# %%
import pandas as pd
from os import getcwd, mkdir
# 1.0 FILES ----

# - Pickle ----
# %%
pickle_df = pd.read_pickle('../01_jumpstart/00_data_wrangled/bike_orderlines_wrangled_df.pkl')
pickle_df.info()
# - CSV ----
csv_df = pd.read_csv('../01_jumpstart/00_data_wrangled/bike_orderlines_wrangled_df.csv', parse_dates=['order_date'])
csv_df.info()
# - Excel ----
excel_df = pd.read_excel('../01_jumpstart/00_data_wrangled/bike_orderlines_wrangled_df.xlsx')
excel_df


# %%
