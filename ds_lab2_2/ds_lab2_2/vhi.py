#!/usr/bin/env python
# coding: utf-8

# In[5]:



from urllib import request
import time
import datetime
import os
import pandas as pd
def general(x):
    os.chdir(r"C:\Users\tangerine\data_science")
    df = pd.read_csv('vhi_id_%s.csv'%(x),index_col=False, header=1)
    df.drop(df.columns[7], axis=1, inplace=True) 
    df.columns=['year', 'week', 'SMN', 'SMT', 'VCI', 'TCI', 'VHI']
    df['region'] = x
    df = df.loc[~df['VHI'].isin([-1,'NaN'])]
    return df  

def analyze(df,crit1,crit2):
    return df[(df['week']<=crit1) & (df['week']>=crit2)]

def VHI_year(x):
    dop=df[(df['year']==str(x))]
    return(dop.VHI)
def max_min_year():
    d={"year":df.year}
    data=pd.DataFrame(d)
    data.drop_duplicates(inplace=True)
    years=df['year'].unique()
    data['VHI_max']= [VHI_year(x).max() for x in years]
    data['VHI_min']=[VHI_year(x).min() for x in years]
    data = data.reset_index(drop=True)
    return data

def year_reg():
    data3=df.groupby(['region','year'], group_keys=False).apply(lambda x: pd.Series(dict(VHI_max=x.VHI.max(), VHI_min=x.VHI.min())))
    return data3


def month():
    data4=df
    data4['month']=(df['week']/(4.34)).astype('int')+1
    #data4['month']=data4['month'].astype('int')+1
    data4=data4.groupby(['month','year'], group_keys=False).apply(lambda x: pd.Series(dict(VHI_max=(x.VHI).max(), VHI_min=(x.VHI).min())))
    #data4=data4.groupby(['month','year'], group_keys=False).apply()



# In[55]:


def year_max():
    data4=df.groupby(['month'], group_keys=False).apply(lambda x: x.nlargest(1, 'VHI'))
    data4=data4[['month','year']]
    data4=data4.rename(columns={"year": "year_max"})
    data5=df.groupby(['month'], group_keys=False).apply(lambda x: x.nsmallest(1, 'VHI'))
    data5=data5[['month','year']]
    data5=data5.rename(columns={"year": "year_min"})
    data5=data5.merge(data4) 
    return data5


# In[11]:


