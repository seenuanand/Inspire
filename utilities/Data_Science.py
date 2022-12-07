import inline
import matplotlib
import pandas as pd
import numpy as np
import matplotlib as plt

#Reading the dataset in a dataframe using Pandas
df = pd.read_csv("C:\\Users\\91900\\Downloads\\Hospital_Staffing\\hospital-staffing-2009-2013.csv")
print(df.head())
print(df['Property_Area'].value_counts())
