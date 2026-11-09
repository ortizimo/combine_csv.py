# name: combine_csv 
# version: 1.0
# author: Saulo 'Sal' Ortiz
# date: 2023.08.22
# update: 2023.08.30
# best to use in Linux...cause LINUX RULEZ!!!!

# hey...listen! place this file in the same directory/folder where your CSVs from hayabusa are located then run it to create a single CSV file
# use: python3 combine_csv.py

import os
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

print()
print('The cursor will stop blinking...please wait for process to complete!')

sal_df = pd.DataFrame()

for file in os.listdir(os.getcwd()):
	if file.endswith('.csv'):
		sal_df = sal_df.append(pd.read_csv(file))

sal_df.to_csv('COMBINED_OUTPUT.csv', index=False)

print('--------------------------------------------------------------------')
print('Process Complete!')
