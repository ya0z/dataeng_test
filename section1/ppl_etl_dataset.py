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

### To clean the salutations in name
salutation_filename = 'salutation.csv'

### Read the dataset into a Dataframe
input_df = pd.read_csv(input_filename)

def clean_name(rec):
    # Remove salutation from name
    salutation = open(salutation_filename).read().splitlines()
    name = re.sub('^' + r'\s+|^'.join(salutation) + '\s+', '', rec)
    #print(name)
    return name

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
input_df['first_name'] = input_df['name'].apply(lambda row: get_firstname(clean_name(row)))
### Creates a new column with the first name
input_df['last_name'] = input_df['name'].apply(lambda row: get_lastname(clean_name(row)))
### Creates a new column that has price greater than 100
input_df['above_100'] = input_df['price'].apply(lambda row: get_price_above100(row))

### Select first_name, last_name, price, above_100
selected_columns = ['first_name','last_name','price','above_100']
output_df = input_df.loc[:,selected_columns]
### Creates the output file
output_df.to_csv(output_filename, index=False)
