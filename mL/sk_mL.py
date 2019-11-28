# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 10:37:45 2019

@author: vaibhav
"""

import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
#%matplotlib inline
from collections import Counter
import warnings
warnings.filterwarnings("ignore")


train_input=pd.read_csv("Credit_Risk_Train_data")
test_input=pd.read_csv("Credit_Risk_Test_data")

test_input.rename(columns={"outcome":"Loan_status"},inplace=True)
data_all=pd.concat([train_input,test_input],axis=0,ignore_index=True)
data_all.isnull().sum()
Counter(data_all["Gender"])

print(data_all[data_all['Gender'].isnull()].index.tolist()) # to check for null (NaN ) values
data_null=(data_all[data_all['Gender'].isnull()].index.tolist())
