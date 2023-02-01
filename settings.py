from types import SimpleNamespace
import os


import numpy as np

# DATA PROPERTIES

## to specify the source data
## file/googlesheets/database etc
SOURCE_TYPE = 'file'

## properties required to connect with source succesfully and read data
if SOURCE_TYPE == 'file':
    _ = {
        'name': 'Personal Expense Tracker - transactions.csv',
        'type': 'csv',
        'location': r'data',
        'columns': ('id', 'date', 'amount', 'type', 'sub_type', 'description', 'bank', 'payment_mode'),
        'datatype': {
            'id': np.int8, 
            'date': np.str_, 
            'amount': np.float64, 
            'type': np.str_,
            'sub_type': np.str_,
            'description': np.str_, 
            'bank': np.str_, 
            'payment_mode': np.str_,
        },
        'parse_dates': ['date',],
        'metadata': {
            'id': {'position': 1, 'data_type': 'INTEGER'}, 
            'date': {'position': 2, 'data_type': 'DATE'}, 
            'amount': {'position': 3, 'data_type': 'NUMERIC'}, 
            'type': {'position': 4, 'data_type': 'TEXT'},
            'sub_type': {'position': 5, 'data_type': 'TEXT'},
            'description': {'position': 6, 'data_type': 'TEXT'}, 
            'bank': {'position': 7, 'data_type': 'TEXT'}, 
            'payment_mode': {'position': 8, 'data_type': 'TEXT'},
        },
    }

    PROPERTIES = SimpleNamespace(
        **_,
        relative_path=os.path.join(_['location'], _['name'])
    )