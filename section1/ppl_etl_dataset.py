#!/usr/bin/python3
"""
Author: Lu Yaomin
Description: To process dataset into first_name, last_name, price, above_100
Input data: dataset.csv
Output data: dataset_output.csv
"""
import pandas as pd
import os
import re

### Input filename
input_filename = 'dataset.csv'
### Output filename
output_filename = 'dataset_output.csv'

### Read the dataset into a Dataframe
input_df = pd.read_csv(input_filename)

def get_firstname(name):
    first, *last = name.split()
    return first

def get_lastname(name):
    first, *last = name.split()
    last = " ".join(last)
    return last

def get_price_above100(rec):
    if (rec > 100):
        return 'true'
    else:
        return 'false'
### Drop empty name records if any
input_df.dropna(subset=['name'], inplace=True)
### No need to drop the zero padding from the price, 
### because naturally the zero paddings will be removed with float64 datatype

### Creates a new column with the first name
input_df['first_name'] = input_df['name'].apply(lambda row: get_firstname(row))
### Creates a new column with the first name
input_df['last_name'] = input_df['name'].apply(lambda row: get_lastname(row))
### Creates a new column that has price greater than 100
input_df['above_100'] = input_df['price'].apply(lambda row: get_price_above100(row))

### Creates the output file
input_df.to_csv(output_filename, index=False)
