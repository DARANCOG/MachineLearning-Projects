# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 07:38:47 2022

@author: dario
"""

import pandas as pd

# importar dataset
dataset = pd.read_csv('Data.csv')
# Variables Independientes
X = dataset.iloc[ : , : -1]
# Variable dependiente
y = dataset.iloc[ : , 3 ]