import pandas as pd
import numpy as np

data = {
    'house_id': [1, 2, 3, 4, 5, 6, 7, 8],
    'price': [250000, 340000, 190000, 420000, 275000, 510000, 305000, 460000],
    'area_sqft': [1200, 1600, 950, 2100, 1350, 2400, 1500, 2000],
    'bedrooms': [2, 3, 2, 4, 3, 4, 3, 4]
}

df = pd.DataFrame(data)
print("---------------DATASET------------------------")
print(df)
print("---------------DATASET Printed----------------")
#Fromula for price per sqft
df['price_per_sqft']= df['price']/df['area_sqft']
print(df[['house_id','price','area_sqft','bedrooms','price_per_sqft']])
print("------------------------------------------------------")
#Function for normaization of price , area_sqft,price_per_sqft
def normalization_min_max(column):
    arr = column.to_numpy().copy()
    if arr.max() == arr.min():
        return np.zeros_like(arr, dtype=float)
    return (arr-arr.min())/(arr.max()-arr.min())
df['price_normalize']= normalization_min_max(df['price'])
df['area_sqft_normalize']= normalization_min_max(df['area_sqft'])
df['price_per_sqft_normalize']=normalization_min_max(df['price_per_sqft'])
print(df[['house_id','price','price_normalize','area_sqft_normalize']])