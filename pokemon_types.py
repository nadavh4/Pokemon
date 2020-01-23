# -*- coding: utf-8 -*-
"""

Pokemon Types

"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#%%

#Loaing the dataframe
df=pd.read_csv('pokemon.csv')

#creating a new dataframe by counting the number of pokemon from type 1 and renaming the columns
df=df['Type 1'].value_counts().reset_index().rename(columns={'Type 1':'Number','index':'Type 1'})


#plotting 
ax= sns.barplot(x='Type 1',y='Number', data=df)
ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right")
plt.savefig('pokemon_types_1.png')