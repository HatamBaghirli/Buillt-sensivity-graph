#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from scipy import stats
from scipy import optimize
from scipy.optimize import differential_evolution
from scipy import interpolate
import warnings


# In[2]:


def annual_worth_oil(i,n_o,Capital_Investment_oil,reduced_operating_expenses_oil,cost_of_fuel_oil,Btus_producced_oil,number_of_Btus_oil):
    return Capital_Investment_oil*(i*(1+i)**n_o)/((1+i)**n_o-1)+reduced_operating_expenses_oil-(cost_of_fuel_oil/Btus_producced_oil)*number_of_Btus_oil
def annual_worth_gas(i,n_g,Capital_Investment_gas,reduced_operating_expenses_gas,cost_of_fuel_gas,Btus_producced_gas,number_of_Btus_gas):
    return Capital_Investment_gas*(i*(1+i)**n_g)/((1+i)**n_g-1)+reduced_operating_expenses_gas-(cost_of_fuel_gas/Btus_producced_gas)*number_of_Btus_gas


# In[3]:


def oil(i,number_of_Btus_oil):
    return -5400-0.0157*number_of_Btus*(1+i)
def gas(i,number_of_Btus_gas):
    return -1050-0.04*number_of_Btus*(1+i)


# In[7]:


number_of_Btus= 179012


# In[8]:


DiscountRate_array = np.linspace(-0.3, 0.3, 15000)
oil_array = oil(DiscountRate_array,number_of_Btus)
gas_array = gas(DiscountRate_array,number_of_Btus)


# In[9]:


df=pd.DataFrame(data={'Discount Rate':DiscountRate_array, 'oil': oil_array, 'gas': gas_array})
fig = px.line(df, x='Discount Rate', y=['oil', 'gas'], labels=dict(value="Value", variable="Approach"))
fig.show()


# In[ ]:




