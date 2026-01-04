import pandas as pd
import numpy as np

df = pd.read_csv('sales_real_world_project.csv')

# drop duplicate 
df = df.drop_duplicates(subset='order_id',keep='first')

# fill blank region to unkown region
df['region'] = df['region'].fillna('unknown')

# convert unknown to nan value 

df['region'] = df['region'].replace('unknown',np.nan)

# fill blank region to unkown in discount_percent
df['discount_percent'] = df['discount_percent'].fillna('unknown')

# convert unknown to 0 value 

df['discount_percent'] = df['discount_percent'].replace('unknown',0)

# convert unknown to nan value 

df['region'] = df['region'].replace('unknown',np.nan)


# onvert date to datetime 
df['order_date'] = pd.to_datetime(
    df['order_date'],
    dayfirst=True, # this funtion  Tells Pandas that in the date, day is written first and month is written later.
    errors='coerce'
)

# Delete order date nan value 
d = df.dropna(subset='order_date')

# convert to numeric first

df['sales_amount'] = pd.to_numeric(df['sales_amount'], errors='coerce')

# Removed invalid sales values (<=0) as per business rules
df.loc[df['sales_amount'] <= 0, 'sales_amount'] = np.nan

# clean region
df['region'] = df['region'].replace('Unknown', np.nan)

# Used region-wise mean to preserve regional sales patterns
# Used company mean when region information was missing
company_avg = df['sales_amount'].mean()
region_avg = df.groupby('region')['sales_amount'].transform('mean')


df['sales_amount'] = df['sales_amount'].fillna(
    # region avg lagega jaha humara region not null hai other wise company avg 
    region_avg.where(df['region'].notna(),company_avg)
)


df['quantity'] = df['quantity'].fillna(
    df['quantity'].median()
)

df.to_csv('clean_dataset.csv')

