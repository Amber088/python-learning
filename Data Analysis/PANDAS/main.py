import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

Super= pd.read_csv("/Users/amberjain/Desktop/Python/PANDAS/bollywood.csv",index_col='movie').squeeze()
# print(Super.value_counts())
vk = pd.read_csv("/Users/amberjain/Desktop/Python/PANDAS/kohli_ipl.csv",index_col='match_no').squeeze()
# 

subs = pd.read_csv("/Users/amberjain/Desktop/Python/PANDAS/subs.csv").squeeze()
vk.plot()
print(plt.show())

